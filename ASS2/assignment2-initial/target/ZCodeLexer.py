# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01e4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00d2\n\b\3\b\5\b\u00d5")
        buf.write("\n\b\3\b\5\b\u00d8\n\b\3\t\6\t\u00db\n\t\r\t\16\t\u00dc")
        buf.write("\3\n\3\n\5\n\u00e1\n\n\3\n\3\n\3\13\7\13\u00e6\n\13\f")
        buf.write("\13\16\13\u00e9\13\13\3\f\3\f\3\r\3\r\5\r\u00ef\n\r\3")
        buf.write("\16\3\16\3\16\3\16\7\16\u00f5\n\16\f\16\16\16\u00f8\13")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\5\22\u0109\n\22\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\7<\u01ae\n<\f<\16<\u01b1\13")
        buf.write("<\3=\6=\u01b4\n=\r=\16=\u01b5\3=\3=\3>\3>\3>\5>\u01bd")
        buf.write("\n>\3?\3?\3?\3?\7?\u01c3\n?\f?\16?\u01c6\13?\3?\3?\3@")
        buf.write("\3@\3@\3A\3A\3A\7A\u01d0\nA\fA\16A\u01d3\13A\3A\5A\u01d6")
        buf.write("\nA\3A\3A\3B\3B\3B\7B\u01dd\nB\fB\16B\u01e0\13B\3B\3B")
        buf.write("\3B\2\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\2")
        buf.write("\27\2\31\n\33\13\35\2\37\2!\2#\2%\f\'\r)\16+\17-\20/\21")
        buf.write("\61\22\63\23\65\24\67\259\26;\27=\30?\31A\32C\33E\34G")
        buf.write("\35I\36K\37M O!Q\"S#U$W%Y&[\'](_)a*c+e,g-i.k/m\60o\61")
        buf.write("q\62s\63u\64w\65y\66{\67}8\1779\u0081:\u0083;\3\2\16\3")
        buf.write("\2\62;\4\2GGgg\4\2--//\3\2\60\60\3\2$$\5\2\f\f$$^^\t\2")
        buf.write("))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\13\16\16")
        buf.write("\"\"\4\2\f\f\17\17\3\3\f\f\2\u01ee\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\3\u0085\3\2\2\2\5\u0092\3\2\2\2\7\u009f\3\2\2\2\t\u00aa")
        buf.write("\3\2\2\2\13\u00b5\3\2\2\2\r\u00c2\3\2\2\2\17\u00cf\3\2")
        buf.write("\2\2\21\u00da\3\2\2\2\23\u00de\3\2\2\2\25\u00e7\3\2\2")
        buf.write("\2\27\u00ea\3\2\2\2\31\u00ee\3\2\2\2\33\u00f0\3\2\2\2")
        buf.write("\35\u00fc\3\2\2\2\37\u00fe\3\2\2\2!\u0101\3\2\2\2#\u0108")
        buf.write("\3\2\2\2%\u010a\3\2\2\2\'\u010f\3\2\2\2)\u0115\3\2\2\2")
        buf.write("+\u011c\3\2\2\2-\u0121\3\2\2\2/\u0128\3\2\2\2\61\u012f")
        buf.write("\3\2\2\2\63\u0133\3\2\2\2\65\u013b\3\2\2\2\67\u0140\3")
        buf.write("\2\2\29\u0144\3\2\2\2;\u014a\3\2\2\2=\u014d\3\2\2\2?\u0153")
        buf.write("\3\2\2\2A\u015c\3\2\2\2C\u015f\3\2\2\2E\u0164\3\2\2\2")
        buf.write("G\u0169\3\2\2\2I\u016f\3\2\2\2K\u0173\3\2\2\2M\u0175\3")
        buf.write("\2\2\2O\u0177\3\2\2\2Q\u0179\3\2\2\2S\u017b\3\2\2\2U\u017d")
        buf.write("\3\2\2\2W\u0181\3\2\2\2Y\u0185\3\2\2\2[\u0188\3\2\2\2")
        buf.write("]\u018a\3\2\2\2_\u018d\3\2\2\2a\u0190\3\2\2\2c\u0192\3")
        buf.write("\2\2\2e\u0195\3\2\2\2g\u0197\3\2\2\2i\u019a\3\2\2\2k\u019e")
        buf.write("\3\2\2\2m\u01a1\3\2\2\2o\u01a3\3\2\2\2q\u01a5\3\2\2\2")
        buf.write("s\u01a7\3\2\2\2u\u01a9\3\2\2\2w\u01ab\3\2\2\2y\u01b3\3")
        buf.write("\2\2\2{\u01bc\3\2\2\2}\u01be\3\2\2\2\177\u01c9\3\2\2\2")
        buf.write("\u0081\u01cc\3\2\2\2\u0083\u01d9\3\2\2\2\u0085\u0086\7")
        buf.write("t\2\2\u0086\u0087\7g\2\2\u0087\u0088\7c\2\2\u0088\u0089")
        buf.write("\7f\2\2\u0089\u008a\7P\2\2\u008a\u008b\7w\2\2\u008b\u008c")
        buf.write("\7o\2\2\u008c\u008d\7d\2\2\u008d\u008e\7g\2\2\u008e\u008f")
        buf.write("\7t\2\2\u008f\u0090\7*\2\2\u0090\u0091\7+\2\2\u0091\4")
        buf.write("\3\2\2\2\u0092\u0093\7y\2\2\u0093\u0094\7t\2\2\u0094\u0095")
        buf.write("\7k\2\2\u0095\u0096\7v\2\2\u0096\u0097\7g\2\2\u0097\u0098")
        buf.write("\7P\2\2\u0098\u0099\7w\2\2\u0099\u009a\7o\2\2\u009a\u009b")
        buf.write("\7d\2\2\u009b\u009c\7g\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7*\2\2\u009e\6\3\2\2\2\u009f\u00a0\7t\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7f\2\2\u00a3\u00a4")
        buf.write("\7D\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7")
        buf.write("\7n\2\2\u00a7\u00a8\7*\2\2\u00a8\u00a9\7+\2\2\u00a9\b")
        buf.write("\3\2\2\2\u00aa\u00ab\7y\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7g\2\2\u00af\u00b0")
        buf.write("\7D\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7*\2\2\u00b4\n\3\2\2\2\u00b5\u00b6")
        buf.write("\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9")
        buf.write("\7f\2\2\u00b9\u00ba\7U\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7i\2\2\u00bf\u00c0\7*\2\2\u00c0\u00c1\7+\2\2\u00c1\f")
        buf.write("\3\2\2\2\u00c2\u00c3\7y\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7U\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd\7i\2\2\u00cd\u00ce")
        buf.write("\7*\2\2\u00ce\16\3\2\2\2\u00cf\u00d1\5\21\t\2\u00d0\u00d2")
        buf.write("\5\27\f\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d4\3\2\2\2\u00d3\u00d5\5\25\13\2\u00d4\u00d3\3\2\2")
        buf.write("\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d8")
        buf.write("\5\23\n\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\20\3\2\2\2\u00d9\u00db\t\2\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\22\3\2\2\2\u00de\u00e0\t\3\2\2\u00df\u00e1\t\4")
        buf.write("\2\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e3\5\25\13\2\u00e3\24\3\2\2\2\u00e4")
        buf.write("\u00e6\t\2\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e9\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\26\3\2")
        buf.write("\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\t\5\2\2\u00eb\30")
        buf.write("\3\2\2\2\u00ec\u00ef\5%\23\2\u00ed\u00ef\5\'\24\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\32\3\2\2\2\u00f0")
        buf.write("\u00f6\t\6\2\2\u00f1\u00f5\5\35\17\2\u00f2\u00f5\5\37")
        buf.write("\20\2\u00f3\u00f5\5!\21\2\u00f4\u00f1\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f9\u00fa\t\6\2\2\u00fa\u00fb\b")
        buf.write("\16\2\2\u00fb\34\3\2\2\2\u00fc\u00fd\n\7\2\2\u00fd\36")
        buf.write("\3\2\2\2\u00fe\u00ff\7^\2\2\u00ff\u0100\t\b\2\2\u0100")
        buf.write(" \3\2\2\2\u0101\u0102\7)\2\2\u0102\u0103\t\6\2\2\u0103")
        buf.write("\"\3\2\2\2\u0104\u0105\7^\2\2\u0105\u0109\n\b\2\2\u0106")
        buf.write("\u0107\7)\2\2\u0107\u0109\n\6\2\2\u0108\u0104\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0109$\3\2\2\2\u010a\u010b\7v\2\2")
        buf.write("\u010b\u010c\7t\2\2\u010c\u010d\7w\2\2\u010d\u010e\7g")
        buf.write("\2\2\u010e&\3\2\2\2\u010f\u0110\7h\2\2\u0110\u0111\7c")
        buf.write("\2\2\u0111\u0112\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114")
        buf.write("\7g\2\2\u0114(\3\2\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7w\2\2\u0117\u0118\7o\2\2\u0118\u0119\7d\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7t\2\2\u011b*\3\2\2\2\u011c\u011d")
        buf.write("\7d\2\2\u011d\u011e\7q\2\2\u011e\u011f\7q\2\2\u011f\u0120")
        buf.write("\7n\2\2\u0120,\3\2\2\2\u0121\u0122\7u\2\2\u0122\u0123")
        buf.write("\7v\2\2\u0123\u0124\7t\2\2\u0124\u0125\7k\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\u0127\7i\2\2\u0127.\3\2\2\2\u0128\u0129")
        buf.write("\7t\2\2\u0129\u012a\7g\2\2\u012a\u012b\7v\2\2\u012b\u012c")
        buf.write("\7w\2\2\u012c\u012d\7t\2\2\u012d\u012e\7p\2\2\u012e\60")
        buf.write("\3\2\2\2\u012f\u0130\7x\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\62\3\2\2\2\u0133\u0134\7f\2\2\u0134\u0135")
        buf.write("\7{\2\2\u0135\u0136\7p\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7o\2\2\u0138\u0139\7k\2\2\u0139\u013a\7e\2\2\u013a\64")
        buf.write("\3\2\2\2\u013b\u013c\7h\2\2\u013c\u013d\7w\2\2\u013d\u013e")
        buf.write("\7p\2\2\u013e\u013f\7e\2\2\u013f\66\3\2\2\2\u0140\u0141")
        buf.write("\7h\2\2\u0141\u0142\7q\2\2\u0142\u0143\7t\2\2\u01438\3")
        buf.write("\2\2\2\u0144\u0145\7w\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7k\2\2\u0148\u0149\7n\2\2\u0149:\3")
        buf.write("\2\2\2\u014a\u014b\7d\2\2\u014b\u014c\7{\2\2\u014c<\3")
        buf.write("\2\2\2\u014d\u014e\7d\2\2\u014e\u014f\7t\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150\u0151\7c\2\2\u0151\u0152\7m\2\2\u0152>\3")
        buf.write("\2\2\2\u0153\u0154\7e\2\2\u0154\u0155\7q\2\2\u0155\u0156")
        buf.write("\7p\2\2\u0156\u0157\7v\2\2\u0157\u0158\7k\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159\u015a\7w\2\2\u015a\u015b\7g\2\2\u015b@\3")
        buf.write("\2\2\2\u015c\u015d\7k\2\2\u015d\u015e\7h\2\2\u015eB\3")
        buf.write("\2\2\2\u015f\u0160\7g\2\2\u0160\u0161\7n\2\2\u0161\u0162")
        buf.write("\7u\2\2\u0162\u0163\7g\2\2\u0163D\3\2\2\2\u0164\u0165")
        buf.write("\7g\2\2\u0165\u0166\7n\2\2\u0166\u0167\7k\2\2\u0167\u0168")
        buf.write("\7h\2\2\u0168F\3\2\2\2\u0169\u016a\7d\2\2\u016a\u016b")
        buf.write("\7g\2\2\u016b\u016c\7i\2\2\u016c\u016d\7k\2\2\u016d\u016e")
        buf.write("\7p\2\2\u016eH\3\2\2\2\u016f\u0170\7g\2\2\u0170\u0171")
        buf.write("\7p\2\2\u0171\u0172\7f\2\2\u0172J\3\2\2\2\u0173\u0174")
        buf.write("\7-\2\2\u0174L\3\2\2\2\u0175\u0176\7/\2\2\u0176N\3\2\2")
        buf.write("\2\u0177\u0178\7,\2\2\u0178P\3\2\2\2\u0179\u017a\7\61")
        buf.write("\2\2\u017aR\3\2\2\2\u017b\u017c\7\'\2\2\u017cT\3\2\2\2")
        buf.write("\u017d\u017e\7p\2\2\u017e\u017f\7q\2\2\u017f\u0180\7v")
        buf.write("\2\2\u0180V\3\2\2\2\u0181\u0182\7c\2\2\u0182\u0183\7p")
        buf.write("\2\2\u0183\u0184\7f\2\2\u0184X\3\2\2\2\u0185\u0186\7q")
        buf.write("\2\2\u0186\u0187\7t\2\2\u0187Z\3\2\2\2\u0188\u0189\7?")
        buf.write("\2\2\u0189\\\3\2\2\2\u018a\u018b\7>\2\2\u018b\u018c\7")
        buf.write("/\2\2\u018c^\3\2\2\2\u018d\u018e\7#\2\2\u018e\u018f\7")
        buf.write("?\2\2\u018f`\3\2\2\2\u0190\u0191\7>\2\2\u0191b\3\2\2\2")
        buf.write("\u0192\u0193\7>\2\2\u0193\u0194\7?\2\2\u0194d\3\2\2\2")
        buf.write("\u0195\u0196\7@\2\2\u0196f\3\2\2\2\u0197\u0198\7@\2\2")
        buf.write("\u0198\u0199\7?\2\2\u0199h\3\2\2\2\u019a\u019b\7\60\2")
        buf.write("\2\u019b\u019c\7\60\2\2\u019c\u019d\7\60\2\2\u019dj\3")
        buf.write("\2\2\2\u019e\u019f\7?\2\2\u019f\u01a0\7?\2\2\u01a0l\3")
        buf.write("\2\2\2\u01a1\u01a2\7.\2\2\u01a2n\3\2\2\2\u01a3\u01a4\7")
        buf.write("*\2\2\u01a4p\3\2\2\2\u01a5\u01a6\7+\2\2\u01a6r\3\2\2\2")
        buf.write("\u01a7\u01a8\7]\2\2\u01a8t\3\2\2\2\u01a9\u01aa\7_\2\2")
        buf.write("\u01aav\3\2\2\2\u01ab\u01af\t\t\2\2\u01ac\u01ae\t\n\2")
        buf.write("\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0x\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b2\u01b4\t\13\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01b8\b=\3\2\u01b8z\3\2\2\2")
        buf.write("\u01b9\u01bd\t\f\2\2\u01ba\u01bb\7\17\2\2\u01bb\u01bd")
        buf.write("\7\f\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write("|\3\2\2\2\u01be\u01bf\7%\2\2\u01bf\u01c0\7%\2\2\u01c0")
        buf.write("\u01c4\3\2\2\2\u01c1\u01c3\n\f\2\2\u01c2\u01c1\3\2\2\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3")
        buf.write("\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8")
        buf.write("\b?\3\2\u01c8~\3\2\2\2\u01c9\u01ca\13\2\2\2\u01ca\u01cb")
        buf.write("\b@\4\2\u01cb\u0080\3\2\2\2\u01cc\u01d1\7$\2\2\u01cd\u01d0")
        buf.write("\5\35\17\2\u01ce\u01d0\5\37\20\2\u01cf\u01cd\3\2\2\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3")
        buf.write("\2\2\2\u01d4\u01d6\t\r\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7\u01d8\bA\5\2\u01d8\u0082\3\2\2\2\u01d9")
        buf.write("\u01de\7$\2\2\u01da\u01dd\5\35\17\2\u01db\u01dd\5\37\20")
        buf.write("\2\u01dc\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd\u01e0")
        buf.write("\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df")
        buf.write("\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e2\5#\22\2")
        buf.write("\u01e2\u01e3\bB\6\2\u01e3\u0084\3\2\2\2\26\2\u00d1\u00d4")
        buf.write("\u00d7\u00dc\u00e0\u00e7\u00ee\u00f4\u00f6\u0108\u01af")
        buf.write("\u01b5\u01bc\u01c4\u01cf\u01d1\u01d5\u01dc\u01de\7\3\16")
        buf.write("\2\b\2\2\3@\3\3A\4\3B\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NUMBER_LITERAL = 7
    BOOL_LITERAL = 8
    STRING_LITERAL = 9
    TRUE = 10
    FALSE = 11
    NUMBER = 12
    BOOL = 13
    STRING = 14
    RETURN = 15
    VAR = 16
    DYNAMIC = 17
    FUNC = 18
    FOR = 19
    UNTIL = 20
    BY = 21
    BREAK = 22
    CONTINUE = 23
    IF = 24
    ELSE = 25
    ELIF = 26
    BEGIN = 27
    END = 28
    PLUS = 29
    MINUS = 30
    MULTIPLY = 31
    DIVIDE = 32
    MODULO = 33
    NOT = 34
    AND = 35
    OR = 36
    ASSIGN = 37
    ARROW = 38
    NOT_EQUAL = 39
    LESS_THAN = 40
    LESS_THAN_OR_EQUAL = 41
    GREATER_THAN = 42
    GREATER_THAN_OR_EQUAL = 43
    ELLIPSIS = 44
    EQUAL = 45
    COMMA = 46
    LPAREN = 47
    RPAREN = 48
    LBRACKET = 49
    RBRACKET = 50
    IDENTIFIER = 51
    WS = 52
    NEWLINE = 53
    COMMENT = 54
    ERROR_CHAR = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readNumber()'", "'writeNumber('", "'readBool()'", "'writeBool('", 
            "'readString()'", "'writeString('", "'true'", "'false'", "'number'", 
            "'bool'", "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
            "'for'", "'until'", "'by'", "'break'", "'continue'", "'if'", 
            "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "','", "'('", 
            "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER_LITERAL", "BOOL_LITERAL", "STRING_LITERAL", "TRUE", 
            "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
            "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
            "ELIF", "BEGIN", "END", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
            "MODULO", "NOT", "AND", "OR", "ASSIGN", "ARROW", "NOT_EQUAL", 
            "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
            "ELLIPSIS", "EQUAL", "COMMA", "LPAREN", "RPAREN", "LBRACKET", 
            "RBRACKET", "IDENTIFIER", "WS", "NEWLINE", "COMMENT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NUMBER_LITERAL", 
                  "INT", "EXP_PART", "INT_PART", "DOT", "BOOL_LITERAL", 
                  "STRING_LITERAL", "STR_CHAR", "ESCAPE_SEQUENCE", "DOUBQ", 
                  "ESCAPE_ERROR", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                  "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                  "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "NOT", 
                  "AND", "OR", "ASSIGN", "ARROW", "NOT_EQUAL", "LESS_THAN", 
                  "LESS_THAN_OR_EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
                  "ELLIPSIS", "EQUAL", "COMMA", "LPAREN", "RPAREN", "LBRACKET", 
                  "RBRACKET", "IDENTIFIER", "WS", "NEWLINE", "COMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.STRING_LITERAL_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = str(self.text)[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	content = str(self.text)
            	esc = '\n'
            	if content[-1] in esc:
            		raise UncloseString(content[1:-1])
            	else:
            		raise UncloseString(content[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(str(self.text)[1:])

     


