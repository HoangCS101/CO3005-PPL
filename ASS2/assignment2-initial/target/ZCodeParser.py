# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u01b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\6\2f\n\2\r\2\16")
        buf.write("\2g\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3x\n\3\3\3\6\3{\n\3\r\3\16\3|\3\4\3\4\3\4\5\4")
        buf.write("\u0082\n\4\3\4\3\4\5\4\u0086\n\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\5\6\u0091\n\6\3\7\3\7\3\7\3\7\5\7\u0097")
        buf.write("\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u00a1\n\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\5\f\u00b0\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b8\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\7\25\u00e0\n\25\f\25\16")
        buf.write("\25\u00e3\13\25\3\26\3\26\3\26\3\26\7\26\u00e9\n\26\f")
        buf.write("\26\16\26\u00ec\13\26\3\26\3\26\3\27\3\27\5\27\u00f2\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\7\31\u00fb\n\31")
        buf.write("\f\31\16\31\u00fe\13\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\7\32\u0107\n\32\f\32\16\32\u010a\13\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u0110\n\32\3\33\3\33\3\33\5\33\u0115\n")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u011e\n\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u0126\n\35\3\36\3")
        buf.write("\36\3\37\3\37\3 \3 \5 \u012e\n \3!\3!\5!\u0132\n!\3!\7")
        buf.write("!\u0135\n!\f!\16!\u0138\13!\3!\5!\u013b\n!\3!\3!\5!\u013f")
        buf.write("\n!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0147\n\"\3#\3#\5#\u014b")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u0152\n$\3%\3%\3%\3%\5%\u0158\n")
        buf.write("%\3&\3&\3&\3&\3&\5&\u015f\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0166")
        buf.write("\n\'\3(\3(\3(\3(\3(\3(\7(\u016e\n(\f(\16(\u0171\13(\3")
        buf.write(")\3)\3)\3)\3)\3)\7)\u0179\n)\f)\16)\u017c\13)\3*\3*\3")
        buf.write("*\3*\3*\3*\7*\u0184\n*\f*\16*\u0187\13*\3+\3+\3+\5+\u018c")
        buf.write("\n+\3,\3,\3,\5,\u0191\n,\3-\3-\5-\u0195\n-\3-\3-\3-\3")
        buf.write("-\3-\5-\u019c\n-\3.\3.\3.\3.\3.\5.\u01a3\n.\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\5/\u01ac\n/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\u0136\5NPR\63\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\b\3")
        buf.write("\2%&\3\2\37 \3\2!#\5\2\'\')-//\3\2\16\20\3\2\t\13\2\u01bf")
        buf.write("\2e\3\2\2\2\4w\3\2\2\2\6~\3\2\2\2\b\u0087\3\2\2\2\n\u008c")
        buf.write("\3\2\2\2\f\u0092\3\2\2\2\16\u009a\3\2\2\2\20\u00a0\3\2")
        buf.write("\2\2\22\u00a7\3\2\2\2\24\u00a9\3\2\2\2\26\u00af\3\2\2")
        buf.write("\2\30\u00b7\3\2\2\2\32\u00b9\3\2\2\2\34\u00bd\3\2\2\2")
        buf.write("\36\u00c2\3\2\2\2 \u00c6\3\2\2\2\"\u00cb\3\2\2\2$\u00cf")
        buf.write("\3\2\2\2&\u00d4\3\2\2\2(\u00dc\3\2\2\2*\u00e4\3\2\2\2")
        buf.write(",\u00f1\3\2\2\2.\u00f3\3\2\2\2\60\u00f7\3\2\2\2\62\u010f")
        buf.write("\3\2\2\2\64\u0114\3\2\2\2\66\u0116\3\2\2\28\u0125\3\2")
        buf.write("\2\2:\u0127\3\2\2\2<\u0129\3\2\2\2>\u012b\3\2\2\2@\u012f")
        buf.write("\3\2\2\2B\u0146\3\2\2\2D\u014a\3\2\2\2F\u0151\3\2\2\2")
        buf.write("H\u0157\3\2\2\2J\u015e\3\2\2\2L\u0165\3\2\2\2N\u0167\3")
        buf.write("\2\2\2P\u0172\3\2\2\2R\u017d\3\2\2\2T\u018b\3\2\2\2V\u0190")
        buf.write("\3\2\2\2X\u019b\3\2\2\2Z\u01a2\3\2\2\2\\\u01ab\3\2\2\2")
        buf.write("^\u01ad\3\2\2\2`\u01af\3\2\2\2b\u01b1\3\2\2\2df\5\4\3")
        buf.write("\2ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2i")
        buf.write("j\7\2\2\3j\3\3\2\2\2kx\5\6\4\2lx\5\b\5\2mx\5\n\6\2nx\5")
        buf.write("\f\7\2ox\5\30\r\2px\5B\"\2qx\5&\24\2rx\5.\30\2sx\5\60")
        buf.write("\31\2tx\5\66\34\2ux\58\35\2vx\5J&\2wk\3\2\2\2wl\3\2\2")
        buf.write("\2wm\3\2\2\2wn\3\2\2\2wo\3\2\2\2wp\3\2\2\2wq\3\2\2\2w")
        buf.write("r\3\2\2\2ws\3\2\2\2wt\3\2\2\2wu\3\2\2\2wv\3\2\2\2xz\3")
        buf.write("\2\2\2y{\7\67\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2")
        buf.write("\2\2}\5\3\2\2\2~\u0081\5`\61\2\177\u0082\7\65\2\2\u0080")
        buf.write("\u0082\5X-\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\u0085\3\2\2\2\u0083\u0084\7(\2\2\u0084\u0086\5J&\2\u0085")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\7\3\2\2\2\u0087")
        buf.write("\u0088\7\22\2\2\u0088\u0089\7\65\2\2\u0089\u008a\7(\2")
        buf.write("\2\u008a\u008b\5J&\2\u008b\t\3\2\2\2\u008c\u008d\7\23")
        buf.write("\2\2\u008d\u0090\7\65\2\2\u008e\u008f\7(\2\2\u008f\u0091")
        buf.write("\5J&\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\13")
        buf.write("\3\2\2\2\u0092\u0093\7\24\2\2\u0093\u0094\7\65\2\2\u0094")
        buf.write("\u0096\5\16\b\2\u0095\u0097\7\67\2\2\u0096\u0095\3\2\2")
        buf.write("\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\5\26\f\2\u0099\r\3\2\2\2\u009a\u009b\7\61\2\2\u009b\u009c")
        buf.write("\5\20\t\2\u009c\u009d\7\62\2\2\u009d\17\3\2\2\2\u009e")
        buf.write("\u00a1\5\22\n\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2")
        buf.write("\2\u00a0\u009f\3\2\2\2\u00a1\21\3\2\2\2\u00a2\u00a3\5")
        buf.write("\24\13\2\u00a3\u00a4\7\60\2\2\u00a4\u00a5\5\22\n\2\u00a5")
        buf.write("\u00a8\3\2\2\2\u00a6\u00a8\5\24\13\2\u00a7\u00a2\3\2\2")
        buf.write("\2\u00a7\u00a6\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00aa\5")
        buf.write("`\61\2\u00aa\u00ab\5J&\2\u00ab\25\3\2\2\2\u00ac\u00b0")
        buf.write("\5> \2\u00ad\u00b0\5@!\2\u00ae\u00b0\3\2\2\2\u00af\u00ac")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2\u00b0")
        buf.write("\27\3\2\2\2\u00b1\u00b8\5\32\16\2\u00b2\u00b8\5\34\17")
        buf.write("\2\u00b3\u00b8\5\36\20\2\u00b4\u00b8\5 \21\2\u00b5\u00b8")
        buf.write("\5\"\22\2\u00b6\u00b8\5$\23\2\u00b7\u00b1\3\2\2\2\u00b7")
        buf.write("\u00b2\3\2\2\2\u00b7\u00b3\3\2\2\2\u00b7\u00b4\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\31\3\2")
        buf.write("\2\2\u00b9\u00ba\7\3\2\2\u00ba\u00bb\7\61\2\2\u00bb\u00bc")
        buf.write("\7\62\2\2\u00bc\33\3\2\2\2\u00bd\u00be\7\4\2\2\u00be\u00bf")
        buf.write("\7\61\2\2\u00bf\u00c0\5J&\2\u00c0\u00c1\7\62\2\2\u00c1")
        buf.write("\35\3\2\2\2\u00c2\u00c3\7\5\2\2\u00c3\u00c4\7\61\2\2\u00c4")
        buf.write("\u00c5\7\62\2\2\u00c5\37\3\2\2\2\u00c6\u00c7\7\6\2\2\u00c7")
        buf.write("\u00c8\7\61\2\2\u00c8\u00c9\5J&\2\u00c9\u00ca\7\62\2\2")
        buf.write("\u00ca!\3\2\2\2\u00cb\u00cc\7\7\2\2\u00cc\u00cd\7\61\2")
        buf.write("\2\u00cd\u00ce\7\62\2\2\u00ce#\3\2\2\2\u00cf\u00d0\7\b")
        buf.write("\2\2\u00d0\u00d1\7\61\2\2\u00d1\u00d2\5J&\2\u00d2\u00d3")
        buf.write("\7\62\2\2\u00d3%\3\2\2\2\u00d4\u00d5\5`\61\2\u00d5\u00d6")
        buf.write("\7\65\2\2\u00d6\u00d7\7\63\2\2\u00d7\u00d8\5(\25\2\u00d8")
        buf.write("\u00d9\7\64\2\2\u00d9\u00da\7(\2\2\u00da\u00db\5*\26\2")
        buf.write("\u00db\'\3\2\2\2\u00dc\u00e1\7\t\2\2\u00dd\u00de\7\60")
        buf.write("\2\2\u00de\u00e0\7\t\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e3")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write(")\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\7\63\2\2\u00e5")
        buf.write("\u00ea\5,\27\2\u00e6\u00e7\7\60\2\2\u00e7\u00e9\5,\27")
        buf.write("\2\u00e8\u00e6\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8")
        buf.write("\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ed\u00ee\7\64\2\2\u00ee+\3\2\2\2\u00ef")
        buf.write("\u00f2\5J&\2\u00f0\u00f2\5*\26\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f2-\3\2\2\2\u00f3\u00f4\5J&\2\u00f4")
        buf.write("\u00f5\7(\2\2\u00f5\u00f6\5J&\2\u00f6/\3\2\2\2\u00f7\u00f8")
        buf.write("\7\32\2\2\u00f8\u00fc\5J&\2\u00f9\u00fb\7\67\2\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3")
        buf.write("\2\2\2\u00ff\u0100\5\4\3\2\u0100\u0101\5\62\32\2\u0101")
        buf.write("\u0102\5\64\33\2\u0102\61\3\2\2\2\u0103\u0104\7\34\2\2")
        buf.write("\u0104\u0108\5J&\2\u0105\u0107\7\67\2\2\u0106\u0105\3")
        buf.write("\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0108\3\2\2\2\u010b")
        buf.write("\u010c\5\4\3\2\u010c\u010d\5\62\32\2\u010d\u0110\3\2\2")
        buf.write("\2\u010e\u0110\3\2\2\2\u010f\u0103\3\2\2\2\u010f\u010e")
        buf.write("\3\2\2\2\u0110\63\3\2\2\2\u0111\u0112\7\33\2\2\u0112\u0115")
        buf.write("\5\4\3\2\u0113\u0115\3\2\2\2\u0114\u0111\3\2\2\2\u0114")
        buf.write("\u0113\3\2\2\2\u0115\65\3\2\2\2\u0116\u0117\7\25\2\2\u0117")
        buf.write("\u0118\7\65\2\2\u0118\u0119\7\26\2\2\u0119\u011a\5J&\2")
        buf.write("\u011a\u011b\7\27\2\2\u011b\u011d\5J&\2\u011c\u011e\7")
        buf.write("\67\2\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write("\u011f\3\2\2\2\u011f\u0120\5\4\3\2\u0120\67\3\2\2\2\u0121")
        buf.write("\u0126\5:\36\2\u0122\u0126\5<\37\2\u0123\u0126\5> \2\u0124")
        buf.write("\u0126\5@!\2\u0125\u0121\3\2\2\2\u0125\u0122\3\2\2\2\u0125")
        buf.write("\u0123\3\2\2\2\u0125\u0124\3\2\2\2\u01269\3\2\2\2\u0127")
        buf.write("\u0128\7\30\2\2\u0128;\3\2\2\2\u0129\u012a\7\31\2\2\u012a")
        buf.write("=\3\2\2\2\u012b\u012d\7\21\2\2\u012c\u012e\5J&\2\u012d")
        buf.write("\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e?\3\2\2\2\u012f")
        buf.write("\u0131\7\35\2\2\u0130\u0132\7\67\2\2\u0131\u0130\3\2\2")
        buf.write("\2\u0131\u0132\3\2\2\2\u0132\u0136\3\2\2\2\u0133\u0135")
        buf.write("\5\4\3\2\u0134\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u013a\3\2\2\2")
        buf.write("\u0138\u0136\3\2\2\2\u0139\u013b\7\67\2\2\u013a\u0139")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c")
        buf.write("\u013e\7\36\2\2\u013d\u013f\7\67\2\2\u013e\u013d\3\2\2")
        buf.write("\2\u013e\u013f\3\2\2\2\u013fA\3\2\2\2\u0140\u0141\7\65")
        buf.write("\2\2\u0141\u0142\7\61\2\2\u0142\u0143\5D#\2\u0143\u0144")
        buf.write("\7\62\2\2\u0144\u0147\3\2\2\2\u0145\u0147\5\30\r\2\u0146")
        buf.write("\u0140\3\2\2\2\u0146\u0145\3\2\2\2\u0147C\3\2\2\2\u0148")
        buf.write("\u014b\5F$\2\u0149\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write("\u0149\3\2\2\2\u014bE\3\2\2\2\u014c\u014d\5H%\2\u014d")
        buf.write("\u014e\7\60\2\2\u014e\u014f\5F$\2\u014f\u0152\3\2\2\2")
        buf.write("\u0150\u0152\5H%\2\u0151\u014c\3\2\2\2\u0151\u0150\3\2")
        buf.write("\2\2\u0152G\3\2\2\2\u0153\u0158\5b\62\2\u0154\u0158\5")
        buf.write("B\"\2\u0155\u0158\7\65\2\2\u0156\u0158\5J&\2\u0157\u0153")
        buf.write("\3\2\2\2\u0157\u0154\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158I\3\2\2\2\u0159\u015a\5L\'\2\u015a")
        buf.write("\u015b\7.\2\2\u015b\u015c\5L\'\2\u015c\u015f\3\2\2\2\u015d")
        buf.write("\u015f\5L\'\2\u015e\u0159\3\2\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015fK\3\2\2\2\u0160\u0161\5N(\2\u0161\u0162\5^\60\2")
        buf.write("\u0162\u0163\5N(\2\u0163\u0166\3\2\2\2\u0164\u0166\5N")
        buf.write("(\2\u0165\u0160\3\2\2\2\u0165\u0164\3\2\2\2\u0166M\3\2")
        buf.write("\2\2\u0167\u0168\b(\1\2\u0168\u0169\5P)\2\u0169\u016f")
        buf.write("\3\2\2\2\u016a\u016b\f\4\2\2\u016b\u016c\t\2\2\2\u016c")
        buf.write("\u016e\5P)\2\u016d\u016a\3\2\2\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170O\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0172\u0173\b)\1\2\u0173\u0174\5R*\2\u0174")
        buf.write("\u017a\3\2\2\2\u0175\u0176\f\4\2\2\u0176\u0177\t\3\2\2")
        buf.write("\u0177\u0179\5R*\2\u0178\u0175\3\2\2\2\u0179\u017c\3\2")
        buf.write("\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017bQ\3")
        buf.write("\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\b*\1\2\u017e\u017f")
        buf.write("\5T+\2\u017f\u0185\3\2\2\2\u0180\u0181\f\4\2\2\u0181\u0182")
        buf.write("\t\4\2\2\u0182\u0184\5T+\2\u0183\u0180\3\2\2\2\u0184\u0187")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("S\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u0189\7$\2\2\u0189")
        buf.write("\u018c\5T+\2\u018a\u018c\5V,\2\u018b\u0188\3\2\2\2\u018b")
        buf.write("\u018a\3\2\2\2\u018cU\3\2\2\2\u018d\u018e\7 \2\2\u018e")
        buf.write("\u0191\5V,\2\u018f\u0191\5X-\2\u0190\u018d\3\2\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191W\3\2\2\2\u0192\u0195\7\65\2\2\u0193")
        buf.write("\u0195\5B\"\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2")
        buf.write("\u0195\u0196\3\2\2\2\u0196\u0197\7\63\2\2\u0197\u0198")
        buf.write("\5Z.\2\u0198\u0199\7\64\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u019c\5\\/\2\u019b\u0194\3\2\2\2\u019b\u019a\3\2\2\2")
        buf.write("\u019cY\3\2\2\2\u019d\u019e\5J&\2\u019e\u019f\7\60\2\2")
        buf.write("\u019f\u01a0\5Z.\2\u01a0\u01a3\3\2\2\2\u01a1\u01a3\5J")
        buf.write("&\2\u01a2\u019d\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3[\3\2")
        buf.write("\2\2\u01a4\u01ac\5b\62\2\u01a5\u01a6\7\61\2\2\u01a6\u01a7")
        buf.write("\5J&\2\u01a7\u01a8\7\62\2\2\u01a8\u01ac\3\2\2\2\u01a9")
        buf.write("\u01ac\5B\"\2\u01aa\u01ac\7\65\2\2\u01ab\u01a4\3\2\2\2")
        buf.write("\u01ab\u01a5\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ab\u01aa\3")
        buf.write("\2\2\2\u01ac]\3\2\2\2\u01ad\u01ae\t\5\2\2\u01ae_\3\2\2")
        buf.write("\2\u01af\u01b0\t\6\2\2\u01b0a\3\2\2\2\u01b1\u01b2\t\7")
        buf.write("\2\2\u01b2c\3\2\2\2*gw|\u0081\u0085\u0090\u0096\u00a0")
        buf.write("\u00a7\u00af\u00b7\u00e1\u00ea\u00f1\u00fc\u0108\u010f")
        buf.write("\u0114\u011d\u0125\u012d\u0131\u0136\u013a\u013e\u0146")
        buf.write("\u014a\u0151\u0157\u015e\u0165\u016f\u017a\u0185\u018b")
        buf.write("\u0190\u0194\u019b\u01a2\u01ab")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'writeBool'", "'readString'", "'writeString'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "','", "'('", "')'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER_LITERAL", 
                      "BOOL_LITERAL", "STRING_LITERAL", "TRUE", "FALSE", 
                      "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "PLUS", "MINUS", 
                      "MULTIPLY", "DIVIDE", "MODULO", "NOT", "AND", "OR", 
                      "ASSIGN", "ARROW", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "ELLIPSIS", 
                      "EQUAL", "COMMA", "LPAREN", "RPAREN", "LBRACKET", 
                      "RBRACKET", "IDENTIFIER", "WS", "NEWLINE", "COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_vardecl = 2
    RULE_im_vardecl = 3
    RULE_im_dydecl = 4
    RULE_funcdecl = 5
    RULE_arg = 6
    RULE_arglist = 7
    RULE_argprime = 8
    RULE_argment = 9
    RULE_funcend = 10
    RULE_builtin = 11
    RULE_readnum = 12
    RULE_writenum = 13
    RULE_readbool = 14
    RULE_writebool = 15
    RULE_readstr = 16
    RULE_writestr = 17
    RULE_arraydecl = 18
    RULE_arraydim = 19
    RULE_array = 20
    RULE_arrayelement = 21
    RULE_assignstmt = 22
    RULE_ifstmt = 23
    RULE_elifstmt = 24
    RULE_elsestmt = 25
    RULE_forstmt = 26
    RULE_otherstmt = 27
    RULE_breakstmt = 28
    RULE_continuestmt = 29
    RULE_returnstmt = 30
    RULE_blockstmt = 31
    RULE_funccall = 32
    RULE_paramlist = 33
    RULE_paramprime = 34
    RULE_param = 35
    RULE_expr = 36
    RULE_expr1 = 37
    RULE_expr2 = 38
    RULE_expr3 = 39
    RULE_expr4 = 40
    RULE_expr5 = 41
    RULE_expr6 = 42
    RULE_expr7 = 43
    RULE_expr8 = 44
    RULE_expr9 = 45
    RULE_relationals = 46
    RULE_typ = 47
    RULE_literals = 48

    ruleNames =  [ "program", "stmt", "vardecl", "im_vardecl", "im_dydecl", 
                   "funcdecl", "arg", "arglist", "argprime", "argment", 
                   "funcend", "builtin", "readnum", "writenum", "readbool", 
                   "writebool", "readstr", "writestr", "arraydecl", "arraydim", 
                   "array", "arrayelement", "assignstmt", "ifstmt", "elifstmt", 
                   "elsestmt", "forstmt", "otherstmt", "breakstmt", "continuestmt", 
                   "returnstmt", "blockstmt", "funccall", "paramlist", "paramprime", 
                   "param", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "relationals", 
                   "typ", "literals" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMBER_LITERAL=7
    BOOL_LITERAL=8
    STRING_LITERAL=9
    TRUE=10
    FALSE=11
    NUMBER=12
    BOOL=13
    STRING=14
    RETURN=15
    VAR=16
    DYNAMIC=17
    FUNC=18
    FOR=19
    UNTIL=20
    BY=21
    BREAK=22
    CONTINUE=23
    IF=24
    ELSE=25
    ELIF=26
    BEGIN=27
    END=28
    PLUS=29
    MINUS=30
    MULTIPLY=31
    DIVIDE=32
    MODULO=33
    NOT=34
    AND=35
    OR=36
    ASSIGN=37
    ARROW=38
    NOT_EQUAL=39
    LESS_THAN=40
    LESS_THAN_OR_EQUAL=41
    GREATER_THAN=42
    GREATER_THAN_OR_EQUAL=43
    ELLIPSIS=44
    EQUAL=45
    COMMA=46
    LPAREN=47
    RPAREN=48
    LBRACKET=49
    RBRACKET=50
    IDENTIFIER=51
    WS=52
    NEWLINE=53
    COMMENT=54
    ERROR_CHAR=55
    UNCLOSE_STRING=56
    ILLEGAL_ESCAPE=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.stmt()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOL_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDENTIFIER))) != 0)):
                    break

            self.state = 103
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def im_vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.Im_vardeclContext,0)


        def im_dydecl(self):
            return self.getTypedRuleContext(ZCodeParser.Im_dydeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def builtin(self):
            return self.getTypedRuleContext(ZCodeParser.BuiltinContext,0)


        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def otherstmt(self):
            return self.getTypedRuleContext(ZCodeParser.OtherstmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 105
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 106
                self.im_vardecl()
                pass

            elif la_ == 3:
                self.state = 107
                self.im_dydecl()
                pass

            elif la_ == 4:
                self.state = 108
                self.funcdecl()
                pass

            elif la_ == 5:
                self.state = 109
                self.builtin()
                pass

            elif la_ == 6:
                self.state = 110
                self.funccall()
                pass

            elif la_ == 7:
                self.state = 111
                self.arraydecl()
                pass

            elif la_ == 8:
                self.state = 112
                self.assignstmt()
                pass

            elif la_ == 9:
                self.state = 113
                self.ifstmt()
                pass

            elif la_ == 10:
                self.state = 114
                self.forstmt()
                pass

            elif la_ == 11:
                self.state = 115
                self.otherstmt()
                pass

            elif la_ == 12:
                self.state = 116
                self.expr()
                pass


            self.state = 120 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 119
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 122 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.typ()
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 125
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 126
                self.expr7()
                pass


            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 129
                self.match(ZCodeParser.ARROW)
                self.state = 130
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Im_vardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_im_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIm_vardecl" ):
                return visitor.visitIm_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def im_vardecl(self):

        localctx = ZCodeParser.Im_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_im_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(ZCodeParser.VAR)
            self.state = 134
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 135
            self.match(ZCodeParser.ARROW)
            self.state = 136
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Im_dydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_im_dydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIm_dydecl" ):
                return visitor.visitIm_dydecl(self)
            else:
                return visitor.visitChildren(self)




    def im_dydecl(self):

        localctx = ZCodeParser.Im_dydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_im_dydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ZCodeParser.DYNAMIC)
            self.state = 139
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 140
                self.match(ZCodeParser.ARROW)
                self.state = 141
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def funcend(self):
            return self.getTypedRuleContext(ZCodeParser.FuncendContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.FUNC)
            self.state = 145
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 146
            self.arg()
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 147
                self.match(ZCodeParser.NEWLINE)


            self.state = 150
            self.funcend()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def arglist(self):
            return self.getTypedRuleContext(ZCodeParser.ArglistContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = ZCodeParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(ZCodeParser.LPAREN)
            self.state = 153
            self.arglist()
            self.state = 154
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arglist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




    def arglist(self):

        localctx = ZCodeParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arglist)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.argprime()
                pass
            elif token in [ZCodeParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argment(self):
            return self.getTypedRuleContext(ZCodeParser.ArgmentContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argprime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgprime" ):
                return visitor.visitArgprime(self)
            else:
                return visitor.visitChildren(self)




    def argprime(self):

        localctx = ZCodeParser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argprime)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.argment()
                self.state = 161
                self.match(ZCodeParser.COMMA)
                self.state = 162
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.argment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgment" ):
                return visitor.visitArgment(self)
            else:
                return visitor.visitChildren(self)




    def argment(self):

        localctx = ZCodeParser.ArgmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.typ()
            self.state = 168
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcend

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncend" ):
                return visitor.visitFuncend(self)
            else:
                return visitor.visitChildren(self)




    def funcend(self):

        localctx = ZCodeParser.FuncendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcend)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.blockstmt()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuiltinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readnum(self):
            return self.getTypedRuleContext(ZCodeParser.ReadnumContext,0)


        def writenum(self):
            return self.getTypedRuleContext(ZCodeParser.WritenumContext,0)


        def readbool(self):
            return self.getTypedRuleContext(ZCodeParser.ReadboolContext,0)


        def writebool(self):
            return self.getTypedRuleContext(ZCodeParser.WriteboolContext,0)


        def readstr(self):
            return self.getTypedRuleContext(ZCodeParser.ReadstrContext,0)


        def writestr(self):
            return self.getTypedRuleContext(ZCodeParser.WritestrContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_builtin

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltin" ):
                return visitor.visitBuiltin(self)
            else:
                return visitor.visitChildren(self)




    def builtin(self):

        localctx = ZCodeParser.BuiltinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_builtin)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.readnum()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.writenum()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.readbool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.writebool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
                self.readstr()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 180
                self.writestr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadnumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readnum

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadnum" ):
                return visitor.visitReadnum(self)
            else:
                return visitor.visitChildren(self)




    def readnum(self):

        localctx = ZCodeParser.ReadnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_readnum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(ZCodeParser.T__0)
            self.state = 184
            self.match(ZCodeParser.LPAREN)
            self.state = 185
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WritenumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writenum

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWritenum" ):
                return visitor.visitWritenum(self)
            else:
                return visitor.visitChildren(self)




    def writenum(self):

        localctx = ZCodeParser.WritenumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_writenum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.T__1)
            self.state = 188
            self.match(ZCodeParser.LPAREN)
            self.state = 189
            self.expr()
            self.state = 190
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readbool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadbool" ):
                return visitor.visitReadbool(self)
            else:
                return visitor.visitChildren(self)




    def readbool(self):

        localctx = ZCodeParser.ReadboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_readbool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(ZCodeParser.T__2)
            self.state = 193
            self.match(ZCodeParser.LPAREN)
            self.state = 194
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writebool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWritebool" ):
                return visitor.visitWritebool(self)
            else:
                return visitor.visitChildren(self)




    def writebool(self):

        localctx = ZCodeParser.WriteboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_writebool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(ZCodeParser.T__3)
            self.state = 197
            self.match(ZCodeParser.LPAREN)
            self.state = 198
            self.expr()
            self.state = 199
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadstr" ):
                return visitor.visitReadstr(self)
            else:
                return visitor.visitChildren(self)




    def readstr(self):

        localctx = ZCodeParser.ReadstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_readstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(ZCodeParser.T__4)
            self.state = 202
            self.match(ZCodeParser.LPAREN)
            self.state = 203
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WritestrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writestr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWritestr" ):
                return visitor.visitWritestr(self)
            else:
                return visitor.visitChildren(self)




    def writestr(self):

        localctx = ZCodeParser.WritestrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_writestr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(ZCodeParser.T__5)
            self.state = 206
            self.match(ZCodeParser.LPAREN)
            self.state = 207
            self.expr()
            self.state = 208
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def arraydim(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydimContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.typ()
            self.state = 211
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 212
            self.match(ZCodeParser.LBRACKET)
            self.state = 213
            self.arraydim()
            self.state = 214
            self.match(ZCodeParser.RBRACKET)
            self.state = 215
            self.match(ZCodeParser.ARROW)
            self.state = 216
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NUMBER_LITERAL)
            else:
                return self.getToken(ZCodeParser.NUMBER_LITERAL, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydim

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydim" ):
                return visitor.visitArraydim(self)
            else:
                return visitor.visitChildren(self)




    def arraydim(self):

        localctx = ZCodeParser.ArraydimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arraydim)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ZCodeParser.NUMBER_LITERAL)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.COMMA:
                self.state = 219
                self.match(ZCodeParser.COMMA)
                self.state = 220
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def arrayelement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ArrayelementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ArrayelementContext,i)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ZCodeParser.LBRACKET)
            self.state = 227
            self.arrayelement()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.COMMA:
                self.state = 228
                self.match(ZCodeParser.COMMA)
                self.state = 229
                self.arrayelement()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayelementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayelement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayelement" ):
                return visitor.visitArrayelement(self)
            else:
                return visitor.visitChildren(self)




    def arrayelement(self):

        localctx = ZCodeParser.ArrayelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrayelement)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.expr()
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def ARROW(self):
            return self.getToken(ZCodeParser.ARROW, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.expr()
            self.state = 242
            self.match(ZCodeParser.ARROW)
            self.state = 243
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElsestmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ZCodeParser.IF)
            self.state = 246
            self.expr()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 247
                self.match(ZCodeParser.NEWLINE)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 253
            self.stmt()
            self.state = 254
            self.elifstmt()
            self.state = 255
            self.elsestmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmt" ):
                return visitor.visitElifstmt(self)
            else:
                return visitor.visitChildren(self)




    def elifstmt(self):

        localctx = ZCodeParser.ElifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elifstmt)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(ZCodeParser.ELIF)
                self.state = 258
                self.expr()
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 259
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 264
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 265
                self.stmt()
                self.state = 266
                self.elifstmt()
                pass
            elif token in [ZCodeParser.ELSE, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = ZCodeParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elsestmt)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.ELSE)
                self.state = 272
                self.stmt()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.FOR)
            self.state = 277
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 278
            self.match(ZCodeParser.UNTIL)
            self.state = 279
            self.expr()
            self.state = 280
            self.match(ZCodeParser.BY)
            self.state = 281
            self.expr()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 282
                self.match(ZCodeParser.NEWLINE)


            self.state = 285
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_otherstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherstmt" ):
                return visitor.visitOtherstmt(self)
            else:
                return visitor.visitChildren(self)




    def otherstmt(self):

        localctx = ZCodeParser.OtherstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_otherstmt)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.breakstmt()
                pass
            elif token in [ZCodeParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.continuestmt()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 289
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 290
                self.blockstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(ZCodeParser.RETURN)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOL_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 298
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(ZCodeParser.BEGIN)
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 302
                self.match(ZCodeParser.NEWLINE)


            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 305
                    self.stmt() 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 311
                self.match(ZCodeParser.NEWLINE)


            self.state = 314
            self.match(ZCodeParser.END)
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 315
                self.match(ZCodeParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def builtin(self):
            return self.getTypedRuleContext(ZCodeParser.BuiltinContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = ZCodeParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_funccall)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 319
                self.match(ZCodeParser.LPAREN)
                self.state = 320
                self.paramlist()
                self.state = 321
                self.match(ZCodeParser.RPAREN)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.builtin()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_paramlist)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.paramprime()
                pass
            elif token in [ZCodeParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_paramprime)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.param()
                self.state = 331
                self.match(ZCodeParser.COMMA)
                self.state = 332
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_param)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.funccall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 340
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def ELLIPSIS(self):
            return self.getToken(ZCodeParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expr)
        try:
            self.state = 348
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.expr1()
                self.state = 344
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 345
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def relationals(self):
            return self.getTypedRuleContext(ZCodeParser.RelationalsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr1)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.expr2(0)
                self.state = 351
                self.relationals()
                self.state = 352
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 362
                    self.expr3(0) 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 371
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 372
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 373
                    self.expr4(0) 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(ZCodeParser.MODULO, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 382
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 383
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 384
                    self.expr5() 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr5)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(ZCodeParser.NOT)
                self.state = 391
                self.expr5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr6)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(ZCodeParser.MINUS)
                self.state = 396
                self.expr6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(ZCodeParser.LBRACKET, 0)

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def expr9(self):
            return self.getTypedRuleContext(ZCodeParser.Expr9Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr7)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 400
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 401
                    self.funccall()
                    pass


                self.state = 404
                self.match(ZCodeParser.LBRACKET)
                self.state = 405
                self.expr8()
                self.state = 406
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr8)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.expr()
                self.state = 412
                self.match(ZCodeParser.COMMA)
                self.state = 413
                self.expr8()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def funccall(self):
            return self.getTypedRuleContext(ZCodeParser.FunccallContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = ZCodeParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr9)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.match(ZCodeParser.LPAREN)
                self.state = 420
                self.expr()
                self.state = 421
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 423
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 424
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relationals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationals" ):
                return visitor.visitRelationals(self)
            else:
                return visitor.visitChildren(self)




    def relationals(self):

        localctx = ZCodeParser.RelationalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_relationals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.ASSIGN) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_THAN_OR_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.GREATER_THAN_OR_EQUAL) | (1 << ZCodeParser.EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(ZCodeParser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(ZCodeParser.BOOL_LITERAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOL_LITERAL) | (1 << ZCodeParser.STRING_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[38] = self.expr2_sempred
        self._predicates[39] = self.expr3_sempred
        self._predicates[40] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




