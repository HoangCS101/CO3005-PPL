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
        buf.write("\u01cb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\5\b\u00ce\n\b\3\b\5\b\u00d1\n\b\3\b\5")
        buf.write("\b\u00d4\n\b\3\t\6\t\u00d7\n\t\r\t\16\t\u00d8\3\n\3\n")
        buf.write("\5\n\u00dd\n\n\3\n\3\n\3\13\7\13\u00e2\n\13\f\13\16\13")
        buf.write("\u00e5\13\13\3\f\3\f\3\r\3\r\5\r\u00eb\n\r\3\16\3\16\3")
        buf.write("\16\3\16\7\16\u00f1\n\16\f\16\16\16\u00f4\13\16\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3")
        buf.write(",\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\7:\u01a2\n:\f:")
        buf.write("\16:\u01a5\13:\3;\6;\u01a8\n;\r;\16;\u01a9\3;\3;\3<\5")
        buf.write("<\u01af\n<\3<\3<\3=\3=\3=\3=\7=\u01b7\n=\f=\16=\u01ba")
        buf.write("\13=\3=\5=\u01bd\n=\3=\3=\5=\u01c1\n=\3=\3=\3>\3>\3>\3")
        buf.write("?\3?\3@\3@\2\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23")
        buf.write("\2\25\2\27\2\31\n\33\13\35\2\37\2!\f#\r%\16\'\17)\20+")
        buf.write("\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32?\33A\34")
        buf.write("C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61")
        buf.write("m\62o\63q\64s\65u\66w\67y8{9}:\177;\3\2\r\3\2\62;\4\2")
        buf.write("GGgg\4\2--//\3\2\60\60\3\2$$\3\2\f\f\t\2))^^ddhhppttv")
        buf.write("v\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\16\"\"\4\2\f\f")
        buf.write("\17\17\2\u01d4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u008e\3\2")
        buf.write("\2\2\7\u009b\3\2\2\2\t\u00a6\3\2\2\2\13\u00b1\3\2\2\2")
        buf.write("\r\u00be\3\2\2\2\17\u00cb\3\2\2\2\21\u00d6\3\2\2\2\23")
        buf.write("\u00da\3\2\2\2\25\u00e3\3\2\2\2\27\u00e6\3\2\2\2\31\u00ea")
        buf.write("\3\2\2\2\33\u00ec\3\2\2\2\35\u00f8\3\2\2\2\37\u00fb\3")
        buf.write("\2\2\2!\u00fe\3\2\2\2#\u0103\3\2\2\2%\u0109\3\2\2\2\'")
        buf.write("\u0110\3\2\2\2)\u0115\3\2\2\2+\u011c\3\2\2\2-\u0123\3")
        buf.write("\2\2\2/\u0127\3\2\2\2\61\u012f\3\2\2\2\63\u0134\3\2\2")
        buf.write("\2\65\u0138\3\2\2\2\67\u013e\3\2\2\29\u0141\3\2\2\2;\u0147")
        buf.write("\3\2\2\2=\u0150\3\2\2\2?\u0153\3\2\2\2A\u0158\3\2\2\2")
        buf.write("C\u015d\3\2\2\2E\u0163\3\2\2\2G\u0167\3\2\2\2I\u0169\3")
        buf.write("\2\2\2K\u016b\3\2\2\2M\u016d\3\2\2\2O\u016f\3\2\2\2Q\u0171")
        buf.write("\3\2\2\2S\u0175\3\2\2\2U\u0179\3\2\2\2W\u017c\3\2\2\2")
        buf.write("Y\u017e\3\2\2\2[\u0181\3\2\2\2]\u0184\3\2\2\2_\u0186\3")
        buf.write("\2\2\2a\u0189\3\2\2\2c\u018b\3\2\2\2e\u018e\3\2\2\2g\u0192")
        buf.write("\3\2\2\2i\u0195\3\2\2\2k\u0197\3\2\2\2m\u0199\3\2\2\2")
        buf.write("o\u019b\3\2\2\2q\u019d\3\2\2\2s\u019f\3\2\2\2u\u01a7\3")
        buf.write("\2\2\2w\u01ae\3\2\2\2y\u01b2\3\2\2\2{\u01c4\3\2\2\2}\u01c7")
        buf.write("\3\2\2\2\177\u01c9\3\2\2\2\u0081\u0082\7t\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\u0084\7c\2\2\u0084\u0085\7f\2\2\u0085\u0086")
        buf.write("\7P\2\2\u0086\u0087\7w\2\2\u0087\u0088\7o\2\2\u0088\u0089")
        buf.write("\7d\2\2\u0089\u008a\7g\2\2\u008a\u008b\7t\2\2\u008b\u008c")
        buf.write("\7*\2\2\u008c\u008d\7+\2\2\u008d\4\3\2\2\2\u008e\u008f")
        buf.write("\7y\2\2\u008f\u0090\7t\2\2\u0090\u0091\7k\2\2\u0091\u0092")
        buf.write("\7v\2\2\u0092\u0093\7g\2\2\u0093\u0094\7P\2\2\u0094\u0095")
        buf.write("\7w\2\2\u0095\u0096\7o\2\2\u0096\u0097\7d\2\2\u0097\u0098")
        buf.write("\7g\2\2\u0098\u0099\7t\2\2\u0099\u009a\7*\2\2\u009a\6")
        buf.write("\3\2\2\2\u009b\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7f\2\2\u009f\u00a0\7D\2\2\u00a0\u00a1")
        buf.write("\7q\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4")
        buf.write("\7*\2\2\u00a4\u00a5\7+\2\2\u00a5\b\3\2\2\2\u00a6\u00a7")
        buf.write("\7y\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7D\2\2\u00ac\u00ad")
        buf.write("\7q\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af\7n\2\2\u00af\u00b0")
        buf.write("\7*\2\2\u00b0\n\3\2\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7f\2\2\u00b5\u00b6")
        buf.write("\7U\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9")
        buf.write("\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7i\2\2\u00bb\u00bc")
        buf.write("\7*\2\2\u00bc\u00bd\7+\2\2\u00bd\f\3\2\2\2\u00be\u00bf")
        buf.write("\7y\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7v\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7U\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7i\2\2\u00c9\u00ca\7*\2\2\u00ca\16")
        buf.write("\3\2\2\2\u00cb\u00cd\5\21\t\2\u00cc\u00ce\5\27\f\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2")
        buf.write("\u00cf\u00d1\5\25\13\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1")
        buf.write("\3\2\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00d4\5\23\n\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\20\3\2\2\2\u00d5")
        buf.write("\u00d7\t\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\22\3\2")
        buf.write("\2\2\u00da\u00dc\t\3\2\2\u00db\u00dd\t\4\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00df\5\25\13\2\u00df\24\3\2\2\2\u00e0\u00e2\t\2\2\2")
        buf.write("\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3")
        buf.write("\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\26\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e6\u00e7\t\5\2\2\u00e7\30\3\2\2\2\u00e8\u00eb")
        buf.write("\5!\21\2\u00e9\u00eb\5#\22\2\u00ea\u00e8\3\2\2\2\u00ea")
        buf.write("\u00e9\3\2\2\2\u00eb\32\3\2\2\2\u00ec\u00f2\t\6\2\2\u00ed")
        buf.write("\u00f1\n\7\2\2\u00ee\u00f1\5\35\17\2\u00ef\u00f1\5\37")
        buf.write("\20\2\u00f0\u00ed\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f5\u00f6\t\6\2\2\u00f6\u00f7\b\16\2\2\u00f7\34\3\2")
        buf.write("\2\2\u00f8\u00f9\7^\2\2\u00f9\u00fa\t\b\2\2\u00fa\36\3")
        buf.write("\2\2\2\u00fb\u00fc\7)\2\2\u00fc\u00fd\t\6\2\2\u00fd \3")
        buf.write("\2\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0102\7g\2\2\u0102\"\3\2\2\2\u0103\u0104")
        buf.write("\7h\2\2\u0104\u0105\7c\2\2\u0105\u0106\7n\2\2\u0106\u0107")
        buf.write("\7u\2\2\u0107\u0108\7g\2\2\u0108$\3\2\2\2\u0109\u010a")
        buf.write("\7p\2\2\u010a\u010b\7w\2\2\u010b\u010c\7o\2\2\u010c\u010d")
        buf.write("\7d\2\2\u010d\u010e\7g\2\2\u010e\u010f\7t\2\2\u010f&\3")
        buf.write("\2\2\2\u0110\u0111\7d\2\2\u0111\u0112\7q\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7n\2\2\u0114(\3\2\2\2\u0115\u0116")
        buf.write("\7u\2\2\u0116\u0117\7v\2\2\u0117\u0118\7t\2\2\u0118\u0119")
        buf.write("\7k\2\2\u0119\u011a\7p\2\2\u011a\u011b\7i\2\2\u011b*\3")
        buf.write("\2\2\2\u011c\u011d\7t\2\2\u011d\u011e\7g\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7w\2\2\u0120\u0121\7t\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122,\3\2\2\2\u0123\u0124\7x\2\2\u0124\u0125")
        buf.write("\7c\2\2\u0125\u0126\7t\2\2\u0126.\3\2\2\2\u0127\u0128")
        buf.write("\7f\2\2\u0128\u0129\7{\2\2\u0129\u012a\7p\2\2\u012a\u012b")
        buf.write("\7c\2\2\u012b\u012c\7o\2\2\u012c\u012d\7k\2\2\u012d\u012e")
        buf.write("\7e\2\2\u012e\60\3\2\2\2\u012f\u0130\7h\2\2\u0130\u0131")
        buf.write("\7w\2\2\u0131\u0132\7p\2\2\u0132\u0133\7e\2\2\u0133\62")
        buf.write("\3\2\2\2\u0134\u0135\7h\2\2\u0135\u0136\7q\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\64\3\2\2\2\u0138\u0139\7w\2\2\u0139\u013a")
        buf.write("\7p\2\2\u013a\u013b\7v\2\2\u013b\u013c\7k\2\2\u013c\u013d")
        buf.write("\7n\2\2\u013d\66\3\2\2\2\u013e\u013f\7d\2\2\u013f\u0140")
        buf.write("\7{\2\2\u01408\3\2\2\2\u0141\u0142\7d\2\2\u0142\u0143")
        buf.write("\7t\2\2\u0143\u0144\7g\2\2\u0144\u0145\7c\2\2\u0145\u0146")
        buf.write("\7m\2\2\u0146:\3\2\2\2\u0147\u0148\7e\2\2\u0148\u0149")
        buf.write("\7q\2\2\u0149\u014a\7p\2\2\u014a\u014b\7v\2\2\u014b\u014c")
        buf.write("\7k\2\2\u014c\u014d\7p\2\2\u014d\u014e\7w\2\2\u014e\u014f")
        buf.write("\7g\2\2\u014f<\3\2\2\2\u0150\u0151\7k\2\2\u0151\u0152")
        buf.write("\7h\2\2\u0152>\3\2\2\2\u0153\u0154\7g\2\2\u0154\u0155")
        buf.write("\7n\2\2\u0155\u0156\7u\2\2\u0156\u0157\7g\2\2\u0157@\3")
        buf.write("\2\2\2\u0158\u0159\7g\2\2\u0159\u015a\7n\2\2\u015a\u015b")
        buf.write("\7k\2\2\u015b\u015c\7h\2\2\u015cB\3\2\2\2\u015d\u015e")
        buf.write("\7d\2\2\u015e\u015f\7g\2\2\u015f\u0160\7i\2\2\u0160\u0161")
        buf.write("\7k\2\2\u0161\u0162\7p\2\2\u0162D\3\2\2\2\u0163\u0164")
        buf.write("\7g\2\2\u0164\u0165\7p\2\2\u0165\u0166\7f\2\2\u0166F\3")
        buf.write("\2\2\2\u0167\u0168\7-\2\2\u0168H\3\2\2\2\u0169\u016a\7")
        buf.write("/\2\2\u016aJ\3\2\2\2\u016b\u016c\7,\2\2\u016cL\3\2\2\2")
        buf.write("\u016d\u016e\7\61\2\2\u016eN\3\2\2\2\u016f\u0170\7\'\2")
        buf.write("\2\u0170P\3\2\2\2\u0171\u0172\7p\2\2\u0172\u0173\7q\2")
        buf.write("\2\u0173\u0174\7v\2\2\u0174R\3\2\2\2\u0175\u0176\7c\2")
        buf.write("\2\u0176\u0177\7p\2\2\u0177\u0178\7f\2\2\u0178T\3\2\2")
        buf.write("\2\u0179\u017a\7q\2\2\u017a\u017b\7t\2\2\u017bV\3\2\2")
        buf.write("\2\u017c\u017d\7?\2\2\u017dX\3\2\2\2\u017e\u017f\7>\2")
        buf.write("\2\u017f\u0180\7/\2\2\u0180Z\3\2\2\2\u0181\u0182\7#\2")
        buf.write("\2\u0182\u0183\7?\2\2\u0183\\\3\2\2\2\u0184\u0185\7>\2")
        buf.write("\2\u0185^\3\2\2\2\u0186\u0187\7>\2\2\u0187\u0188\7?\2")
        buf.write("\2\u0188`\3\2\2\2\u0189\u018a\7@\2\2\u018ab\3\2\2\2\u018b")
        buf.write("\u018c\7@\2\2\u018c\u018d\7?\2\2\u018dd\3\2\2\2\u018e")
        buf.write("\u018f\7\60\2\2\u018f\u0190\7\60\2\2\u0190\u0191\7\60")
        buf.write("\2\2\u0191f\3\2\2\2\u0192\u0193\7?\2\2\u0193\u0194\7?")
        buf.write("\2\2\u0194h\3\2\2\2\u0195\u0196\7.\2\2\u0196j\3\2\2\2")
        buf.write("\u0197\u0198\7*\2\2\u0198l\3\2\2\2\u0199\u019a\7+\2\2")
        buf.write("\u019an\3\2\2\2\u019b\u019c\7]\2\2\u019cp\3\2\2\2\u019d")
        buf.write("\u019e\7_\2\2\u019er\3\2\2\2\u019f\u01a3\t\t\2\2\u01a0")
        buf.write("\u01a2\t\n\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4t\3\2\2")
        buf.write("\2\u01a5\u01a3\3\2\2\2\u01a6\u01a8\t\13\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\b;\3\2")
        buf.write("\u01acv\3\2\2\2\u01ad\u01af\7\17\2\2\u01ae\u01ad\3\2\2")
        buf.write("\2\u01ae\u01af\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1")
        buf.write("\7\f\2\2\u01b1x\3\2\2\2\u01b2\u01b3\7%\2\2\u01b3\u01b4")
        buf.write("\7%\2\2\u01b4\u01b8\3\2\2\2\u01b5\u01b7\n\f\2\2\u01b6")
        buf.write("\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01c0\3\2\2\2\u01ba\u01b8\3")
        buf.write("\2\2\2\u01bb\u01bd\7\17\2\2\u01bc\u01bb\3\2\2\2\u01bc")
        buf.write("\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c1\7\f\2\2")
        buf.write("\u01bf\u01c1\7\2\2\3\u01c0\u01bc\3\2\2\2\u01c0\u01bf\3")
        buf.write("\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\b=\3\2\u01c3z\3")
        buf.write("\2\2\2\u01c4\u01c5\13\2\2\2\u01c5\u01c6\b>\4\2\u01c6|")
        buf.write("\3\2\2\2\u01c7\u01c8\13\2\2\2\u01c8~\3\2\2\2\u01c9\u01ca")
        buf.write("\13\2\2\2\u01ca\u0080\3\2\2\2\22\2\u00cd\u00d0\u00d3\u00d8")
        buf.write("\u00dc\u00e3\u00ea\u00f0\u00f2\u01a3\u01a9\u01ae\u01b8")
        buf.write("\u01bc\u01c0\5\3\16\2\b\2\2\3>\3")
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
                  "STRING_LITERAL", "ESCAPE_SEQUENCE", "DOUBQ", "TRUE", 
                  "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
                  "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", 
                  "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", "ASSIGN", 
                  "ARROW", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                  "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "ELLIPSIS", "EQUAL", 
                  "COMMA", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "IDENTIFIER", 
                  "WS", "NEWLINE", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            content = str(self.text)
            self.text = content[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


