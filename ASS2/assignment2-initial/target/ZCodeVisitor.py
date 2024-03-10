# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vardecl.
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#im_vardecl.
    def visitIm_vardecl(self, ctx:ZCodeParser.Im_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#im_dydecl.
    def visitIm_dydecl(self, ctx:ZCodeParser.Im_dydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcdecl.
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arg.
    def visitArg(self, ctx:ZCodeParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arglist.
    def visitArglist(self, ctx:ZCodeParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argprime.
    def visitArgprime(self, ctx:ZCodeParser.ArgprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argment.
    def visitArgment(self, ctx:ZCodeParser.ArgmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funcend.
    def visitFuncend(self, ctx:ZCodeParser.FuncendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#builtin.
    def visitBuiltin(self, ctx:ZCodeParser.BuiltinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readnum.
    def visitReadnum(self, ctx:ZCodeParser.ReadnumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writenum.
    def visitWritenum(self, ctx:ZCodeParser.WritenumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readbool.
    def visitReadbool(self, ctx:ZCodeParser.ReadboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writebool.
    def visitWritebool(self, ctx:ZCodeParser.WriteboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#readstr.
    def visitReadstr(self, ctx:ZCodeParser.ReadstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#writestr.
    def visitWritestr(self, ctx:ZCodeParser.WritestrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydecl.
    def visitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arraydim.
    def visitArraydim(self, ctx:ZCodeParser.ArraydimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arrayelement.
    def visitArrayelement(self, ctx:ZCodeParser.ArrayelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elifstmt.
    def visitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elsestmt.
    def visitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#otherstmt.
    def visitOtherstmt(self, ctx:ZCodeParser.OtherstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continuestmt.
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#funccall.
    def visitFunccall(self, ctx:ZCodeParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramlist.
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramprime.
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr9.
    def visitExpr9(self, ctx:ZCodeParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relationals.
    def visitRelationals(self, ctx:ZCodeParser.RelationalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#typ.
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literals.
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        return self.visitChildren(ctx)



del ZCodeParser