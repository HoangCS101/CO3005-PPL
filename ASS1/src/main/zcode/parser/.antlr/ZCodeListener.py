# Generated from d:/232/PPL/ASSignments/ASS1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ZCodeParser#term.
    def enterTerm(self, ctx:ZCodeParser.TermContext):
        pass

    # Exit a parse tree produced by ZCodeParser#term.
    def exitTerm(self, ctx:ZCodeParser.TermContext):
        pass


    # Enter a parse tree produced by ZCodeParser#factor.
    def enterFactor(self, ctx:ZCodeParser.FactorContext):
        pass

    # Exit a parse tree produced by ZCodeParser#factor.
    def exitFactor(self, ctx:ZCodeParser.FactorContext):
        pass


    # Enter a parse tree produced by ZCodeParser#oprand.
    def enterOprand(self, ctx:ZCodeParser.OprandContext):
        pass

    # Exit a parse tree produced by ZCodeParser#oprand.
    def exitOprand(self, ctx:ZCodeParser.OprandContext):
        pass


    # Enter a parse tree produced by ZCodeParser#subexpr.
    def enterSubexpr(self, ctx:ZCodeParser.SubexprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#subexpr.
    def exitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        pass



del ZCodeParser