from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([VarDecl(Id(ctx.IDENTIFIER().getText()), NumberType())])

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
    
    # literals : NUMBER_LITERAL | STRING_LITERAL | BOOL_LITERAL ;
    def visitLiteral(self, ctx: ZCodeParser.LiteralsContext):
        if ctx.NUMBER_LITERAL():
            return NumberLiteral(ctx.NUMBER_LITERAL().getText())
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        return BooleanLiteral(ctx.BOOL_LITERAL().getText() == 'true')