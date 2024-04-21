from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Symbol:
    def __init__(self, name, typ = VoidType()):
        self.name = name
        self.typ = typ

def infer(id, typ, param):
    for x in param:
        if id.name is x.name:
            x.typ = typ
            return typ
        
def compareTyp(a, b):
    if isinstance(a, NumberType) and isinstance(b, NumberType):
        return True
    if isinstance(a, BoolType) and isinstance(b, BoolType):
        return True
    if isinstance(a, StringType) and isinstance(b, StringType):
        return True
    if isinstance(a, ArrayType) and isinstance(b, ArrayType):
        if a.size == b.size and compareTyp(a.eleType, b.eleType):
            return True
    return False
        
# def intersection(lst1, lst2): 
#     lst3 = [value for value in lst1 if value in lst2] 
#     return lst3 
            
class StaticChecker(BaseVisitor, Utils):
    in_loop = 0
    
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        self.visit(self.ast, [])
        
    # decl: List[Decl]  # empty list if there is no statement in block
    def visitProgram(self, ast, param):
        param = []
        flag = False
        for decl in ast.decl:
            if decl.name.name == 'main':
                flag = True
            param = self.visit(decl , param)
        if not flag: raise NoEntryPoint()
        
    # name: Id
    # varType: Type = None  # None if there is no type
    # modifier: str = None  # None if there is no modifier
    # varInit: Expr = None  # None if there is no initial
    def visitVarDecl(self, ast, param):
        for x in param:
            if x.name == ast.name.name:
                raise Redeclared(Identifier(), ast.name.name)
        if ast.varType is not None:
            if ast.varInit is not None:
                exprTyp = self.visit(ast.varInit, param)
                if not compareTyp(ast.varType, exprTyp):
                    raise TypeMismatchInStatement(ast)
                return param + [Symbol(ast.name.name, exprTyp)]
            return param + [Symbol(ast.name.name, ast.varType)]
        if ast.varInit is not None:
            exprTyp = self.visit(ast.varInit, param)
            return param + [Symbol(ast.name.name, exprTyp)]
        return param + [Symbol(ast.name.name)]

    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
    def visitFuncDecl(self, ast , param):
        for x in param:
            if x.name == ast.name.name:
                raise Redeclared(Identifier(), ast.name.name)
        if ast.param:
            for vardecl in ast.param:
                param = self.visit(vardecl, param)
        if ast.body is not None:
            param = self.visit(ast.body, param)
        return param + [Symbol(ast.name.name)]
    
    def visitNumberType(self, ast, param):
        return NumberType()

    def visitBoolType(self, ast, param):
        return BoolType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitArrayType(self, ast, param):
        return ArrayType()

    def visitBinaryOp(self, ast, param):
        op = ast.op
        ltyp = self.visit(ast.left, param)
        rtyp = self.visit(ast.right, param)
        # print(ltyp, rtyp)

        if op in ['+', '-', '*', '/', '%']:
            # if intersection([type(ltyp), type(rtyp)], [BoolType(), StringType(), ArrayType()]):
            if type(ltyp) is VoidType:
                infer(ast.left, NumberType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, NumberType(), param)
                
            if not compareTyp(ltyp, NumberType()) or not compareTyp(rtyp, NumberType()):
                raise TypeMismatchInExpression(ast)
            
            return NumberType()
        
        if op in ['=', '!=', '>', '>=', '<', '<=']:
            # if intersection([type(ltyp), type(rtyp)], [BoolType(), StringType(), ArrayType()]):
            if type(ltyp) is VoidType:
                infer(ast.left, NumberType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, NumberType(), param)
                
            if not compareTyp(ltyp, NumberType()) or not compareTyp(rtyp, NumberType()):
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
        
        if op in ['and', 'or']:
            # if intersection([type(ltyp), type(rtyp)], [NumberType(), StringType(), ArrayType()]):
            if type(ltyp) is VoidType:
                infer(ast.left, BoolType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, BoolType(), param)
                
            if not compareTyp(ltyp, BoolType()) or not compareTyp(rtyp, BoolType()):
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
        
        if op in ['...']:
            # if intersection([type(ltyp), type(rtyp)], [BoolType(), NumberType(), ArrayType()]):
            if type(ltyp) is VoidType:
                infer(ast.left, StringType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, StringType(), param)
                
            if not compareTyp(ltyp, StringType()) or not compareTyp(rtyp, StringType()):
                raise TypeMismatchInExpression(ast)
            
            return StringType()
        
        if op in ['==']:
            # if intersection([type(ltyp), type(rtyp)], [BoolType(), NumberType(), ArrayType()]):
            if type(ltyp) is VoidType:
                infer(ast.left, StringType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, StringType(), param)
                
            if not compareTyp(ltyp, StringType()) or not compareTyp(rtyp, StringType()):
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
            

    def visitUnaryOp(self, ast, param):
        op = ast.op
        opr = self.visit(ast.operand, param)
        
        if op in ['-']:
            # if type(opr) in [BoolType, StringType, ArrayType]:
            if type(opr) is VoidType:
                infer(ast.operand, NumberType(), param)
                
            if type(opr) is not NumberType:
                raise TypeMismatchInExpression(ast)
            
            return NumberType
        
        if op in ['not']:
            # if type(opr) in [NumberType, StringType, ArrayType]:
            if type(opr) is VoidType:
                infer(ast.operand, BoolType(), param)
                
            if type(opr) is not BoolType:
                raise TypeMismatchInExpression(ast)
            
            return BoolType()

    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast, param):
        for x in param:
            if x.name == ast.name:
                return x.typ
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, param):
        pass

    # stmt: List[Stmt]  # empty list if there is no statement in block
    def visitBlock(self, ast, param):
        env = param.copy()
        for stmt in ast.stmt:
            env = self.visit(stmt , env)
            # print(stmt)

    # expr: Expr
    # thenStmt: Stmt
    # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
    # elseStmt: Stmt = None  # None if there is no else branch
    def visitIf(self, ast, param):
        exprTyp = self.visit(ast.expr, param)
        if not compareTyp(exprTyp, BoolType()):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, param)
        if ast.elifStmt:
            for x in ast.elifStmt:
                exprTyp = self.visit(x[0], param)
                if not compareTyp(exprTyp, BoolType()):
                    raise TypeMismatchInStatement(ast)
        self.visit(ast.elseStmt, param)

    # name: Id
    # condExpr: Expr
    # updExpr: Expr
    # body: Stmt
    def visitFor(self, ast, param):
        self.in_loop += 1
        if not compareTyp(self.visit(ast.name, param), NumberType()):
            raise TypeMismatchInStatement(ast)
        if not compareTyp(self.visit(ast.condExpr, param), BoolType()):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.updExpr, param)
        self.visit(ast.body, param)
        self.in_loop -= 1

    def visitContinue(self, ast, param):
        if self.in_loop <= 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.in_loop <= 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        pass

    # lhs: Expr
    # rhs: Expr
    def visitAssign(self, ast, param):
        ltyp = self.visit(ast.lhs, param)
        rtyp = self.visit(ast.rhs, param)
        # print(ltyp, rtyp, " !!!!!!!!!!!!!!")
        
        if type(ltyp) is VoidType and type(rtyp) is VoidType:
            raise TypeCannotBeInferred(ast)
            
        if type(ltyp) is VoidType:
            infer(ast.lhs, rtyp, param)
            return
        
        if type(rtyp) is VoidType:
            infer(ast.rhs, ltyp, param)
            return
        
        if type(ltyp) is not type(rtyp):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast, param):
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    def visitStringLiteral(self, ast, param):
        return StringType()

    def visitArrayLiteral(self, ast, param):
        return ArrayType()
