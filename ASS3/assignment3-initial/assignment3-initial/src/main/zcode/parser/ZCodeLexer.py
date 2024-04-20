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
        buf.write("\u01db\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00c9")
        buf.write("\n\b\3\b\5\b\u00cc\n\b\3\b\5\b\u00cf\n\b\3\t\6\t\u00d2")
        buf.write("\n\t\r\t\16\t\u00d3\3\n\3\n\5\n\u00d8\n\n\3\n\3\n\3\13")
        buf.write("\7\13\u00dd\n\13\f\13\16\13\u00e0\13\13\3\f\3\f\3\r\3")
        buf.write("\r\5\r\u00e6\n\r\3\16\3\16\3\16\3\16\7\16\u00ec\n\16\f")
        buf.write("\16\16\16\u00ef\13\16\3\16\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u0100")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\7<\u01a5\n<\f")
        buf.write("<\16<\u01a8\13<\3=\6=\u01ab\n=\r=\16=\u01ac\3=\3=\3>\3")
        buf.write(">\3>\5>\u01b4\n>\3?\3?\3?\3?\7?\u01ba\n?\f?\16?\u01bd")
        buf.write("\13?\3?\3?\3@\3@\3@\3A\3A\3A\7A\u01c7\nA\fA\16A\u01ca")
        buf.write("\13A\3A\5A\u01cd\nA\3A\3A\3B\3B\3B\7B\u01d4\nB\fB\16B")
        buf.write("\u01d7\13B\3B\3B\3B\2\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\2\23\2\25\2\27\2\31\n\33\13\35\2\37\2!\2#\2%\f\'\r")
        buf.write(")\16+\17-\20/\21\61\22\63\23\65\24\67\259\26;\27=\30?")
        buf.write("\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%Y&[\'](_)a*c+")
        buf.write("e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\3\2\16\3\2\62;\4\2GGgg\4\2--//\3\2\60\60\3\2")
        buf.write("$$\5\2\f\f$$^^\t\2))^^ddhhppttvv\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\5\2\n\13\16\16\"\"\4\2\f\f\17\17\3\3\f\f\2\u01e5")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\3\u0085\3\2\2\2\5\u0090\3\2\2")
        buf.write("\2\7\u009c\3\2\2\2\t\u00a5\3\2\2\2\13\u00af\3\2\2\2\r")
        buf.write("\u00ba\3\2\2\2\17\u00c6\3\2\2\2\21\u00d1\3\2\2\2\23\u00d5")
        buf.write("\3\2\2\2\25\u00de\3\2\2\2\27\u00e1\3\2\2\2\31\u00e5\3")
        buf.write("\2\2\2\33\u00e7\3\2\2\2\35\u00f3\3\2\2\2\37\u00f5\3\2")
        buf.write("\2\2!\u00f8\3\2\2\2#\u00ff\3\2\2\2%\u0101\3\2\2\2\'\u0106")
        buf.write("\3\2\2\2)\u010c\3\2\2\2+\u0113\3\2\2\2-\u0118\3\2\2\2")
        buf.write("/\u011f\3\2\2\2\61\u0126\3\2\2\2\63\u012a\3\2\2\2\65\u0132")
        buf.write("\3\2\2\2\67\u0137\3\2\2\29\u013b\3\2\2\2;\u0141\3\2\2")
        buf.write("\2=\u0144\3\2\2\2?\u014a\3\2\2\2A\u0153\3\2\2\2C\u0156")
        buf.write("\3\2\2\2E\u015b\3\2\2\2G\u0160\3\2\2\2I\u0166\3\2\2\2")
        buf.write("K\u016a\3\2\2\2M\u016c\3\2\2\2O\u016e\3\2\2\2Q\u0170\3")
        buf.write("\2\2\2S\u0172\3\2\2\2U\u0174\3\2\2\2W\u0178\3\2\2\2Y\u017c")
        buf.write("\3\2\2\2[\u017f\3\2\2\2]\u0181\3\2\2\2_\u0184\3\2\2\2")
        buf.write("a\u0187\3\2\2\2c\u0189\3\2\2\2e\u018c\3\2\2\2g\u018e\3")
        buf.write("\2\2\2i\u0191\3\2\2\2k\u0195\3\2\2\2m\u0198\3\2\2\2o\u019a")
        buf.write("\3\2\2\2q\u019c\3\2\2\2s\u019e\3\2\2\2u\u01a0\3\2\2\2")
        buf.write("w\u01a2\3\2\2\2y\u01aa\3\2\2\2{\u01b3\3\2\2\2}\u01b5\3")
        buf.write("\2\2\2\177\u01c0\3\2\2\2\u0081\u01c3\3\2\2\2\u0083\u01d0")
        buf.write("\3\2\2\2\u0085\u0086\7t\2\2\u0086\u0087\7g\2\2\u0087\u0088")
        buf.write("\7c\2\2\u0088\u0089\7f\2\2\u0089\u008a\7P\2\2\u008a\u008b")
        buf.write("\7w\2\2\u008b\u008c\7o\2\2\u008c\u008d\7d\2\2\u008d\u008e")
        buf.write("\7g\2\2\u008e\u008f\7t\2\2\u008f\4\3\2\2\2\u0090\u0091")
        buf.write("\7y\2\2\u0091\u0092\7t\2\2\u0092\u0093\7k\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\u0095\7g\2\2\u0095\u0096\7P\2\2\u0096\u0097")
        buf.write("\7w\2\2\u0097\u0098\7o\2\2\u0098\u0099\7d\2\2\u0099\u009a")
        buf.write("\7g\2\2\u009a\u009b\7t\2\2\u009b\6\3\2\2\2\u009c\u009d")
        buf.write("\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f\7c\2\2\u009f\u00a0")
        buf.write("\7f\2\2\u00a0\u00a1\7D\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\u00a4\7n\2\2\u00a4\b\3\2\2\2\u00a5\u00a6")
        buf.write("\7y\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7D\2\2\u00ab\u00ac")
        buf.write("\7q\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7n\2\2\u00ae\n")
        buf.write("\3\2\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7f\2\2\u00b3\u00b4\7U\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8")
        buf.write("\7p\2\2\u00b8\u00b9\7i\2\2\u00b9\f\3\2\2\2\u00ba\u00bb")
        buf.write("\7y\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7U\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5\16\3\2\2\2\u00c6\u00c8")
        buf.write("\5\21\t\2\u00c7\u00c9\5\27\f\2\u00c8\u00c7\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00cc\5\25\13")
        buf.write("\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce")
        buf.write("\3\2\2\2\u00cd\u00cf\5\23\n\2\u00ce\u00cd\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\20\3\2\2\2\u00d0\u00d2\t\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\22\3\2\2\2\u00d5\u00d7\t\3")
        buf.write("\2\2\u00d6\u00d8\t\4\2\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\5\25\13\2\u00da")
        buf.write("\24\3\2\2\2\u00db\u00dd\t\2\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\26\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\t\5")
        buf.write("\2\2\u00e2\30\3\2\2\2\u00e3\u00e6\5%\23\2\u00e4\u00e6")
        buf.write("\5\'\24\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6")
        buf.write("\32\3\2\2\2\u00e7\u00ed\t\6\2\2\u00e8\u00ec\5\35\17\2")
        buf.write("\u00e9\u00ec\5\37\20\2\u00ea\u00ec\5!\21\2\u00eb\u00e8")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\t")
        buf.write("\6\2\2\u00f1\u00f2\b\16\2\2\u00f2\34\3\2\2\2\u00f3\u00f4")
        buf.write("\n\7\2\2\u00f4\36\3\2\2\2\u00f5\u00f6\7^\2\2\u00f6\u00f7")
        buf.write("\t\b\2\2\u00f7 \3\2\2\2\u00f8\u00f9\7)\2\2\u00f9\u00fa")
        buf.write("\t\6\2\2\u00fa\"\3\2\2\2\u00fb\u00fc\7^\2\2\u00fc\u0100")
        buf.write("\n\b\2\2\u00fd\u00fe\7)\2\2\u00fe\u0100\n\6\2\2\u00ff")
        buf.write("\u00fb\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100$\3\2\2\2\u0101")
        buf.write("\u0102\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104\7w\2\2\u0104")
        buf.write("\u0105\7g\2\2\u0105&\3\2\2\2\u0106\u0107\7h\2\2\u0107")
        buf.write("\u0108\7c\2\2\u0108\u0109\7n\2\2\u0109\u010a\7u\2\2\u010a")
        buf.write("\u010b\7g\2\2\u010b(\3\2\2\2\u010c\u010d\7p\2\2\u010d")
        buf.write("\u010e\7w\2\2\u010e\u010f\7o\2\2\u010f\u0110\7d\2\2\u0110")
        buf.write("\u0111\7g\2\2\u0111\u0112\7t\2\2\u0112*\3\2\2\2\u0113")
        buf.write("\u0114\7d\2\2\u0114\u0115\7q\2\2\u0115\u0116\7q\2\2\u0116")
        buf.write("\u0117\7n\2\2\u0117,\3\2\2\2\u0118\u0119\7u\2\2\u0119")
        buf.write("\u011a\7v\2\2\u011a\u011b\7t\2\2\u011b\u011c\7k\2\2\u011c")
        buf.write("\u011d\7p\2\2\u011d\u011e\7i\2\2\u011e.\3\2\2\2\u011f")
        buf.write("\u0120\7t\2\2\u0120\u0121\7g\2\2\u0121\u0122\7v\2\2\u0122")
        buf.write("\u0123\7w\2\2\u0123\u0124\7t\2\2\u0124\u0125\7p\2\2\u0125")
        buf.write("\60\3\2\2\2\u0126\u0127\7x\2\2\u0127\u0128\7c\2\2\u0128")
        buf.write("\u0129\7t\2\2\u0129\62\3\2\2\2\u012a\u012b\7f\2\2\u012b")
        buf.write("\u012c\7{\2\2\u012c\u012d\7p\2\2\u012d\u012e\7c\2\2\u012e")
        buf.write("\u012f\7o\2\2\u012f\u0130\7k\2\2\u0130\u0131\7e\2\2\u0131")
        buf.write("\64\3\2\2\2\u0132\u0133\7h\2\2\u0133\u0134\7w\2\2\u0134")
        buf.write("\u0135\7p\2\2\u0135\u0136\7e\2\2\u0136\66\3\2\2\2\u0137")
        buf.write("\u0138\7h\2\2\u0138\u0139\7q\2\2\u0139\u013a\7t\2\2\u013a")
        buf.write("8\3\2\2\2\u013b\u013c\7w\2\2\u013c\u013d\7p\2\2\u013d")
        buf.write("\u013e\7v\2\2\u013e\u013f\7k\2\2\u013f\u0140\7n\2\2\u0140")
        buf.write(":\3\2\2\2\u0141\u0142\7d\2\2\u0142\u0143\7{\2\2\u0143")
        buf.write("<\3\2\2\2\u0144\u0145\7d\2\2\u0145\u0146\7t\2\2\u0146")
        buf.write("\u0147\7g\2\2\u0147\u0148\7c\2\2\u0148\u0149\7m\2\2\u0149")
        buf.write(">\3\2\2\2\u014a\u014b\7e\2\2\u014b\u014c\7q\2\2\u014c")
        buf.write("\u014d\7p\2\2\u014d\u014e\7v\2\2\u014e\u014f\7k\2\2\u014f")
        buf.write("\u0150\7p\2\2\u0150\u0151\7w\2\2\u0151\u0152\7g\2\2\u0152")
        buf.write("@\3\2\2\2\u0153\u0154\7k\2\2\u0154\u0155\7h\2\2\u0155")
        buf.write("B\3\2\2\2\u0156\u0157\7g\2\2\u0157\u0158\7n\2\2\u0158")
        buf.write("\u0159\7u\2\2\u0159\u015a\7g\2\2\u015aD\3\2\2\2\u015b")
        buf.write("\u015c\7g\2\2\u015c\u015d\7n\2\2\u015d\u015e\7k\2\2\u015e")
        buf.write("\u015f\7h\2\2\u015fF\3\2\2\2\u0160\u0161\7d\2\2\u0161")
        buf.write("\u0162\7g\2\2\u0162\u0163\7i\2\2\u0163\u0164\7k\2\2\u0164")
        buf.write("\u0165\7p\2\2\u0165H\3\2\2\2\u0166\u0167\7g\2\2\u0167")
        buf.write("\u0168\7p\2\2\u0168\u0169\7f\2\2\u0169J\3\2\2\2\u016a")
        buf.write("\u016b\7-\2\2\u016bL\3\2\2\2\u016c\u016d\7/\2\2\u016d")
        buf.write("N\3\2\2\2\u016e\u016f\7,\2\2\u016fP\3\2\2\2\u0170\u0171")
        buf.write("\7\61\2\2\u0171R\3\2\2\2\u0172\u0173\7\'\2\2\u0173T\3")
        buf.write("\2\2\2\u0174\u0175\7p\2\2\u0175\u0176\7q\2\2\u0176\u0177")
        buf.write("\7v\2\2\u0177V\3\2\2\2\u0178\u0179\7c\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a\u017b\7f\2\2\u017bX\3\2\2\2\u017c\u017d")
        buf.write("\7q\2\2\u017d\u017e\7t\2\2\u017eZ\3\2\2\2\u017f\u0180")
        buf.write("\7?\2\2\u0180\\\3\2\2\2\u0181\u0182\7>\2\2\u0182\u0183")
        buf.write("\7/\2\2\u0183^\3\2\2\2\u0184\u0185\7#\2\2\u0185\u0186")
        buf.write("\7?\2\2\u0186`\3\2\2\2\u0187\u0188\7>\2\2\u0188b\3\2\2")
        buf.write("\2\u0189\u018a\7>\2\2\u018a\u018b\7?\2\2\u018bd\3\2\2")
        buf.write("\2\u018c\u018d\7@\2\2\u018df\3\2\2\2\u018e\u018f\7@\2")
        buf.write("\2\u018f\u0190\7?\2\2\u0190h\3\2\2\2\u0191\u0192\7\60")
        buf.write("\2\2\u0192\u0193\7\60\2\2\u0193\u0194\7\60\2\2\u0194j")
        buf.write("\3\2\2\2\u0195\u0196\7?\2\2\u0196\u0197\7?\2\2\u0197l")
        buf.write("\3\2\2\2\u0198\u0199\7.\2\2\u0199n\3\2\2\2\u019a\u019b")
        buf.write("\7*\2\2\u019bp\3\2\2\2\u019c\u019d\7+\2\2\u019dr\3\2\2")
        buf.write("\2\u019e\u019f\7]\2\2\u019ft\3\2\2\2\u01a0\u01a1\7_\2")
        buf.write("\2\u01a1v\3\2\2\2\u01a2\u01a6\t\t\2\2\u01a3\u01a5\t\n")
        buf.write("\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7x\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a9\u01ab\t\13\2\2\u01aa\u01a9\3\2\2\2\u01ab")
        buf.write("\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01af\b=\3\2\u01afz\3\2\2\2")
        buf.write("\u01b0\u01b4\t\f\2\2\u01b1\u01b2\7\17\2\2\u01b2\u01b4")
        buf.write("\7\f\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("|\3\2\2\2\u01b5\u01b6\7%\2\2\u01b6\u01b7\7%\2\2\u01b7")
        buf.write("\u01bb\3\2\2\2\u01b8\u01ba\n\f\2\2\u01b9\u01b8\3\2\2\2")
        buf.write("\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3")
        buf.write("\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf")
        buf.write("\b?\3\2\u01bf~\3\2\2\2\u01c0\u01c1\13\2\2\2\u01c1\u01c2")
        buf.write("\b@\4\2\u01c2\u0080\3\2\2\2\u01c3\u01c8\7$\2\2\u01c4\u01c7")
        buf.write("\5\35\17\2\u01c5\u01c7\5\37\20\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c8\u01c9\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3")
        buf.write("\2\2\2\u01cb\u01cd\t\r\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce")
        buf.write("\3\2\2\2\u01ce\u01cf\bA\5\2\u01cf\u0082\3\2\2\2\u01d0")
        buf.write("\u01d5\7$\2\2\u01d1\u01d4\5\35\17\2\u01d2\u01d4\5\37\20")
        buf.write("\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01d9\5#\22\2")
        buf.write("\u01d9\u01da\bB\6\2\u01da\u0084\3\2\2\2\26\2\u00c8\u00cb")
        buf.write("\u00ce\u00d3\u00d7\u00de\u00e5\u00eb\u00ed\u00ff\u01a6")
        buf.write("\u01ac\u01b3\u01bb\u01c6\u01c8\u01cc\u01d3\u01d5\7\3\16")
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
            "'readNumber'", "'writeNumber'", "'readBool'", "'writeBool'", 
            "'readString'", "'writeString'", "'true'", "'false'", "'number'", 
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

     


