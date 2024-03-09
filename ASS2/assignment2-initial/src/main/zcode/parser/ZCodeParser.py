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
        buf.write("\u01a6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\6\2h")
        buf.write("\n\2\r\2\16\2i\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3z\n\3\3\3\6\3}\n\3\r\3\16\3~\3\4\3")
        buf.write("\4\3\4\5\4\u0084\n\4\3\4\3\4\5\4\u0088\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u0093\n\6\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u0099\n\7\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u00a1\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\5\f\u00af\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b7\n\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u00d7\n")
        buf.write("\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u00e2\n\27\3\30\3\30\5\30\u00e6\n\30\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\7\32\u00ef\n\32\f\32\16\32\u00f2\13")
        buf.write("\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\7\33\u00fb\n\33")
        buf.write("\f\33\16\33\u00fe\13\33\3\33\3\33\3\33\3\33\5\33\u0104")
        buf.write("\n\33\3\34\3\34\3\34\5\34\u0109\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0112\n\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u011a\n\36\3\37\3\37\3 \3 \3!\3!\5!\u0122")
        buf.write("\n!\3\"\3\"\5\"\u0126\n\"\3\"\7\"\u0129\n\"\f\"\16\"\u012c")
        buf.write("\13\"\3\"\5\"\u012f\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\5#\u0139")
        buf.write("\n#\3$\3$\5$\u013d\n$\3%\3%\3%\3%\3%\5%\u0144\n%\3&\3")
        buf.write("&\3&\3&\5&\u014a\n&\3\'\3\'\3\'\3\'\3\'\5\'\u0151\n\'")
        buf.write("\3(\3(\3(\3(\3(\5(\u0158\n(\3)\3)\3)\3)\3)\3)\7)\u0160")
        buf.write("\n)\f)\16)\u0163\13)\3*\3*\3*\3*\3*\3*\7*\u016b\n*\f*")
        buf.write("\16*\u016e\13*\3+\3+\3+\3+\3+\3+\7+\u0176\n+\f+\16+\u0179")
        buf.write("\13+\3,\3,\3,\5,\u017e\n,\3-\3-\3-\5-\u0183\n-\3.\3.\5")
        buf.write(".\u0187\n.\3.\3.\3.\3.\3.\5.\u018e\n.\3/\3/\3/\3/\3/\5")
        buf.write("/\u0195\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u019e")
        buf.write("\n\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\u012a\5PRT")
        buf.write("\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\b\3\2%&\3\2\37 \3")
        buf.write("\2!#\5\2\'\')-//\3\2\16\20\3\2\t\13\2\u01ae\2g\3\2\2\2")
        buf.write("\4y\3\2\2\2\6\u0080\3\2\2\2\b\u0089\3\2\2\2\n\u008e\3")
        buf.write("\2\2\2\f\u0094\3\2\2\2\16\u009a\3\2\2\2\20\u00a0\3\2\2")
        buf.write("\2\22\u00a7\3\2\2\2\24\u00a9\3\2\2\2\26\u00ae\3\2\2\2")
        buf.write("\30\u00b6\3\2\2\2\32\u00b8\3\2\2\2\34\u00ba\3\2\2\2\36")
        buf.write("\u00be\3\2\2\2 \u00c0\3\2\2\2\"\u00c4\3\2\2\2$\u00c6\3")
        buf.write("\2\2\2&\u00ca\3\2\2\2(\u00d6\3\2\2\2*\u00d8\3\2\2\2,\u00e1")
        buf.write("\3\2\2\2.\u00e5\3\2\2\2\60\u00e7\3\2\2\2\62\u00eb\3\2")
        buf.write("\2\2\64\u0103\3\2\2\2\66\u0108\3\2\2\28\u010a\3\2\2\2")
        buf.write(":\u0119\3\2\2\2<\u011b\3\2\2\2>\u011d\3\2\2\2@\u011f\3")
        buf.write("\2\2\2B\u0123\3\2\2\2D\u0138\3\2\2\2F\u013c\3\2\2\2H\u0143")
        buf.write("\3\2\2\2J\u0149\3\2\2\2L\u0150\3\2\2\2N\u0157\3\2\2\2")
        buf.write("P\u0159\3\2\2\2R\u0164\3\2\2\2T\u016f\3\2\2\2V\u017d\3")
        buf.write("\2\2\2X\u0182\3\2\2\2Z\u018d\3\2\2\2\\\u0194\3\2\2\2^")
        buf.write("\u019d\3\2\2\2`\u019f\3\2\2\2b\u01a1\3\2\2\2d\u01a3\3")
        buf.write("\2\2\2fh\5\4\3\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2")
        buf.write("\2jk\3\2\2\2kl\7\2\2\3l\3\3\2\2\2mz\5\6\4\2nz\5\b\5\2")
        buf.write("oz\5\n\6\2pz\5\f\7\2qz\5\30\r\2rz\5D#\2sz\5&\24\2tz\5")
        buf.write("\60\31\2uz\5\62\32\2vz\58\35\2wz\5:\36\2xz\5L\'\2ym\3")
        buf.write("\2\2\2yn\3\2\2\2yo\3\2\2\2yp\3\2\2\2yq\3\2\2\2yr\3\2\2")
        buf.write("\2ys\3\2\2\2yt\3\2\2\2yu\3\2\2\2yv\3\2\2\2yw\3\2\2\2y")
        buf.write("x\3\2\2\2z|\3\2\2\2{}\7\67\2\2|{\3\2\2\2}~\3\2\2\2~|\3")
        buf.write("\2\2\2~\177\3\2\2\2\177\5\3\2\2\2\u0080\u0083\5b\62\2")
        buf.write("\u0081\u0084\7\65\2\2\u0082\u0084\5Z.\2\u0083\u0081\3")
        buf.write("\2\2\2\u0083\u0082\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0086")
        buf.write("\7(\2\2\u0086\u0088\5L\'\2\u0087\u0085\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\7\3\2\2\2\u0089\u008a\7\22\2\2\u008a\u008b")
        buf.write("\7\65\2\2\u008b\u008c\7(\2\2\u008c\u008d\5L\'\2\u008d")
        buf.write("\t\3\2\2\2\u008e\u008f\7\23\2\2\u008f\u0092\7\65\2\2\u0090")
        buf.write("\u0091\7(\2\2\u0091\u0093\5L\'\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\13\3\2\2\2\u0094\u0095\7\24\2\2\u0095")
        buf.write("\u0096\7\65\2\2\u0096\u0098\5\16\b\2\u0097\u0099\5\26")
        buf.write("\f\2\u0098\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099\r\3")
        buf.write("\2\2\2\u009a\u009b\7\61\2\2\u009b\u009c\5\20\t\2\u009c")
        buf.write("\u009d\7\62\2\2\u009d\17\3\2\2\2\u009e\u00a1\5\22\n\2")
        buf.write("\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3")
        buf.write("\2\2\2\u00a1\21\3\2\2\2\u00a2\u00a3\5\24\13\2\u00a3\u00a4")
        buf.write("\7\60\2\2\u00a4\u00a5\5\22\n\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write("\u00a8\5\24\13\2\u00a7\u00a2\3\2\2\2\u00a7\u00a6\3\2\2")
        buf.write("\2\u00a8\23\3\2\2\2\u00a9\u00aa\5b\62\2\u00aa\u00ab\5")
        buf.write("L\'\2\u00ab\25\3\2\2\2\u00ac\u00af\5@!\2\u00ad\u00af\5")
        buf.write("B\"\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\27")
        buf.write("\3\2\2\2\u00b0\u00b7\5\32\16\2\u00b1\u00b7\5\34\17\2\u00b2")
        buf.write("\u00b7\5\36\20\2\u00b3\u00b7\5 \21\2\u00b4\u00b7\5\"\22")
        buf.write("\2\u00b5\u00b7\5$\23\2\u00b6\u00b0\3\2\2\2\u00b6\u00b1")
        buf.write("\3\2\2\2\u00b6\u00b2\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\31\3\2\2\2\u00b8")
        buf.write("\u00b9\7\3\2\2\u00b9\33\3\2\2\2\u00ba\u00bb\7\4\2\2\u00bb")
        buf.write("\u00bc\5L\'\2\u00bc\u00bd\7\62\2\2\u00bd\35\3\2\2\2\u00be")
        buf.write("\u00bf\7\5\2\2\u00bf\37\3\2\2\2\u00c0\u00c1\7\6\2\2\u00c1")
        buf.write("\u00c2\5L\'\2\u00c2\u00c3\7\62\2\2\u00c3!\3\2\2\2\u00c4")
        buf.write("\u00c5\7\7\2\2\u00c5#\3\2\2\2\u00c6\u00c7\7\b\2\2\u00c7")
        buf.write("\u00c8\5L\'\2\u00c8\u00c9\7\62\2\2\u00c9%\3\2\2\2\u00ca")
        buf.write("\u00cb\5b\62\2\u00cb\u00cc\7\65\2\2\u00cc\u00cd\7\63\2")
        buf.write("\2\u00cd\u00ce\5(\25\2\u00ce\u00cf\7\64\2\2\u00cf\u00d0")
        buf.write("\7(\2\2\u00d0\u00d1\5*\26\2\u00d1\'\3\2\2\2\u00d2\u00d3")
        buf.write("\7\t\2\2\u00d3\u00d4\7\60\2\2\u00d4\u00d7\5(\25\2\u00d5")
        buf.write("\u00d7\7\t\2\2\u00d6\u00d2\3\2\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7)\3\2\2\2\u00d8\u00d9\7\63\2\2\u00d9\u00da\5,\27")
        buf.write("\2\u00da\u00db\7\64\2\2\u00db+\3\2\2\2\u00dc\u00dd\5.")
        buf.write("\30\2\u00dd\u00de\7\60\2\2\u00de\u00df\5.\30\2\u00df\u00e2")
        buf.write("\3\2\2\2\u00e0\u00e2\3\2\2\2\u00e1\u00dc\3\2\2\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e2-\3\2\2\2\u00e3\u00e6\5d\63\2\u00e4")
        buf.write("\u00e6\5*\26\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2")
        buf.write("\u00e6/\3\2\2\2\u00e7\u00e8\5L\'\2\u00e8\u00e9\7(\2\2")
        buf.write("\u00e9\u00ea\5L\'\2\u00ea\61\3\2\2\2\u00eb\u00ec\7\32")
        buf.write("\2\2\u00ec\u00f0\5L\'\2\u00ed\u00ef\7\67\2\2\u00ee\u00ed")
        buf.write("\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f4\5\4\3\2\u00f4\u00f5\5\64\33\2\u00f5\u00f6")
        buf.write("\5\66\34\2\u00f6\63\3\2\2\2\u00f7\u00f8\7\34\2\2\u00f8")
        buf.write("\u00fc\5L\'\2\u00f9\u00fb\7\67\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100")
        buf.write("\5\4\3\2\u0100\u0101\5\64\33\2\u0101\u0104\3\2\2\2\u0102")
        buf.write("\u0104\3\2\2\2\u0103\u00f7\3\2\2\2\u0103\u0102\3\2\2\2")
        buf.write("\u0104\65\3\2\2\2\u0105\u0106\7\33\2\2\u0106\u0109\5\4")
        buf.write("\3\2\u0107\u0109\3\2\2\2\u0108\u0105\3\2\2\2\u0108\u0107")
        buf.write("\3\2\2\2\u0109\67\3\2\2\2\u010a\u010b\7\25\2\2\u010b\u010c")
        buf.write("\7\65\2\2\u010c\u010d\7\26\2\2\u010d\u010e\5L\'\2\u010e")
        buf.write("\u010f\7\27\2\2\u010f\u0111\5L\'\2\u0110\u0112\7\67\2")
        buf.write("\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0114\5\4\3\2\u01149\3\2\2\2\u0115\u011a")
        buf.write("\5<\37\2\u0116\u011a\5> \2\u0117\u011a\5@!\2\u0118\u011a")
        buf.write("\5B\"\2\u0119\u0115\3\2\2\2\u0119\u0116\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u011a;\3\2\2\2\u011b")
        buf.write("\u011c\7\30\2\2\u011c=\3\2\2\2\u011d\u011e\7\31\2\2\u011e")
        buf.write("?\3\2\2\2\u011f\u0121\7\21\2\2\u0120\u0122\5L\'\2\u0121")
        buf.write("\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122A\3\2\2\2\u0123")
        buf.write("\u0125\7\35\2\2\u0124\u0126\7\67\2\2\u0125\u0124\3\2\2")
        buf.write("\2\u0125\u0126\3\2\2\2\u0126\u012a\3\2\2\2\u0127\u0129")
        buf.write("\5\4\3\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012e\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012d\u012f\7\67\2\2\u012e\u012d")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u0131\7\36\2\2\u0131C\3\2\2\2\u0132\u0133\7\65\2\2\u0133")
        buf.write("\u0134\7\61\2\2\u0134\u0135\5F$\2\u0135\u0136\7\62\2\2")
        buf.write("\u0136\u0139\3\2\2\2\u0137\u0139\5\30\r\2\u0138\u0132")
        buf.write("\3\2\2\2\u0138\u0137\3\2\2\2\u0139E\3\2\2\2\u013a\u013d")
        buf.write("\5H%\2\u013b\u013d\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013b")
        buf.write("\3\2\2\2\u013dG\3\2\2\2\u013e\u013f\5J&\2\u013f\u0140")
        buf.write("\7\60\2\2\u0140\u0141\5H%\2\u0141\u0144\3\2\2\2\u0142")
        buf.write("\u0144\5J&\2\u0143\u013e\3\2\2\2\u0143\u0142\3\2\2\2\u0144")
        buf.write("I\3\2\2\2\u0145\u014a\5d\63\2\u0146\u014a\5D#\2\u0147")
        buf.write("\u014a\7\65\2\2\u0148\u014a\5L\'\2\u0149\u0145\3\2\2\2")
        buf.write("\u0149\u0146\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u0148\3")
        buf.write("\2\2\2\u014aK\3\2\2\2\u014b\u014c\5N(\2\u014c\u014d\7")
        buf.write(".\2\2\u014d\u014e\5N(\2\u014e\u0151\3\2\2\2\u014f\u0151")
        buf.write("\5N(\2\u0150\u014b\3\2\2\2\u0150\u014f\3\2\2\2\u0151M")
        buf.write("\3\2\2\2\u0152\u0153\5P)\2\u0153\u0154\5`\61\2\u0154\u0155")
        buf.write("\5P)\2\u0155\u0158\3\2\2\2\u0156\u0158\5P)\2\u0157\u0152")
        buf.write("\3\2\2\2\u0157\u0156\3\2\2\2\u0158O\3\2\2\2\u0159\u015a")
        buf.write("\b)\1\2\u015a\u015b\5R*\2\u015b\u0161\3\2\2\2\u015c\u015d")
        buf.write("\f\4\2\2\u015d\u015e\t\2\2\2\u015e\u0160\5R*\2\u015f\u015c")
        buf.write("\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162Q\3\2\2\2\u0163\u0161\3\2\2\2\u0164")
        buf.write("\u0165\b*\1\2\u0165\u0166\5T+\2\u0166\u016c\3\2\2\2\u0167")
        buf.write("\u0168\f\4\2\2\u0168\u0169\t\3\2\2\u0169\u016b\5T+\2\u016a")
        buf.write("\u0167\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016dS\3\2\2\2\u016e\u016c\3\2\2")
        buf.write("\2\u016f\u0170\b+\1\2\u0170\u0171\5V,\2\u0171\u0177\3")
        buf.write("\2\2\2\u0172\u0173\f\4\2\2\u0173\u0174\t\4\2\2\u0174\u0176")
        buf.write("\5V,\2\u0175\u0172\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178U\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u017a\u017b\7$\2\2\u017b\u017e\5V,\2\u017c\u017e")
        buf.write("\5X-\2\u017d\u017a\3\2\2\2\u017d\u017c\3\2\2\2\u017eW")
        buf.write("\3\2\2\2\u017f\u0180\7 \2\2\u0180\u0183\5X-\2\u0181\u0183")
        buf.write("\5Z.\2\u0182\u017f\3\2\2\2\u0182\u0181\3\2\2\2\u0183Y")
        buf.write("\3\2\2\2\u0184\u0187\7\65\2\2\u0185\u0187\5D#\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u0189\7\63\2\2\u0189\u018a\5\\/\2\u018a\u018b\7")
        buf.write("\64\2\2\u018b\u018e\3\2\2\2\u018c\u018e\5^\60\2\u018d")
        buf.write("\u0186\3\2\2\2\u018d\u018c\3\2\2\2\u018e[\3\2\2\2\u018f")
        buf.write("\u0190\5L\'\2\u0190\u0191\7\60\2\2\u0191\u0192\5\\/\2")
        buf.write("\u0192\u0195\3\2\2\2\u0193\u0195\5L\'\2\u0194\u018f\3")
        buf.write("\2\2\2\u0194\u0193\3\2\2\2\u0195]\3\2\2\2\u0196\u019e")
        buf.write("\5d\63\2\u0197\u0198\7\61\2\2\u0198\u0199\5L\'\2\u0199")
        buf.write("\u019a\7\62\2\2\u019a\u019e\3\2\2\2\u019b\u019e\5D#\2")
        buf.write("\u019c\u019e\7\65\2\2\u019d\u0196\3\2\2\2\u019d\u0197")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("_\3\2\2\2\u019f\u01a0\t\5\2\2\u01a0a\3\2\2\2\u01a1\u01a2")
        buf.write("\t\6\2\2\u01a2c\3\2\2\2\u01a3\u01a4\t\7\2\2\u01a4e\3\2")
        buf.write("\2\2)iy~\u0083\u0087\u0092\u0098\u00a0\u00a7\u00ae\u00b6")
        buf.write("\u00d6\u00e1\u00e5\u00f0\u00fc\u0103\u0108\u0111\u0119")
        buf.write("\u0121\u0125\u012a\u012e\u0138\u013c\u0143\u0149\u0150")
        buf.write("\u0157\u0161\u016c\u0177\u017d\u0182\u0186\u018d\u0194")
        buf.write("\u019d")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber()'", "'writeNumber('", "'readBool()'", 
                     "'writeBool('", "'readString()'", "'writeString('", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'...'", "'=='", "','", "'('", 
                     "')'", "'['", "']'" ]

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
    RULE_arraylist = 21
    RULE_arrayelement = 22
    RULE_assignstmt = 23
    RULE_ifstmt = 24
    RULE_elifstmt = 25
    RULE_elsestmt = 26
    RULE_forstmt = 27
    RULE_otherstmt = 28
    RULE_breakstmt = 29
    RULE_continuestmt = 30
    RULE_returnstmt = 31
    RULE_blockstmt = 32
    RULE_funccall = 33
    RULE_paramlist = 34
    RULE_paramprime = 35
    RULE_param = 36
    RULE_expr = 37
    RULE_expr1 = 38
    RULE_expr2 = 39
    RULE_expr3 = 40
    RULE_expr4 = 41
    RULE_expr5 = 42
    RULE_expr6 = 43
    RULE_expr7 = 44
    RULE_expr8 = 45
    RULE_expr9 = 46
    RULE_relationals = 47
    RULE_typ = 48
    RULE_literals = 49

    ruleNames =  [ "program", "stmt", "vardecl", "im_vardecl", "im_dydecl", 
                   "funcdecl", "arg", "arglist", "argprime", "argment", 
                   "funcend", "builtin", "readnum", "writenum", "readbool", 
                   "writebool", "readstr", "writestr", "arraydecl", "arraydim", 
                   "array", "arraylist", "arrayelement", "assignstmt", "ifstmt", 
                   "elifstmt", "elsestmt", "forstmt", "otherstmt", "breakstmt", 
                   "continuestmt", "returnstmt", "blockstmt", "funccall", 
                   "paramlist", "paramprime", "param", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "expr9", "relationals", "typ", "literals" ]

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
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                self.stmt()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOL_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDENTIFIER))) != 0)):
                    break

            self.state = 105
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
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 107
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 108
                self.im_vardecl()
                pass

            elif la_ == 3:
                self.state = 109
                self.im_dydecl()
                pass

            elif la_ == 4:
                self.state = 110
                self.funcdecl()
                pass

            elif la_ == 5:
                self.state = 111
                self.builtin()
                pass

            elif la_ == 6:
                self.state = 112
                self.funccall()
                pass

            elif la_ == 7:
                self.state = 113
                self.arraydecl()
                pass

            elif la_ == 8:
                self.state = 114
                self.assignstmt()
                pass

            elif la_ == 9:
                self.state = 115
                self.ifstmt()
                pass

            elif la_ == 10:
                self.state = 116
                self.forstmt()
                pass

            elif la_ == 11:
                self.state = 117
                self.otherstmt()
                pass

            elif la_ == 12:
                self.state = 118
                self.expr()
                pass


            self.state = 122 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 121
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 124 
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
            self.state = 126
            self.typ()
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 127
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 128
                self.expr7()
                pass


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 131
                self.match(ZCodeParser.ARROW)
                self.state = 132
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
            self.state = 135
            self.match(ZCodeParser.VAR)
            self.state = 136
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 137
            self.match(ZCodeParser.ARROW)
            self.state = 138
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
            self.state = 140
            self.match(ZCodeParser.DYNAMIC)
            self.state = 141
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 142
                self.match(ZCodeParser.ARROW)
                self.state = 143
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ZCodeParser.FUNC)
            self.state = 147
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 148
            self.arg()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.RETURN or _la==ZCodeParser.BEGIN:
                self.state = 149
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
            self.state = 172
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
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.readnum()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.writenum()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.readbool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.writebool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.readstr()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
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
            self.state = 182
            self.match(ZCodeParser.T__0)
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
            self.state = 184
            self.match(ZCodeParser.T__1)
            self.state = 185
            self.expr()
            self.state = 186
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
            self.state = 188
            self.match(ZCodeParser.T__2)
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
            self.state = 190
            self.match(ZCodeParser.T__3)
            self.state = 191
            self.expr()
            self.state = 192
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
            self.state = 194
            self.match(ZCodeParser.T__4)
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
            self.state = 196
            self.match(ZCodeParser.T__5)
            self.state = 197
            self.expr()
            self.state = 198
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
            self.state = 200
            self.typ()
            self.state = 201
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 202
            self.match(ZCodeParser.LBRACKET)
            self.state = 203
            self.arraydim()
            self.state = 204
            self.match(ZCodeParser.RBRACKET)
            self.state = 205
            self.match(ZCodeParser.ARROW)
            self.state = 206
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

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arraydim(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydimContext,0)


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
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 209
                self.match(ZCodeParser.COMMA)
                self.state = 210
                self.arraydim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass


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

        def arraylist(self):
            return self.getTypedRuleContext(ZCodeParser.ArraylistContext,0)


        def RBRACKET(self):
            return self.getToken(ZCodeParser.RBRACKET, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ZCodeParser.LBRACKET)
            self.state = 215
            self.arraylist()
            self.state = 216
            self.match(ZCodeParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayelement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ArrayelementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ArrayelementContext,i)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylist" ):
                return visitor.visitArraylist(self)
            else:
                return visitor.visitChildren(self)




    def arraylist(self):

        localctx = ZCodeParser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arraylist)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.arrayelement()
                self.state = 219
                self.match(ZCodeParser.COMMA)
                self.state = 220
                self.arrayelement()
                pass
            elif token in [ZCodeParser.RBRACKET]:
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


    class ArrayelementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralsContext,0)


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
        self.enterRule(localctx, 44, self.RULE_arrayelement)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.literals()
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
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
        self.enterRule(localctx, 46, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.expr()
            self.state = 230
            self.match(ZCodeParser.ARROW)
            self.state = 231
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
        self.enterRule(localctx, 48, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ZCodeParser.IF)
            self.state = 234
            self.expr()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 235
                self.match(ZCodeParser.NEWLINE)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 241
            self.stmt()
            self.state = 242
            self.elifstmt()
            self.state = 243
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
        self.enterRule(localctx, 50, self.RULE_elifstmt)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(ZCodeParser.ELIF)
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
        self.enterRule(localctx, 52, self.RULE_elsestmt)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(ZCodeParser.ELSE)
                self.state = 260
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
        self.enterRule(localctx, 54, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ZCodeParser.FOR)
            self.state = 265
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 266
            self.match(ZCodeParser.UNTIL)
            self.state = 267
            self.expr()
            self.state = 268
            self.match(ZCodeParser.BY)
            self.state = 269
            self.expr()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 270
                self.match(ZCodeParser.NEWLINE)


            self.state = 273
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
        self.enterRule(localctx, 56, self.RULE_otherstmt)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.breakstmt()
                pass
            elif token in [ZCodeParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.continuestmt()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
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
        self.enterRule(localctx, 58, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
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
        self.enterRule(localctx, 60, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
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
        self.enterRule(localctx, 62, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ZCodeParser.RETURN)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOL_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 286
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
        self.enterRule(localctx, 64, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.BEGIN)
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 290
                self.match(ZCodeParser.NEWLINE)


            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 293
                    self.stmt() 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 299
                self.match(ZCodeParser.NEWLINE)


            self.state = 302
            self.match(ZCodeParser.END)
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
        self.enterRule(localctx, 66, self.RULE_funccall)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 305
                self.match(ZCodeParser.LPAREN)
                self.state = 306
                self.paramlist()
                self.state = 307
                self.match(ZCodeParser.RPAREN)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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
        self.enterRule(localctx, 68, self.RULE_paramlist)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
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
        self.enterRule(localctx, 70, self.RULE_paramprime)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.param()
                self.state = 317
                self.match(ZCodeParser.COMMA)
                self.state = 318
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
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
        self.enterRule(localctx, 72, self.RULE_param)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.funccall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
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
        self.enterRule(localctx, 74, self.RULE_expr)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.expr1()
                self.state = 330
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 331
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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
        self.enterRule(localctx, 76, self.RULE_expr1)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.expr2(0)
                self.state = 337
                self.relationals()
                self.state = 338
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 346
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 347
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 348
                    self.expr3(0) 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 357
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 359
                    self.expr4(0) 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 370
                    self.expr5() 
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_expr5)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(ZCodeParser.NOT)
                self.state = 377
                self.expr5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
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
        self.enterRule(localctx, 86, self.RULE_expr6)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(ZCodeParser.MINUS)
                self.state = 382
                self.expr6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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
        self.enterRule(localctx, 88, self.RULE_expr7)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 386
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 387
                    self.funccall()
                    pass


                self.state = 390
                self.match(ZCodeParser.LBRACKET)
                self.state = 391
                self.expr8()
                self.state = 392
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
        self.enterRule(localctx, 90, self.RULE_expr8)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.expr()
                self.state = 398
                self.match(ZCodeParser.COMMA)
                self.state = 399
                self.expr8()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
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
        self.enterRule(localctx, 92, self.RULE_expr9)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(ZCodeParser.LPAREN)
                self.state = 406
                self.expr()
                self.state = 407
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 410
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
        self.enterRule(localctx, 94, self.RULE_relationals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
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
        self.enterRule(localctx, 96, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
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
        self.enterRule(localctx, 98, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
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
        self._predicates[39] = self.expr2_sempred
        self._predicates[40] = self.expr3_sempred
        self._predicates[41] = self.expr4_sempred
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
         




