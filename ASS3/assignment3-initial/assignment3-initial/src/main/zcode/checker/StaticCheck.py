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
    for env in param:
        if id.name in env:
            env[id.name] = typ
            return typ
        
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
            
class StaticChecker(BaseVisitor, Utils):
    in_loop = 0
    
    def __init__(self, ast):
        self.ast = ast
        
    def check(self):
        self.visit(self.ast, [])
        
    def visitProgram(self, ast, param):
        param = []
        flag = False
        for decl in ast.decl:
            if decl.name.name == 'main':
                flag = True
            param = self.visit(decl , param)
        if not flag: raise NoEntryPoint()
        
    def visitVarDecl(self, ast, param):
        for x in param:
            if x.name == ast.name.name:
                raise Redeclared(Identifier(), ast.name.name)
        return param + [Symbol(ast.name.name)]

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
        
        if op in ['+', '-', '*', '/', '%']:
            if intersection([type(ltyp), type(rtyp)], [BoolType, StringType, ArrayType]):
                raise TypeMismatchInExpression(ast)
            
            if type(ltyp) is VoidType:
                infer(ast.left, NumberType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, NumberType(), param)
                
            return NumberType
        
        if op in ['=', '!=', '>', '>=', '<', '<=']:
            if intersection([type(ltyp), type(rtyp)], [BoolType, StringType, ArrayType]):
                raise TypeMismatchInExpression(ast)
            
            if type(ltyp) is VoidType:
                infer(ast.left, NumberType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, NumberType(), param)
                
            return BoolType()
        
        if op in ['and', 'or']:
            if intersection([type(ltyp), type(rtyp)], [NumberType, StringType, ArrayType]):
                raise TypeMismatchInExpression(ast)
            
            if type(ltyp) is VoidType:
                infer(ast.left, BoolType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, BoolType(), param)
                
            return BoolType()
        
        if op in ['...']:
            if intersection([type(ltyp), type(rtyp)], [BoolType, NumberType, ArrayType]):
                raise TypeMismatchInExpression(ast)
            
            if type(ltyp) is VoidType:
                infer(ast.left, StringType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, StringType(), param)
                
            return StringType()
        
        if op in ['==']:
            if intersection([type(ltyp), type(rtyp)], [BoolType, NumberType, ArrayType]):
                raise TypeMismatchInExpression(ast)
            
            if type(ltyp) is VoidType:
                infer(ast.left, StringType(), param)
            
            if type(rtyp) is VoidType:
                infer(ast.right, StringType(), param)
                
            return BoolType()
            

    def visitUnaryOp(self, ast, param):
        op = ast.op
        opr = self.visit(ast.operand, param)
        
        if op in ['-']:
            if type(opr) in [BoolType, StringType, ArrayType]:
                raise TypeMismatchInExpression(ast)
            
            if type(opr) is VoidType:
                infer(ast.operand, NumberType, param)
                
            return NumberType
        
        if op in ['not']:
            if type(opr) in [NumberType, StringType, ArrayType]:
                raise TypeMismatchInExpression(ast)
            
            if type(opr) is VoidType:
                infer(ast.operand, BoolType(), param)
                
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

    def visitBlock(self, ast, param):
        env = param.copy()
        for stmt in ast.stmt:
            env = self.visit(stmt , env)

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        ltyp = self.visit(ast.lhs, param)
        rtyp = self.visit(ast.exp, param)
        
        if type(ltyp) is VoidType and type(rtyp) is VoidType:
            raise TypeCannotBeInferred(ast)
            
        if type(ltyp) is VoidType:
            infer(ast.lhs, rtyp, param)
            return
        
        if type(rtyp) is VoidType:
            infer(ast.exp, ltyp, param)
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
