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
        buf.write("\u01b7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\7\2d\n\2\f\2\16\2g\13\2\3")
        buf.write("\2\3\2\6\2k\n\2\r\2\16\2l\3\2\7\2p\n\2\f\2\16\2s\13\2")
        buf.write("\3\2\6\2v\n\2\r\2\16\2w\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u0088\n\3\3\4\3\4\3\4\5")
        buf.write("\4\u008d\n\4\3\4\3\4\5\4\u0091\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\5\6\u009c\n\6\3\7\3\7\3\7\3\7\5\7\u00a2")
        buf.write("\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u00ac\n\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00b3\n\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\5\f\u00bb\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00c3\n")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\7\25\u00eb\n\25\f\25\16")
        buf.write("\25\u00ee\13\25\3\26\3\26\3\26\3\26\7\26\u00f4\n\26\f")
        buf.write("\26\16\26\u00f7\13\26\3\26\3\26\3\27\3\27\5\27\u00fd\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\7\31\u0106\n\31")
        buf.write("\f\31\16\31\u0109\13\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\7\32\u0113\n\32\f\32\16\32\u0116\13\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u011c\n\32\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0122\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u012b\n\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u0133\n")
        buf.write("\35\3\36\3\36\3\37\3\37\3 \3 \5 \u013b\n \3!\3!\3!\3!")
        buf.write("\3!\7!\u0142\n!\f!\16!\u0145\13!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0150\n\"\3#\3#\5#\u0154\n#\3$\3$\3$")
        buf.write("\3$\3$\5$\u015b\n$\3%\3%\3%\3%\3%\5%\u0162\n%\3&\3&\3")
        buf.write("&\3&\3&\5&\u0169\n&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0171")
        buf.write("\n\'\f\'\16\'\u0174\13\'\3(\3(\3(\3(\3(\3(\7(\u017c\n")
        buf.write("(\f(\16(\u017f\13(\3)\3)\3)\3)\3)\3)\7)\u0187\n)\f)\16")
        buf.write(")\u018a\13)\3*\3*\3*\5*\u018f\n*\3+\3+\3+\5+\u0194\n+")
        buf.write("\3,\3,\5,\u0198\n,\3,\3,\3,\3,\3,\5,\u019f\n,\3-\3-\3")
        buf.write("-\3-\3-\5-\u01a6\n-\3.\3.\3.\3.\3.\3.\3.\5.\u01af\n.\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3e\5LNP\62\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`\2\b\3\2%&\3\2\37 \3\2!#\5\2\'\')-//\3\2")
        buf.write("\16\20\3\2\t\13\2\u01bf\2e\3\2\2\2\4\u0087\3\2\2\2\6\u0089")
        buf.write("\3\2\2\2\b\u0092\3\2\2\2\n\u0097\3\2\2\2\f\u009d\3\2\2")
        buf.write("\2\16\u00a5\3\2\2\2\20\u00ab\3\2\2\2\22\u00b2\3\2\2\2")
        buf.write("\24\u00b4\3\2\2\2\26\u00ba\3\2\2\2\30\u00c2\3\2\2\2\32")
        buf.write("\u00c4\3\2\2\2\34\u00c8\3\2\2\2\36\u00cd\3\2\2\2 \u00d1")
        buf.write("\3\2\2\2\"\u00d6\3\2\2\2$\u00da\3\2\2\2&\u00df\3\2\2\2")
        buf.write("(\u00e7\3\2\2\2*\u00ef\3\2\2\2,\u00fc\3\2\2\2.\u00fe\3")
        buf.write("\2\2\2\60\u0102\3\2\2\2\62\u011b\3\2\2\2\64\u0121\3\2")
        buf.write("\2\2\66\u0123\3\2\2\28\u0132\3\2\2\2:\u0134\3\2\2\2<\u0136")
        buf.write("\3\2\2\2>\u0138\3\2\2\2@\u013c\3\2\2\2B\u014f\3\2\2\2")
        buf.write("D\u0153\3\2\2\2F\u015a\3\2\2\2H\u0161\3\2\2\2J\u0168\3")
        buf.write("\2\2\2L\u016a\3\2\2\2N\u0175\3\2\2\2P\u0180\3\2\2\2R\u018e")
        buf.write("\3\2\2\2T\u0193\3\2\2\2V\u019e\3\2\2\2X\u01a5\3\2\2\2")
        buf.write("Z\u01ae\3\2\2\2\\\u01b0\3\2\2\2^\u01b2\3\2\2\2`\u01b4")
        buf.write("\3\2\2\2bd\7\67\2\2cb\3\2\2\2dg\3\2\2\2ef\3\2\2\2ec\3")
        buf.write("\2\2\2fh\3\2\2\2ge\3\2\2\2hq\5\4\3\2ik\7\67\2\2ji\3\2")
        buf.write("\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2mn\3\2\2\2np\5\4\3\2")
        buf.write("oj\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2ru\3\2\2\2sq\3")
        buf.write("\2\2\2tv\7\67\2\2ut\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2")
        buf.write("\2\2xy\3\2\2\2yz\7\2\2\3z\3\3\2\2\2{\u0088\5\6\4\2|\u0088")
        buf.write("\5\b\5\2}\u0088\5\n\6\2~\u0088\5\f\7\2\177\u0088\5\30")
        buf.write("\r\2\u0080\u0088\5B\"\2\u0081\u0088\5&\24\2\u0082\u0088")
        buf.write("\5.\30\2\u0083\u0088\5\60\31\2\u0084\u0088\5\66\34\2\u0085")
        buf.write("\u0088\58\35\2\u0086\u0088\5H%\2\u0087{\3\2\2\2\u0087")
        buf.write("|\3\2\2\2\u0087}\3\2\2\2\u0087~\3\2\2\2\u0087\177\3\2")
        buf.write("\2\2\u0087\u0080\3\2\2\2\u0087\u0081\3\2\2\2\u0087\u0082")
        buf.write("\3\2\2\2\u0087\u0083\3\2\2\2\u0087\u0084\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088\5\3\2\2\2\u0089")
        buf.write("\u008c\5^\60\2\u008a\u008d\7\65\2\2\u008b\u008d\5V,\2")
        buf.write("\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3")
        buf.write("\2\2\2\u008e\u008f\7(\2\2\u008f\u0091\5H%\2\u0090\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\7\3\2\2\2\u0092\u0093")
        buf.write("\7\22\2\2\u0093\u0094\7\65\2\2\u0094\u0095\7(\2\2\u0095")
        buf.write("\u0096\5H%\2\u0096\t\3\2\2\2\u0097\u0098\7\23\2\2\u0098")
        buf.write("\u009b\7\65\2\2\u0099\u009a\7(\2\2\u009a\u009c\5H%\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\13\3\2\2\2\u009d")
        buf.write("\u009e\7\24\2\2\u009e\u009f\7\65\2\2\u009f\u00a1\5\16")
        buf.write("\b\2\u00a0\u00a2\7\67\2\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\5\26\f\2\u00a4")
        buf.write("\r\3\2\2\2\u00a5\u00a6\7\61\2\2\u00a6\u00a7\5\20\t\2\u00a7")
        buf.write("\u00a8\7\62\2\2\u00a8\17\3\2\2\2\u00a9\u00ac\5\22\n\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3")
        buf.write("\2\2\2\u00ac\21\3\2\2\2\u00ad\u00ae\5\24\13\2\u00ae\u00af")
        buf.write("\7\60\2\2\u00af\u00b0\5\22\n\2\u00b0\u00b3\3\2\2\2\u00b1")
        buf.write("\u00b3\5\24\13\2\u00b2\u00ad\3\2\2\2\u00b2\u00b1\3\2\2")
        buf.write("\2\u00b3\23\3\2\2\2\u00b4\u00b5\5^\60\2\u00b5\u00b6\5")
        buf.write("H%\2\u00b6\25\3\2\2\2\u00b7\u00bb\5> \2\u00b8\u00bb\5")
        buf.write("@!\2\u00b9\u00bb\3\2\2\2\u00ba\u00b7\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\27\3\2\2\2\u00bc\u00c3")
        buf.write("\5\32\16\2\u00bd\u00c3\5\34\17\2\u00be\u00c3\5\36\20\2")
        buf.write("\u00bf\u00c3\5 \21\2\u00c0\u00c3\5\"\22\2\u00c1\u00c3")
        buf.write("\5$\23\2\u00c2\u00bc\3\2\2\2\u00c2\u00bd\3\2\2\2\u00c2")
        buf.write("\u00be\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c1\3\2\2\2\u00c3\31\3\2\2\2\u00c4\u00c5\7\3")
        buf.write("\2\2\u00c5\u00c6\7\61\2\2\u00c6\u00c7\7\62\2\2\u00c7\33")
        buf.write("\3\2\2\2\u00c8\u00c9\7\4\2\2\u00c9\u00ca\7\61\2\2\u00ca")
        buf.write("\u00cb\5H%\2\u00cb\u00cc\7\62\2\2\u00cc\35\3\2\2\2\u00cd")
        buf.write("\u00ce\7\5\2\2\u00ce\u00cf\7\61\2\2\u00cf\u00d0\7\62\2")
        buf.write("\2\u00d0\37\3\2\2\2\u00d1\u00d2\7\6\2\2\u00d2\u00d3\7")
        buf.write("\61\2\2\u00d3\u00d4\5H%\2\u00d4\u00d5\7\62\2\2\u00d5!")
        buf.write("\3\2\2\2\u00d6\u00d7\7\7\2\2\u00d7\u00d8\7\61\2\2\u00d8")
        buf.write("\u00d9\7\62\2\2\u00d9#\3\2\2\2\u00da\u00db\7\b\2\2\u00db")
        buf.write("\u00dc\7\61\2\2\u00dc\u00dd\5H%\2\u00dd\u00de\7\62\2\2")
        buf.write("\u00de%\3\2\2\2\u00df\u00e0\5^\60\2\u00e0\u00e1\7\65\2")
        buf.write("\2\u00e1\u00e2\7\63\2\2\u00e2\u00e3\5(\25\2\u00e3\u00e4")
        buf.write("\7\64\2\2\u00e4\u00e5\7(\2\2\u00e5\u00e6\5*\26\2\u00e6")
        buf.write("\'\3\2\2\2\u00e7\u00ec\7\t\2\2\u00e8\u00e9\7\60\2\2\u00e9")
        buf.write("\u00eb\7\t\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00ee\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed)\3\2\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\7\63\2\2\u00f0\u00f5")
        buf.write("\5,\27\2\u00f1\u00f2\7\60\2\2\u00f2\u00f4\5,\27\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f8\u00f9\7\64\2\2\u00f9+\3\2\2\2\u00fa\u00fd")
        buf.write("\5H%\2\u00fb\u00fd\5*\26\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd-\3\2\2\2\u00fe\u00ff\5H%\2\u00ff\u0100")
        buf.write("\7(\2\2\u0100\u0101\5H%\2\u0101/\3\2\2\2\u0102\u0103\7")
        buf.write("\32\2\2\u0103\u0107\5H%\2\u0104\u0106\7\67\2\2\u0105\u0104")
        buf.write("\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u010a\u010b\5\4\3\2\u010b\u010c\5\62\32\2\u010c\u010d")
        buf.write("\5\64\33\2\u010d\61\3\2\2\2\u010e\u010f\7\67\2\2\u010f")
        buf.write("\u0110\7\34\2\2\u0110\u0114\5H%\2\u0111\u0113\7\67\2\2")
        buf.write("\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112\3")
        buf.write("\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0114")
        buf.write("\3\2\2\2\u0117\u0118\5\4\3\2\u0118\u0119\5\62\32\2\u0119")
        buf.write("\u011c\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u010e\3\2\2\2")
        buf.write("\u011b\u011a\3\2\2\2\u011c\63\3\2\2\2\u011d\u011e\7\67")
        buf.write("\2\2\u011e\u011f\7\33\2\2\u011f\u0122\5\4\3\2\u0120\u0122")
        buf.write("\3\2\2\2\u0121\u011d\3\2\2\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\65\3\2\2\2\u0123\u0124\7\25\2\2\u0124\u0125\7\65\2\2")
        buf.write("\u0125\u0126\7\26\2\2\u0126\u0127\5H%\2\u0127\u0128\7")
        buf.write("\27\2\2\u0128\u012a\5H%\2\u0129\u012b\7\67\2\2\u012a\u0129")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012d\5\4\3\2\u012d\67\3\2\2\2\u012e\u0133\5:\36\2\u012f")
        buf.write("\u0133\5<\37\2\u0130\u0133\5> \2\u0131\u0133\5@!\2\u0132")
        buf.write("\u012e\3\2\2\2\u0132\u012f\3\2\2\2\u0132\u0130\3\2\2\2")
        buf.write("\u0132\u0131\3\2\2\2\u01339\3\2\2\2\u0134\u0135\7\30\2")
        buf.write("\2\u0135;\3\2\2\2\u0136\u0137\7\31\2\2\u0137=\3\2\2\2")
        buf.write("\u0138\u013a\7\21\2\2\u0139\u013b\5H%\2\u013a\u0139\3")
        buf.write("\2\2\2\u013a\u013b\3\2\2\2\u013b?\3\2\2\2\u013c\u013d")
        buf.write("\7\35\2\2\u013d\u013e\7\67\2\2\u013e\u0143\5\4\3\2\u013f")
        buf.write("\u0140\7\67\2\2\u0140\u0142\5\4\3\2\u0141\u013f\3\2\2")
        buf.write("\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144")
        buf.write("\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146")
        buf.write("\u0147\7\67\2\2\u0147\u0148\7\36\2\2\u0148A\3\2\2\2\u0149")
        buf.write("\u014a\7\65\2\2\u014a\u014b\7\61\2\2\u014b\u014c\5D#\2")
        buf.write("\u014c\u014d\7\62\2\2\u014d\u0150\3\2\2\2\u014e\u0150")
        buf.write("\5\30\r\2\u014f\u0149\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("C\3\2\2\2\u0151\u0154\5F$\2\u0152\u0154\3\2\2\2\u0153")
        buf.write("\u0151\3\2\2\2\u0153\u0152\3\2\2\2\u0154E\3\2\2\2\u0155")
        buf.write("\u0156\5H%\2\u0156\u0157\7\60\2\2\u0157\u0158\5F$\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u015b\5H%\2\u015a\u0155\3\2\2\2\u015a")
        buf.write("\u0159\3\2\2\2\u015bG\3\2\2\2\u015c\u015d\5J&\2\u015d")
        buf.write("\u015e\7.\2\2\u015e\u015f\5J&\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u0162\5J&\2\u0161\u015c\3\2\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("I\3\2\2\2\u0163\u0164\5L\'\2\u0164\u0165\5\\/\2\u0165")
        buf.write("\u0166\5L\'\2\u0166\u0169\3\2\2\2\u0167\u0169\5L\'\2\u0168")
        buf.write("\u0163\3\2\2\2\u0168\u0167\3\2\2\2\u0169K\3\2\2\2\u016a")
        buf.write("\u016b\b\'\1\2\u016b\u016c\5N(\2\u016c\u0172\3\2\2\2\u016d")
        buf.write("\u016e\f\4\2\2\u016e\u016f\t\2\2\2\u016f\u0171\5N(\2\u0170")
        buf.write("\u016d\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173M\3\2\2\2\u0174\u0172\3\2\2")
        buf.write("\2\u0175\u0176\b(\1\2\u0176\u0177\5P)\2\u0177\u017d\3")
        buf.write("\2\2\2\u0178\u0179\f\4\2\2\u0179\u017a\t\3\2\2\u017a\u017c")
        buf.write("\5P)\2\u017b\u0178\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017eO\3\2\2\2\u017f\u017d")
        buf.write("\3\2\2\2\u0180\u0181\b)\1\2\u0181\u0182\5R*\2\u0182\u0188")
        buf.write("\3\2\2\2\u0183\u0184\f\4\2\2\u0184\u0185\t\4\2\2\u0185")
        buf.write("\u0187\5R*\2\u0186\u0183\3\2\2\2\u0187\u018a\3\2\2\2\u0188")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189Q\3\2\2\2\u018a")
        buf.write("\u0188\3\2\2\2\u018b\u018c\7$\2\2\u018c\u018f\5R*\2\u018d")
        buf.write("\u018f\5T+\2\u018e\u018b\3\2\2\2\u018e\u018d\3\2\2\2\u018f")
        buf.write("S\3\2\2\2\u0190\u0191\7 \2\2\u0191\u0194\5T+\2\u0192\u0194")
        buf.write("\5V,\2\u0193\u0190\3\2\2\2\u0193\u0192\3\2\2\2\u0194U")
        buf.write("\3\2\2\2\u0195\u0198\7\65\2\2\u0196\u0198\5B\"\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019a\7\63\2\2\u019a\u019b\5X-\2\u019b\u019c\7")
        buf.write("\64\2\2\u019c\u019f\3\2\2\2\u019d\u019f\5Z.\2\u019e\u0197")
        buf.write("\3\2\2\2\u019e\u019d\3\2\2\2\u019fW\3\2\2\2\u01a0\u01a1")
        buf.write("\5H%\2\u01a1\u01a2\7\60\2\2\u01a2\u01a3\5X-\2\u01a3\u01a6")
        buf.write("\3\2\2\2\u01a4\u01a6\5H%\2\u01a5\u01a0\3\2\2\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a6Y\3\2\2\2\u01a7\u01af\5`\61\2\u01a8\u01a9")
        buf.write("\7\61\2\2\u01a9\u01aa\5H%\2\u01aa\u01ab\7\62\2\2\u01ab")
        buf.write("\u01af\3\2\2\2\u01ac\u01af\5B\"\2\u01ad\u01af\7\65\2\2")
        buf.write("\u01ae\u01a7\3\2\2\2\u01ae\u01a8\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01ae\u01ad\3\2\2\2\u01af[\3\2\2\2\u01b0\u01b1")
        buf.write("\t\5\2\2\u01b1]\3\2\2\2\u01b2\u01b3\t\6\2\2\u01b3_\3\2")
        buf.write("\2\2\u01b4\u01b5\t\7\2\2\u01b5a\3\2\2\2(elqw\u0087\u008c")
        buf.write("\u0090\u009b\u00a1\u00ab\u00b2\u00ba\u00c2\u00ec\u00f5")
        buf.write("\u00fc\u0107\u0114\u011b\u0121\u012a\u0132\u013a\u0143")
        buf.write("\u014f\u0153\u015a\u0161\u0168\u0172\u017d\u0188\u018e")
        buf.write("\u0193\u0197\u019e\u01a5\u01ae")
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
    RULE_expr = 35
    RULE_expr1 = 36
    RULE_expr2 = 37
    RULE_expr3 = 38
    RULE_expr4 = 39
    RULE_expr5 = 40
    RULE_expr6 = 41
    RULE_expr7 = 42
    RULE_expr8 = 43
    RULE_expr9 = 44
    RULE_relationals = 45
    RULE_typ = 46
    RULE_literals = 47

    ruleNames =  [ "program", "stmt", "vardecl", "im_vardecl", "im_dydecl", 
                   "funcdecl", "arg", "arglist", "argprime", "argment", 
                   "funcend", "builtin", "readnum", "writenum", "readbool", 
                   "writebool", "readstr", "writestr", "arraydecl", "arraydim", 
                   "array", "arrayelement", "assignstmt", "ifstmt", "elifstmt", 
                   "elsestmt", "forstmt", "otherstmt", "breakstmt", "continuestmt", 
                   "returnstmt", "blockstmt", "funccall", "paramlist", "paramprime", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "relationals", "typ", 
                   "literals" ]

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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 96
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 102
            self.stmt()
            self.state = 111
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 103
                        self.match(ZCodeParser.NEWLINE)
                        self.state = 106 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ZCodeParser.NEWLINE):
                            break

                    self.state = 108
                    self.stmt() 
                self.state = 113
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 115 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 114
                self.match(ZCodeParser.NEWLINE)
                self.state = 117 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

            self.state = 119
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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 121
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 122
                self.im_vardecl()
                pass

            elif la_ == 3:
                self.state = 123
                self.im_dydecl()
                pass

            elif la_ == 4:
                self.state = 124
                self.funcdecl()
                pass

            elif la_ == 5:
                self.state = 125
                self.builtin()
                pass

            elif la_ == 6:
                self.state = 126
                self.funccall()
                pass

            elif la_ == 7:
                self.state = 127
                self.arraydecl()
                pass

            elif la_ == 8:
                self.state = 128
                self.assignstmt()
                pass

            elif la_ == 9:
                self.state = 129
                self.ifstmt()
                pass

            elif la_ == 10:
                self.state = 130
                self.forstmt()
                pass

            elif la_ == 11:
                self.state = 131
                self.otherstmt()
                pass

            elif la_ == 12:
                self.state = 132
                self.expr()
                pass


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
            self.state = 135
            self.typ()
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 136
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 137
                self.expr7()
                pass


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
            self.state = 144
            self.match(ZCodeParser.VAR)
            self.state = 145
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 146
            self.match(ZCodeParser.ARROW)
            self.state = 147
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
            self.state = 149
            self.match(ZCodeParser.DYNAMIC)
            self.state = 150
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 151
                self.match(ZCodeParser.ARROW)
                self.state = 152
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
            self.state = 155
            self.match(ZCodeParser.FUNC)
            self.state = 156
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 157
            self.arg()
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 158
                self.match(ZCodeParser.NEWLINE)


            self.state = 161
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
            self.state = 163
            self.match(ZCodeParser.LPAREN)
            self.state = 164
            self.arglist()
            self.state = 165
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
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
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
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.argment()
                self.state = 172
                self.match(ZCodeParser.COMMA)
                self.state = 173
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
            self.state = 178
            self.typ()
            self.state = 179
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
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
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
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.readnum()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.writenum()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.readbool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.writebool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.readstr()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 191
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
            self.state = 194
            self.match(ZCodeParser.T__0)
            self.state = 195
            self.match(ZCodeParser.LPAREN)
            self.state = 196
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
            self.state = 198
            self.match(ZCodeParser.T__1)
            self.state = 199
            self.match(ZCodeParser.LPAREN)
            self.state = 200
            self.expr()
            self.state = 201
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
            self.state = 203
            self.match(ZCodeParser.T__2)
            self.state = 204
            self.match(ZCodeParser.LPAREN)
            self.state = 205
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
            self.state = 207
            self.match(ZCodeParser.T__3)
            self.state = 208
            self.match(ZCodeParser.LPAREN)
            self.state = 209
            self.expr()
            self.state = 210
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
            self.state = 212
            self.match(ZCodeParser.T__4)
            self.state = 213
            self.match(ZCodeParser.LPAREN)
            self.state = 214
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
            self.state = 216
            self.match(ZCodeParser.T__5)
            self.state = 217
            self.match(ZCodeParser.LPAREN)
            self.state = 218
            self.expr()
            self.state = 219
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
            self.state = 221
            self.typ()
            self.state = 222
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 223
            self.match(ZCodeParser.LBRACKET)
            self.state = 224
            self.arraydim()
            self.state = 225
            self.match(ZCodeParser.RBRACKET)
            self.state = 226
            self.match(ZCodeParser.ARROW)
            self.state = 227
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
            self.state = 229
            self.match(ZCodeParser.NUMBER_LITERAL)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.COMMA:
                self.state = 230
                self.match(ZCodeParser.COMMA)
                self.state = 231
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 236
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
            self.state = 237
            self.match(ZCodeParser.LBRACKET)
            self.state = 238
            self.arrayelement()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.COMMA:
                self.state = 239
                self.match(ZCodeParser.COMMA)
                self.state = 240
                self.arrayelement()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
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
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.expr()
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
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
            self.state = 252
            self.expr()
            self.state = 253
            self.match(ZCodeParser.ARROW)
            self.state = 254
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
            self.state = 256
            self.match(ZCodeParser.IF)
            self.state = 257
            self.expr()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 258
                self.match(ZCodeParser.NEWLINE)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self.stmt()
            self.state = 265
            self.elifstmt()
            self.state = 266
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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtContext,0)


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
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(ZCodeParser.NEWLINE)
                self.state = 269
                self.match(ZCodeParser.ELIF)
                self.state = 270
                self.expr()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NEWLINE:
                    self.state = 271
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 277
                self.stmt()
                self.state = 278
                self.elifstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

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
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(ZCodeParser.NEWLINE)
                self.state = 284
                self.match(ZCodeParser.ELSE)
                self.state = 285
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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
            self.state = 289
            self.match(ZCodeParser.FOR)
            self.state = 290
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 291
            self.match(ZCodeParser.UNTIL)
            self.state = 292
            self.expr()
            self.state = 293
            self.match(ZCodeParser.BY)
            self.state = 294
            self.expr()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 295
                self.match(ZCodeParser.NEWLINE)


            self.state = 298
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
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.breakstmt()
                pass
            elif token in [ZCodeParser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.continuestmt()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 303
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
            self.state = 306
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
            self.state = 308
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
            self.state = 310
            self.match(ZCodeParser.RETURN)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOL_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 311
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


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ZCodeParser.BEGIN)
            self.state = 315
            self.match(ZCodeParser.NEWLINE)
            self.state = 316
            self.stmt()
            self.state = 321
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 317
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 318
                    self.stmt() 
                self.state = 323
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 324
            self.match(ZCodeParser.NEWLINE)
            self.state = 325
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
        self.enterRule(localctx, 64, self.RULE_funccall)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 328
                self.match(ZCodeParser.LPAREN)
                self.state = 329
                self.paramlist()
                self.state = 330
                self.match(ZCodeParser.RPAREN)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
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
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.expr()
                self.state = 340
                self.match(ZCodeParser.COMMA)
                self.state = 341
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
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
        self.enterRule(localctx, 70, self.RULE_expr)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.expr1()
                self.state = 347
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 348
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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
        self.enterRule(localctx, 72, self.RULE_expr1)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.expr2(0)
                self.state = 354
                self.relationals()
                self.state = 355
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 365
                    self.expr3(0) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 376
                    self.expr4(0) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 387
                    self.expr5() 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        self.enterRule(localctx, 80, self.RULE_expr5)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(ZCodeParser.NOT)
                self.state = 394
                self.expr5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
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
        self.enterRule(localctx, 82, self.RULE_expr6)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.MINUS)
                self.state = 399
                self.expr6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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
        self.enterRule(localctx, 84, self.RULE_expr7)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 403
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 404
                    self.funccall()
                    pass


                self.state = 407
                self.match(ZCodeParser.LBRACKET)
                self.state = 408
                self.expr8()
                self.state = 409
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
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
        self.enterRule(localctx, 86, self.RULE_expr8)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.expr()
                self.state = 415
                self.match(ZCodeParser.COMMA)
                self.state = 416
                self.expr8()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
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
        self.enterRule(localctx, 88, self.RULE_expr9)
        try:
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(ZCodeParser.LPAREN)
                self.state = 423
                self.expr()
                self.state = 424
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 427
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
        self.enterRule(localctx, 90, self.RULE_relationals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
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
        self.enterRule(localctx, 92, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
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
        self.enterRule(localctx, 94, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
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
        self._predicates[37] = self.expr2_sempred
        self._predicates[38] = self.expr3_sempred
        self._predicates[39] = self.expr4_sempred
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
         




