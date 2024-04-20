# Generated from d:/232/PPL/ASSignments/CO3005-PPL/ASS3/assignment3-initial/assignment3-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#main_stmt.
    def enterMain_stmt(self, ctx:ZCodeParser.Main_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#main_stmt.
    def exitMain_stmt(self, ctx:ZCodeParser.Main_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arg.
    def enterArg(self, ctx:ZCodeParser.ArgContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arg.
    def exitArg(self, ctx:ZCodeParser.ArgContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arglist.
    def enterArglist(self, ctx:ZCodeParser.ArglistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arglist.
    def exitArglist(self, ctx:ZCodeParser.ArglistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argprime.
    def enterArgprime(self, ctx:ZCodeParser.ArgprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argprime.
    def exitArgprime(self, ctx:ZCodeParser.ArgprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argment.
    def enterArgment(self, ctx:ZCodeParser.ArgmentContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argment.
    def exitArgment(self, ctx:ZCodeParser.ArgmentContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcend.
    def enterFuncend(self, ctx:ZCodeParser.FuncendContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcend.
    def exitFuncend(self, ctx:ZCodeParser.FuncendContext):
        pass


    # Enter a parse tree produced by ZCodeParser#builtin.
    def enterBuiltin(self, ctx:ZCodeParser.BuiltinContext):
        pass

    # Exit a parse tree produced by ZCodeParser#builtin.
    def exitBuiltin(self, ctx:ZCodeParser.BuiltinContext):
        pass


    # Enter a parse tree produced by ZCodeParser#readnum.
    def enterReadnum(self, ctx:ZCodeParser.ReadnumContext):
        pass

    # Exit a parse tree produced by ZCodeParser#readnum.
    def exitReadnum(self, ctx:ZCodeParser.ReadnumContext):
        pass


    # Enter a parse tree produced by ZCodeParser#writenum.
    def enterWritenum(self, ctx:ZCodeParser.WritenumContext):
        pass

    # Exit a parse tree produced by ZCodeParser#writenum.
    def exitWritenum(self, ctx:ZCodeParser.WritenumContext):
        pass


    # Enter a parse tree produced by ZCodeParser#readbool.
    def enterReadbool(self, ctx:ZCodeParser.ReadboolContext):
        pass

    # Exit a parse tree produced by ZCodeParser#readbool.
    def exitReadbool(self, ctx:ZCodeParser.ReadboolContext):
        pass


    # Enter a parse tree produced by ZCodeParser#writebool.
    def enterWritebool(self, ctx:ZCodeParser.WriteboolContext):
        pass

    # Exit a parse tree produced by ZCodeParser#writebool.
    def exitWritebool(self, ctx:ZCodeParser.WriteboolContext):
        pass


    # Enter a parse tree produced by ZCodeParser#readstr.
    def enterReadstr(self, ctx:ZCodeParser.ReadstrContext):
        pass

    # Exit a parse tree produced by ZCodeParser#readstr.
    def exitReadstr(self, ctx:ZCodeParser.ReadstrContext):
        pass


    # Enter a parse tree produced by ZCodeParser#writestr.
    def enterWritestr(self, ctx:ZCodeParser.WritestrContext):
        pass

    # Exit a parse tree produced by ZCodeParser#writestr.
    def exitWritestr(self, ctx:ZCodeParser.WritestrContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl.
    def enterVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl.
    def exitVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var_vardecl.
    def enterVar_vardecl(self, ctx:ZCodeParser.Var_vardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var_vardecl.
    def exitVar_vardecl(self, ctx:ZCodeParser.Var_vardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arraydim.
    def enterArraydim(self, ctx:ZCodeParser.ArraydimContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arraydim.
    def exitArraydim(self, ctx:ZCodeParser.ArraydimContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array.
    def enterArray(self, ctx:ZCodeParser.ArrayContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array.
    def exitArray(self, ctx:ZCodeParser.ArrayContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayelement.
    def enterArrayelement(self, ctx:ZCodeParser.ArrayelementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayelement.
    def exitArrayelement(self, ctx:ZCodeParser.ArrayelementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignstmt.
    def enterAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignstmt.
    def exitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifstmt.
    def enterIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifstmt.
    def exitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elifstmt.
    def enterElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elifstmt.
    def exitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elsestmt.
    def enterElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elsestmt.
    def exitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forstmt.
    def enterForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forstmt.
    def exitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#otherstmt.
    def enterOtherstmt(self, ctx:ZCodeParser.OtherstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#otherstmt.
    def exitOtherstmt(self, ctx:ZCodeParser.OtherstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakstmt.
    def enterBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakstmt.
    def exitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continuestmt.
    def enterContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continuestmt.
    def exitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnstmt.
    def enterReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnstmt.
    def exitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockstmt.
    def enterBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockstmt.
    def exitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funccall.
    def enterFunccall(self, ctx:ZCodeParser.FunccallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funccall.
    def exitFunccall(self, ctx:ZCodeParser.FunccallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramlist.
    def enterParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramlist.
    def exitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramprime.
    def enterParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramprime.
    def exitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr1.
    def enterExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr1.
    def exitExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr2.
    def enterExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr2.
    def exitExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr3.
    def enterExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr3.
    def exitExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr4.
    def enterExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr4.
    def exitExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr5.
    def enterExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr5.
    def exitExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr6.
    def enterExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr6.
    def exitExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr7.
    def enterExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr7.
    def exitExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr8.
    def enterExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr8.
    def exitExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr9.
    def enterExpr9(self, ctx:ZCodeParser.Expr9Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr9.
    def exitExpr9(self, ctx:ZCodeParser.Expr9Context):
        pass


    # Enter a parse tree produced by ZCodeParser#relationals.
    def enterRelationals(self, ctx:ZCodeParser.RelationalsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relationals.
    def exitRelationals(self, ctx:ZCodeParser.RelationalsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typ.
    def enterTyp(self, ctx:ZCodeParser.TypContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typ.
    def exitTyp(self, ctx:ZCodeParser.TypContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literals.
    def enterLiterals(self, ctx:ZCodeParser.LiteralsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literals.
    def exitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        pass



del ZCodeParser