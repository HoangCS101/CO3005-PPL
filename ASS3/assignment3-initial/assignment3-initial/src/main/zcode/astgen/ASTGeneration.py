from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
# dont to use intellisense
# from main.zcode.utils.AST import *

class ASTGeneration(ZCodeVisitor):

    # program: NEWLINE*? main_stmt (NEWLINE+ main_stmt)* NEWLINE+ EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.main_stmt()])

    # main_stmt: (
	# 	vardecl
	# 	| im_vardecl
	# 	| im_dydecl
	# 	| funcdecl
	# 	| arraydecl
	# );
    def visitMain_stmt(self, ctx:ZCodeParser.Main_stmtContext):
        return self.visit(ctx.getChild(0))

    # stmt: (
	# 	vardecl
	# 	| im_vardecl
	# 	| im_dydecl 
	# 	| builtin
	# 	| funccall
	# 	| arraydecl
	# 	| assignstmt
	# 	| ifstmt
	# 	| forstmt
	# 	| otherstmt
	# 	| expr
	# );
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visit(ctx.getChild(0))

    # # vardecl: typ IDENTIFIER (ARROW expr)? ;
    # def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
    #     id = Id(ctx.IDENTIFIER().getText())
    #     if ctx.expr():
    #         return VarDecl(id , self.visit(ctx.typ()) , varInit=self.visit(ctx.expr()))
    #     return VarDecl(id , self.visit(ctx.typ()))

    # # im_vardecl: VAR IDENTIFIER ARROW expr ;
    # def visitIm_vardecl(self, ctx:ZCodeParser.Im_vardeclContext):
    #     return VarDecl(Id(ctx.IDENTIFIER().getText()) , modifier=ctx.VAR().getText() , varInit=self.visit(ctx.expr()))


    # # im_dydecl: DYNAMIC IDENTIFIER (ARROW expr)? ;
    # def visitIm_dydecl(self, ctx:ZCodeParser.Im_dydeclContext):
    #     if ctx.expr():
    #         return VarDecl(Id(ctx.IDENTIFIER().getText()) , modifier=ctx.DYNAMIC().getText() , varInit=self.visit(ctx.expr()))
    #     return VarDecl(Id(ctx.IDENTIFIER().getText()) , modifier=ctx.DYNAMIC().getText())


    # funcdecl: FUNC IDENTIFIER arg funcend?;
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()) , self.visit(ctx.arg()) , self.visit(ctx.funcend()) if ctx.funcend() else None)

    # arg: LPAREN arglist RPAREN;
    def visitArg(self, ctx:ZCodeParser.ArgContext):
        return self.visit(ctx.arglist())


    # arglist: argprime | ;
    def visitArglist(self, ctx:ZCodeParser.ArglistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.argprime())
        return []


    # argprime: argment COMMA argprime | argment;
    def visitArgprime(self, ctx:ZCodeParser.ArgprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.argment())]
        return [self.visit(ctx.argment())] + self.visit(ctx.argprime())


    # argment: vardecl ;
    def visitArgment(self, ctx:ZCodeParser.ArgmentContext):
        return self.visit(ctx.vardecl())


    # funcend: NEWLINE* ( returnstmt | blockstmt);
    def visitFuncend(self, ctx:ZCodeParser.FuncendContext):
        if ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        return self.visit(ctx.blockstmt())


    # builtin:
	# readnum
	# | writenum
	# | readbool
	# | writebool
	# | readstr
	# | writestr;
    def visitBuiltin(self, ctx:ZCodeParser.BuiltinContext):
        return self.visit(ctx.getChild(0))


    # readnum: 'readNumber' LPAREN RPAREN;
    def visitReadnum(self, ctx:ZCodeParser.ReadnumContext):
        return CallStmt(Id(ctx.getChild(0)) , [])


    # writenum: 'writeNumber' LPAREN expr RPAREN ;
    def visitWritenum(self, ctx:ZCodeParser.WritenumContext):
        return CallStmt(Id(ctx.getChild(0)) , [self.visit(ctx.expr())])


    # readbool: 'readBool' LPAREN RPAREN ;
    def visitReadbool(self, ctx:ZCodeParser.ReadboolContext):
        return CallStmt(Id(ctx.getChild(0)) , [])


    # writebool: 'writeBool' LPAREN expr RPAREN ;
    def visitWritebool(self, ctx:ZCodeParser.WriteboolContext):
        return CallStmt(Id(ctx.getChild(0)) , [self.visit(ctx.expr())])


    # readstr: 'readString' LPAREN RPAREN ;
    def visitReadstr(self, ctx:ZCodeParser.ReadstrContext):
        return CallStmt(Id(ctx.getChild(0)) , [])


    # writestr: 'writeString' LPAREN expr RPAREN ;
    def visitWritestr(self, ctx:ZCodeParser.WritestrContext):
        return CallStmt(Id(ctx.getChild(0)) , [self.visit(ctx.expr())])
    
    # arraydecl: (typ | DYNAMIC) IDENTIFIER (LBRACKET arraydim RBRACKET)? (ARROW array | ARROW expr)?;
    def visitVardecl(self, ctx: ZCodeParser.VardeclContext):
        varTyp = self.visit(ctx.typ()) if ctx.typ() else None
        if ctx.arraydim():
            varTyp = ArrayType(self.visit(ctx.arraydim()) , self.visit(ctx.typ())) if ctx.typ() else None
        modi = ctx.DYNAMIC().getText() if ctx.DYNAMIC() else None
        varIni = None
        if ctx.array():
            varIni = self.visit(ctx.array())
        elif ctx.expr():
            varIni = self.visit(ctx.expr())
        return VarDecl(name=Id(ctx.IDENTIFIER().getText()) , varType=varTyp , modifier=modi , varInit=varIni )
    
    # var_arraydecl:
	# VAR IDENTIFIER (LBRACKET arraydim RBRACKET)? (
	# 	ARROW array
	# 	| ARROW expr
	# );
    def visitVar_vardecl(self, ctx: ZCodeParser.Var_vardeclContext):
        modi = ctx.VAR().getText()
        varIni = None
        if ctx.array():
            varIni = self.visit(ctx.array())
        else:
            varIni = self.visit(ctx.expr())
        return VarDecl(name=Id(ctx.IDENTIFIER().getText()) , modifier=modi , varInit=varIni )
    
    # arraydim: NUMBER_LITERAL (COMMA NUMBER_LITERAL)*;
    def visitArraydim(self, ctx: ZCodeParser.ArraydimContext):
        res = []
        for n in ctx.NUMBER_LITERAL():
            res += [float(n.getText())]
        return res
    
    # array: LBRACKET arrayelement (COMMA arrayelement)* RBRACKET ;
    def visitArray(self, ctx: ZCodeParser.ArrayContext):
        res = []
        for ele in ctx.arrayelement():
            res += [self.visit(ele)]
        return ArrayLiteral(res)
    
    # arrayelement: expr | array;
    def visitArrayelement(self, ctx: ZCodeParser.ArrayelementContext):
        return self.visit(ctx.getChild(0))
    
    # assignstmt: expr ARROW expr ;
    def visitAssignstmt(self, ctx: ZCodeParser.AssignstmtContext):
        return Assign( self.visit(ctx.expr(0)) , self.visit(ctx.expr(1)) )
    
    # ifstmt: IF expr NEWLINE* stmt elifstmt elsestmt;
    def visitIfstmt(self, ctx: ZCodeParser.IfstmtContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt()), self.visit(ctx.elifstmt()), self.visit(ctx.elsestmt()) )
    
    # elifstmt: ELIF expr NEWLINE* stmt elifstmt |;
    def visitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        if ctx.getChildCount() == 0:
            return []
        return [(self.visit(ctx.expr()), self.visit(ctx.stmt()))] + self.visit(ctx.elifstmt())
    
    # elsestmt: ELSE stmt |;
    def visitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        if ctx.getChildCount() != 0:
            return self.visit(ctx.stmt())

    
    # forstmt: FOR IDENTIFIER UNTIL expr BY expr NEWLINE? stmt ;
    def visitForstmt(self, ctx: ZCodeParser.ForstmtContext):
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)) , self.visit(ctx.stmt()))
    
    # otherstmt: breakstmt | continuestmt | returnstmt | blockstmt ;
    def visitOtherstmt(self, ctx: ZCodeParser.OtherstmtContext):
        return self.visit(ctx.getChild(0))
    
    # breakstmt: BREAK ;
    def visitBreakstmt(self, ctx: ZCodeParser.BreakstmtContext):
        return Break()
    
    # continuestmt: CONTINUE ;
    def visitContinuestmt(self, ctx: ZCodeParser.ContinuestmtContext):
        return Continue()
    
    # returnstmt: RETURN expr? ;
    def visitReturnstmt(self, ctx: ZCodeParser.ReturnstmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)
    
    # blockstmt: BEGIN NEWLINE (stmt (NEWLINE stmt)* | ) NEWLINE END;
    def visitBlockstmt(self, ctx: ZCodeParser.BlockstmtContext):
        return Block([self.visit(x) for x in ctx.stmt()] if ctx.stmt() else [])
    
    # funccall: IDENTIFIER LPAREN paramlist RPAREN | builtin;
    def visitFunccall(self, ctx: ZCodeParser.FunccallContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.builtin())
        return CallStmt( Id(ctx.IDENTIFIER().getText()) , self.visit(ctx.paramlist()) )
    
    # paramlist: paramprime | ;
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.paramprime())
        return []
    
    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.paramprime())

    # expr: expr1 ELLIPSIS expr1 | expr1;
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        op = ctx.ELLIPSIS().getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinaryOp(op, left, right)
    
    # expr1: expr2 relationals expr2 | expr2;
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        op = self.visit(ctx.relationals())
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        return BinaryOp(op, left, right)
    
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)
    
    # expr3: expr3 (PLUS | MINUS) expr4 | expr4;
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)
    
    # expr4: expr4 (MULTIPLY | DIVIDE | MODULO) expr5 | expr5;
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinaryOp(op, left, right)
    
    # expr5: NOT expr5 | expr6;
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            opr = self.visit(ctx.expr5())
            return UnaryOp(op, opr)
        else: 
            return self.visit(ctx.expr6())
        
    # expr6: MINUS expr6 | expr7;
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.MINUS():
            op = ctx.MINUS().getText()
            opr = self.visit(ctx.expr6())
            return UnaryOp(op, opr)
        else: 
            return self.visit(ctx.expr7())
    
    # expr7: (IDENTIFIER | funccall) LBRACKET expr8 RBRACKET | expr9;
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr9())
        if ctx.funccall():
            call_res = self.visit(ctx.funccall())
            arr = CallExpr(call_res.name, call_res.args)
        if ctx.IDENTIFIER():
            arr = Id(ctx.IDENTIFIER().getText())
        return ArrayCell(arr , self.visit(ctx.expr8()))
            
    # expr8: expr COMMA expr8 | expr;
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expr8())
    
    # expr9: literals | LPAREN expr RPAREN | funccall | IDENTIFIER ;
    def visitExpr9(self, ctx:ZCodeParser.Expr9Context):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.funccall():
            call_res = self.visit(ctx.funccall())
            return CallExpr(call_res.name, call_res.args)
        return Id(ctx.IDENTIFIER().getText())
        
    # relationals: ASSIGN | EQUAL| NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL ;
    def visitRelationals(self, ctx:ZCodeParser.RelationalsContext):
        return ctx.getChild(0).getText()
    
    # typ : NUMBER | BOOL | STRING ;
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()
    
    # literals : NUMBER_LITERAL | STRING_LITERAL | BOOL_LITERAL ;
    def visitLiterals(self, ctx:ZCodeParser.LiteralsContext):
        if ctx.NUMBER_LITERAL():
            return NumberLiteral(float(ctx.NUMBER_LITERAL().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        return BooleanLiteral(ctx.BOOL_LITERAL().getText() == 'true')