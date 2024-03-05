from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])

    # ifstmt: IF ifexpr stmt (ELIF ifexpr stmt)* (ELSE stmt)?;
    def visitIfstmt(self, ctx: ZCodeParser.IfstmtContext):
        return []
    
    # ifexpr: LPAREN expr RPAREN ;
    def visitIfexpr(self, ctx: ZCodeParser.IfexprContext):
        return self.visit(ctx.expr())
    
    # forstmt: FOR IDENTIFIER UNTIL expr BY expr NEWLINE? stmt ;
    def visitForstmt(self, ctx: ZCodeParser.ForstmtContext):
        return For(ctx.IDENTIFIER().getText(), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)) , self.visit(ctx.stmt()))
    
    # otherstmt: breakstmt | continuestmt | returnstmt | blockstmt ;
    def visitOtherstmt(self, ctx: ZCodeParser.OtherstmtContext):
        if ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        if ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        if ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        return self.visit(ctx.blockstmt())
    
    # breakstmt: BREAK ;
    def visitBreakstmt(self, ctx: ZCodeParser.BreakstmtContext):
        return Break()
    
    # continuestmt: CONTINUE ;
    def visitContinuestmt(self, ctx: ZCodeParser.ContinuestmtContext):
        return Continue()
    
    # returnstmt: RETURN expr? ;
    def visitReturnstmt(self, ctx: ZCodeParser.ReturnstmtContext):
        return Return(self.visit(ctx.expr()))
    
    # blockstmt: BEGIN NEWLINE? stmt*? NEWLINE? END ;
    def visitBlockstmt(self, ctx: ZCodeParser.BlockstatementContext):
        return Block(self.visit(ctx.stmt()))
    
    # funccall: IDENTIFIER paramdecl | builtin;
    def visitFunccall(self, ctx: ZCodeParser.FunccallContext):
        if ctx.builtin():
            return self.visit(ctx.builtin())
        return CallStmt(self.visit(ctx.IDENTIFIER().getText() , self.visit(ctx.paramdecl())))
    
    # paramdecl: LPAREN paramlist RPAREN;
    def visitParamdecl(self, ctx: ZCodeParser.ParamDeclContext):
        return self.visit(ctx.paramlist())
    
    # paramlist: paramprime | ;
    def visitParamList(self, ctx: ZCodeParser.ParamListContext):
        if ctx.getChildCount() == 1:
            return self.visitProgram(ctx.paramprime())
        return []
    
    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx: ZCodeParser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.param())
        return [self.visit(ctx.param())] + self.visit(ctx.paramprime())

    # param: literals | funccall | IDENTIFIER | expr;
    def visitParam(self, ctx: ZCodeParser.ParamContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        return self.visit(ctx.expr())

    # expr: expr1 ELLIPSIS expr1 | expr1;
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1())
        op = ctx.ELLIPSIS().getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinaryOp(op, left, right)
    
    # expr1: expr2 relationals expr2 | expr2;
    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2())
        op = self.visit(ctx.relationals())
        left = self.visit(ctx.expr1())
        right = self.visit(ctx.expr2())
        return BinaryOp(op, left, right)
    
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)
    
    # expr3: expr3 (PLUS | MINUS) expr4 | expr4;
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)
    
    # expr4: expr4 (MULTIPLY | DIVIDE | MODULO) expr5 | expr5;
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinaryOp(op, left, right)
    
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        op = ctx.NOT().getText()
        opr = self.visit(ctx.expr5())
        return UnaryOp(op, opr)
        
    # expr6: MINUS expr6 | expr7;
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        op = ctx.MINUS().getText()
        opr = self.visit(ctx.expr6())
        return UnaryOp(op, opr)
    
    # expr7: (IDENTIFIER | funccall) LBRACKET expr8 RBRACKET | expr9;
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        arr = ctx.IDENTIFIER().getText() if ctx.IDENTIFIER() else self.visit(ctx.funcall())
        return ArrayCell(arr , self.visit(ctx.expr8()))
            
    # expr8: expr COMMA expr8 | expr;
    def visitExpr8(self, ctx: ZCodeParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr())
        return [self.visit(ctx.expr())] + self.visit(ctx.expr8())
    
    # expr9: literals | LPAREN expr RPAREN | funccall | IDENTIFIER;
    def visitExpr9(self, ctx: ZCodeParser.Expr9Context):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        return ctx.IDENTIFIER().getText()
        
    # relationals: ASSIGN | EQUAL| NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL ;
    def visitRelationals(self, ctx: ZCodeParser.RelationalsContext):
        return ctx.getChild(0).getText()
    
    # typ : NUMBER | BOOL | STRING ;
    def visitTyp(self, ctx: ZCodeParser.TypedContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()
    
    # literals : NUMBER_LITERAL | STRING_LITERAL | BOOL_LITERAL ;
    def visitLiteral(self, ctx: ZCodeParser.LiteralsContext):
        if ctx.NUMBER_LITERAL():
            return NumberLiteral(ctx.NUMBER_LITERAL().getText())
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        return BooleanLiteral(ctx.BOOL_LITERAL().getText() == 'true')