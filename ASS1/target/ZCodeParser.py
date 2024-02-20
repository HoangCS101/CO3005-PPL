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
        buf.write("\u01a7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\6\2l\n\2\r\2\16\2m\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3~\n\3\3\3\7\3")
        buf.write("\u0081\n\3\f\3\16\3\u0084\13\3\3\4\3\4\3\4\5\4\u0089\n")
        buf.write("\4\3\4\3\4\5\4\u008d\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\5\6\u0098\n\6\3\7\3\7\3\7\5\7\u009d\n\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00af\n\13\3\f\3\f\3\f\3\r\3\r\5\r")
        buf.write("\u00b6\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00be\n")
        buf.write("\16\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u00de")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\30\3\30\5\30\u00e6\n\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u00ed\n\31\3\32\3\32\5\32")
        buf.write("\u00f1\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u00fe\n\34\f\34\16\34\u0101\13\34\3")
        buf.write("\34\3\34\5\34\u0105\n\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\5\36\u0112\n\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u011a\n\37\3 \3 \3!\3!\3\"\3\"")
        buf.write("\5\"\u0122\n\"\3#\3#\5#\u0126\n#\3#\7#\u0129\n#\f#\16")
        buf.write("#\u012c\13#\3#\5#\u012f\n#\3#\3#\3$\3$\3$\5$\u0136\n$")
        buf.write("\3%\3%\3%\3%\3&\3&\5&\u013e\n&\3\'\3\'\3\'\3\'\3\'\5\'")
        buf.write("\u0145\n\'\3(\3(\3(\3(\5(\u014b\n(\3)\3)\3)\3)\3)\5)\u0152")
        buf.write("\n)\3*\3*\3*\3*\3*\5*\u0159\n*\3+\3+\3+\3+\3+\3+\7+\u0161")
        buf.write("\n+\f+\16+\u0164\13+\3,\3,\3,\3,\3,\3,\7,\u016c\n,\f,")
        buf.write("\16,\u016f\13,\3-\3-\3-\3-\3-\3-\7-\u0177\n-\f-\16-\u017a")
        buf.write("\13-\3.\3.\3.\5.\u017f\n.\3/\3/\3/\5/\u0184\n/\3\60\3")
        buf.write("\60\5\60\u0188\n\60\3\60\3\60\3\60\3\60\3\60\5\60\u018f")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u0196\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\5\62\u019f\n\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\4\u0082\u012a\5TVX\66\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfh\2\b\3\2%&\3\2\37 \3\2!#\5\2")
        buf.write("\'\')-//\3\2\16\20\3\2\t\13\2\u01ac\2k\3\2\2\2\4}\3\2")
        buf.write("\2\2\6\u0085\3\2\2\2\b\u008e\3\2\2\2\n\u0093\3\2\2\2\f")
        buf.write("\u0099\3\2\2\2\16\u009e\3\2\2\2\20\u00a1\3\2\2\2\22\u00a7")
        buf.write("\3\2\2\2\24\u00ae\3\2\2\2\26\u00b0\3\2\2\2\30\u00b5\3")
        buf.write("\2\2\2\32\u00bd\3\2\2\2\34\u00bf\3\2\2\2\36\u00c1\3\2")
        buf.write("\2\2 \u00c5\3\2\2\2\"\u00c7\3\2\2\2$\u00cb\3\2\2\2&\u00cd")
        buf.write("\3\2\2\2(\u00d1\3\2\2\2*\u00dd\3\2\2\2,\u00df\3\2\2\2")
        buf.write(".\u00e5\3\2\2\2\60\u00ec\3\2\2\2\62\u00f0\3\2\2\2\64\u00f2")
        buf.write("\3\2\2\2\66\u00f6\3\2\2\28\u0106\3\2\2\2:\u010a\3\2\2")
        buf.write("\2<\u0119\3\2\2\2>\u011b\3\2\2\2@\u011d\3\2\2\2B\u011f")
        buf.write("\3\2\2\2D\u0123\3\2\2\2F\u0135\3\2\2\2H\u0137\3\2\2\2")
        buf.write("J\u013d\3\2\2\2L\u0144\3\2\2\2N\u014a\3\2\2\2P\u0151\3")
        buf.write("\2\2\2R\u0158\3\2\2\2T\u015a\3\2\2\2V\u0165\3\2\2\2X\u0170")
        buf.write("\3\2\2\2Z\u017e\3\2\2\2\\\u0183\3\2\2\2^\u018e\3\2\2\2")
        buf.write("`\u0195\3\2\2\2b\u019e\3\2\2\2d\u01a0\3\2\2\2f\u01a2\3")
        buf.write("\2\2\2h\u01a4\3\2\2\2jl\5\4\3\2kj\3\2\2\2lm\3\2\2\2mk")
        buf.write("\3\2\2\2mn\3\2\2\2no\3\2\2\2op\7\2\2\3p\3\3\2\2\2q~\5")
        buf.write("\6\4\2r~\5\b\5\2s~\5\n\6\2t~\5\f\7\2u~\5\32\16\2v~\5F")
        buf.write("$\2w~\5(\25\2x~\5\64\33\2y~\5\66\34\2z~\5:\36\2{~\5<\37")
        buf.write("\2|~\5P)\2}q\3\2\2\2}r\3\2\2\2}s\3\2\2\2}t\3\2\2\2}u\3")
        buf.write("\2\2\2}v\3\2\2\2}w\3\2\2\2}x\3\2\2\2}y\3\2\2\2}z\3\2\2")
        buf.write("\2}{\3\2\2\2}|\3\2\2\2~\u0082\3\2\2\2\177\u0081\7\67\2")
        buf.write("\2\u0080\177\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0083\3")
        buf.write("\2\2\2\u0082\u0080\3\2\2\2\u0083\5\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0085\u0088\5f\64\2\u0086\u0089\7\65\2\2\u0087")
        buf.write("\u0089\5^\60\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2")
        buf.write("\u0089\u008c\3\2\2\2\u008a\u008b\7(\2\2\u008b\u008d\5")
        buf.write("P)\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\7\3")
        buf.write("\2\2\2\u008e\u008f\7\22\2\2\u008f\u0090\7\65\2\2\u0090")
        buf.write("\u0091\7(\2\2\u0091\u0092\5P)\2\u0092\t\3\2\2\2\u0093")
        buf.write("\u0094\7\23\2\2\u0094\u0097\7\65\2\2\u0095\u0096\7(\2")
        buf.write("\2\u0096\u0098\5P)\2\u0097\u0095\3\2\2\2\u0097\u0098\3")
        buf.write("\2\2\2\u0098\13\3\2\2\2\u0099\u009a\7\24\2\2\u009a\u009c")
        buf.write("\5\16\b\2\u009b\u009d\5\30\r\2\u009c\u009b\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\r\3\2\2\2\u009e\u009f\7\65\2\2\u009f")
        buf.write("\u00a0\5\20\t\2\u00a0\17\3\2\2\2\u00a1\u00a2\7\61\2\2")
        buf.write("\u00a2\u00a3\5\22\n\2\u00a3\u00a4\7\62\2\2\u00a4\21\3")
        buf.write("\2\2\2\u00a5\u00a8\5\24\13\2\u00a6\u00a8\3\2\2\2\u00a7")
        buf.write("\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\23\3\2\2\2\u00a9")
        buf.write("\u00aa\5\26\f\2\u00aa\u00ab\7\60\2\2\u00ab\u00ac\5\24")
        buf.write("\13\2\u00ac\u00af\3\2\2\2\u00ad\u00af\5\26\f\2\u00ae\u00a9")
        buf.write("\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\25\3\2\2\2\u00b0\u00b1")
        buf.write("\5f\64\2\u00b1\u00b2\5P)\2\u00b2\27\3\2\2\2\u00b3\u00b6")
        buf.write("\5B\"\2\u00b4\u00b6\5D#\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b6\31\3\2\2\2\u00b7\u00be\5\34\17\2\u00b8")
        buf.write("\u00be\5\36\20\2\u00b9\u00be\5 \21\2\u00ba\u00be\5\"\22")
        buf.write("\2\u00bb\u00be\5$\23\2\u00bc\u00be\5&\24\2\u00bd\u00b7")
        buf.write("\3\2\2\2\u00bd\u00b8\3\2\2\2\u00bd\u00b9\3\2\2\2\u00bd")
        buf.write("\u00ba\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be\33\3\2\2\2\u00bf\u00c0\7\3\2\2\u00c0\35\3\2\2\2")
        buf.write("\u00c1\u00c2\7\4\2\2\u00c2\u00c3\5P)\2\u00c3\u00c4\7\62")
        buf.write("\2\2\u00c4\37\3\2\2\2\u00c5\u00c6\7\5\2\2\u00c6!\3\2\2")
        buf.write("\2\u00c7\u00c8\7\6\2\2\u00c8\u00c9\5P)\2\u00c9\u00ca\7")
        buf.write("\62\2\2\u00ca#\3\2\2\2\u00cb\u00cc\7\7\2\2\u00cc%\3\2")
        buf.write("\2\2\u00cd\u00ce\7\b\2\2\u00ce\u00cf\5P)\2\u00cf\u00d0")
        buf.write("\7\62\2\2\u00d0\'\3\2\2\2\u00d1\u00d2\5f\64\2\u00d2\u00d3")
        buf.write("\7\65\2\2\u00d3\u00d4\7\63\2\2\u00d4\u00d5\5*\26\2\u00d5")
        buf.write("\u00d6\7\64\2\2\u00d6\u00d7\7(\2\2\u00d7\u00d8\5,\27\2")
        buf.write("\u00d8)\3\2\2\2\u00d9\u00da\7\t\2\2\u00da\u00db\7\60\2")
        buf.write("\2\u00db\u00de\5*\26\2\u00dc\u00de\7\t\2\2\u00dd\u00d9")
        buf.write("\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de+\3\2\2\2\u00df\u00e0")
        buf.write("\7\63\2\2\u00e0\u00e1\5.\30\2\u00e1\u00e2\7\64\2\2\u00e2")
        buf.write("-\3\2\2\2\u00e3\u00e6\5\60\31\2\u00e4\u00e6\3\2\2\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e5\u00e4\3\2\2\2\u00e6/\3\2\2\2\u00e7")
        buf.write("\u00e8\5\62\32\2\u00e8\u00e9\7\60\2\2\u00e9\u00ea\5\60")
        buf.write("\31\2\u00ea\u00ed\3\2\2\2\u00eb\u00ed\5\62\32\2\u00ec")
        buf.write("\u00e7\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\61\3\2\2\2\u00ee")
        buf.write("\u00f1\5h\65\2\u00ef\u00f1\5,\27\2\u00f0\u00ee\3\2\2\2")
        buf.write("\u00f0\u00ef\3\2\2\2\u00f1\63\3\2\2\2\u00f2\u00f3\5P)")
        buf.write("\2\u00f3\u00f4\7(\2\2\u00f4\u00f5\5P)\2\u00f5\65\3\2\2")
        buf.write("\2\u00f6\u00f7\7\32\2\2\u00f7\u00f8\58\35\2\u00f8\u0104")
        buf.write("\5\4\3\2\u00f9\u00fa\7\34\2\2\u00fa\u00fb\58\35\2\u00fb")
        buf.write("\u00fc\5\4\3\2\u00fc\u00fe\3\2\2\2\u00fd\u00f9\3\2\2\2")
        buf.write("\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3")
        buf.write("\2\2\2\u0100\u0102\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0103")
        buf.write("\7\33\2\2\u0103\u0105\5\4\3\2\u0104\u00ff\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\67\3\2\2\2\u0106\u0107\7\61\2\2\u0107")
        buf.write("\u0108\5P)\2\u0108\u0109\7\62\2\2\u01099\3\2\2\2\u010a")
        buf.write("\u010b\7\25\2\2\u010b\u010c\7\65\2\2\u010c\u010d\7\26")
        buf.write("\2\2\u010d\u010e\5P)\2\u010e\u010f\7\27\2\2\u010f\u0111")
        buf.write("\5P)\2\u0110\u0112\7\67\2\2\u0111\u0110\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\5\4\3\2")
        buf.write("\u0114;\3\2\2\2\u0115\u011a\5> \2\u0116\u011a\5@!\2\u0117")
        buf.write("\u011a\5B\"\2\u0118\u011a\5D#\2\u0119\u0115\3\2\2\2\u0119")
        buf.write("\u0116\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u0118\3\2\2\2")
        buf.write("\u011a=\3\2\2\2\u011b\u011c\7\30\2\2\u011c?\3\2\2\2\u011d")
        buf.write("\u011e\7\31\2\2\u011eA\3\2\2\2\u011f\u0121\7\21\2\2\u0120")
        buf.write("\u0122\5P)\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122")
        buf.write("C\3\2\2\2\u0123\u0125\7\35\2\2\u0124\u0126\7\67\2\2\u0125")
        buf.write("\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u012a\3\2\2\2")
        buf.write("\u0127\u0129\5\4\3\2\u0128\u0127\3\2\2\2\u0129\u012c\3")
        buf.write("\2\2\2\u012a\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012b\u012e")
        buf.write("\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u012f\7\67\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\3\2\2\2")
        buf.write("\u0130\u0131\7\36\2\2\u0131E\3\2\2\2\u0132\u0133\7\65")
        buf.write("\2\2\u0133\u0136\5H%\2\u0134\u0136\5\32\16\2\u0135\u0132")
        buf.write("\3\2\2\2\u0135\u0134\3\2\2\2\u0136G\3\2\2\2\u0137\u0138")
        buf.write("\7\61\2\2\u0138\u0139\5J&\2\u0139\u013a\7\62\2\2\u013a")
        buf.write("I\3\2\2\2\u013b\u013e\5L\'\2\u013c\u013e\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013eK\3\2\2\2\u013f")
        buf.write("\u0140\5N(\2\u0140\u0141\7\60\2\2\u0141\u0142\5L\'\2\u0142")
        buf.write("\u0145\3\2\2\2\u0143\u0145\5N(\2\u0144\u013f\3\2\2\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145M\3\2\2\2\u0146\u014b\5h\65\2\u0147")
        buf.write("\u014b\5F$\2\u0148\u014b\7\65\2\2\u0149\u014b\5P)\2\u014a")
        buf.write("\u0146\3\2\2\2\u014a\u0147\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u0149\3\2\2\2\u014bO\3\2\2\2\u014c\u014d\5R*\2")
        buf.write("\u014d\u014e\7.\2\2\u014e\u014f\5R*\2\u014f\u0152\3\2")
        buf.write("\2\2\u0150\u0152\5R*\2\u0151\u014c\3\2\2\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152Q\3\2\2\2\u0153\u0154\5T+\2\u0154\u0155")
        buf.write("\5d\63\2\u0155\u0156\5T+\2\u0156\u0159\3\2\2\2\u0157\u0159")
        buf.write("\5T+\2\u0158\u0153\3\2\2\2\u0158\u0157\3\2\2\2\u0159S")
        buf.write("\3\2\2\2\u015a\u015b\b+\1\2\u015b\u015c\5V,\2\u015c\u0162")
        buf.write("\3\2\2\2\u015d\u015e\f\4\2\2\u015e\u015f\t\2\2\2\u015f")
        buf.write("\u0161\5V,\2\u0160\u015d\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163U\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0165\u0166\b,\1\2\u0166\u0167\5X-\2\u0167")
        buf.write("\u016d\3\2\2\2\u0168\u0169\f\4\2\2\u0169\u016a\t\3\2\2")
        buf.write("\u016a\u016c\5X-\2\u016b\u0168\3\2\2\2\u016c\u016f\3\2")
        buf.write("\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016eW\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\b-\1\2\u0171\u0172")
        buf.write("\5Z.\2\u0172\u0178\3\2\2\2\u0173\u0174\f\4\2\2\u0174\u0175")
        buf.write("\t\4\2\2\u0175\u0177\5Z.\2\u0176\u0173\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("Y\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\7$\2\2\u017c")
        buf.write("\u017f\5Z.\2\u017d\u017f\5\\/\2\u017e\u017b\3\2\2\2\u017e")
        buf.write("\u017d\3\2\2\2\u017f[\3\2\2\2\u0180\u0181\7 \2\2\u0181")
        buf.write("\u0184\5\\/\2\u0182\u0184\5^\60\2\u0183\u0180\3\2\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184]\3\2\2\2\u0185\u0188\7\65\2")
        buf.write("\2\u0186\u0188\5F$\2\u0187\u0185\3\2\2\2\u0187\u0186\3")
        buf.write("\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7\63\2\2\u018a")
        buf.write("\u018b\5`\61\2\u018b\u018c\7\64\2\2\u018c\u018f\3\2\2")
        buf.write("\2\u018d\u018f\5b\62\2\u018e\u0187\3\2\2\2\u018e\u018d")
        buf.write("\3\2\2\2\u018f_\3\2\2\2\u0190\u0191\5P)\2\u0191\u0192")
        buf.write("\7\60\2\2\u0192\u0193\5`\61\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0196\5P)\2\u0195\u0190\3\2\2\2\u0195\u0194\3\2\2\2\u0196")
        buf.write("a\3\2\2\2\u0197\u019f\5h\65\2\u0198\u0199\7\61\2\2\u0199")
        buf.write("\u019a\5P)\2\u019a\u019b\7\62\2\2\u019b\u019f\3\2\2\2")
        buf.write("\u019c\u019f\5F$\2\u019d\u019f\7\65\2\2\u019e\u0197\3")
        buf.write("\2\2\2\u019e\u0198\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019fc\3\2\2\2\u01a0\u01a1\t\5\2\2\u01a1e\3\2")
        buf.write("\2\2\u01a2\u01a3\t\6\2\2\u01a3g\3\2\2\2\u01a4\u01a5\t")
        buf.write("\7\2\2\u01a5i\3\2\2\2(m}\u0082\u0088\u008c\u0097\u009c")
        buf.write("\u00a7\u00ae\u00b5\u00bd\u00dd\u00e5\u00ec\u00f0\u00ff")
        buf.write("\u0104\u0111\u0119\u0121\u0125\u012a\u012e\u0135\u013d")
        buf.write("\u0144\u014a\u0151\u0158\u0162\u016d\u0178\u017e\u0183")
        buf.write("\u0187\u018e\u0195\u019e")
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
    RULE_func = 6
    RULE_arg = 7
    RULE_arglist = 8
    RULE_argprime = 9
    RULE_argment = 10
    RULE_funcend = 11
    RULE_builtin = 12
    RULE_readnum = 13
    RULE_writenum = 14
    RULE_readbool = 15
    RULE_writebool = 16
    RULE_readstr = 17
    RULE_writestr = 18
    RULE_arraydecl = 19
    RULE_arraydim = 20
    RULE_array = 21
    RULE_arraylist = 22
    RULE_arrayobj = 23
    RULE_arrayelement = 24
    RULE_assignstmt = 25
    RULE_ifstmt = 26
    RULE_ifexpr = 27
    RULE_forstmt = 28
    RULE_otherstmt = 29
    RULE_breakstmt = 30
    RULE_continuestmt = 31
    RULE_returnstmt = 32
    RULE_blockstmt = 33
    RULE_funccall = 34
    RULE_paramdecl = 35
    RULE_paramlist = 36
    RULE_paramprime = 37
    RULE_param = 38
    RULE_expr = 39
    RULE_expr1 = 40
    RULE_expr2 = 41
    RULE_expr3 = 42
    RULE_expr4 = 43
    RULE_expr5 = 44
    RULE_expr6 = 45
    RULE_expr7 = 46
    RULE_idxop = 47
    RULE_expr9 = 48
    RULE_relationals = 49
    RULE_typ = 50
    RULE_literals = 51

    ruleNames =  [ "program", "stmt", "vardecl", "im_vardecl", "im_dydecl", 
                   "funcdecl", "func", "arg", "arglist", "argprime", "argment", 
                   "funcend", "builtin", "readnum", "writenum", "readbool", 
                   "writebool", "readstr", "writestr", "arraydecl", "arraydim", 
                   "array", "arraylist", "arrayobj", "arrayelement", "assignstmt", 
                   "ifstmt", "ifexpr", "forstmt", "otherstmt", "breakstmt", 
                   "continuestmt", "returnstmt", "blockstmt", "funccall", 
                   "paramdecl", "paramlist", "paramprime", "param", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "idxop", "expr9", "relationals", "typ", "literals" ]

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
            self.state = 105 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 104
                self.stmt()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.T__5) | (1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.BOOL_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.IDENTIFIER))) != 0)):
                    break

            self.state = 109
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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 111
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 112
                self.im_vardecl()
                pass

            elif la_ == 3:
                self.state = 113
                self.im_dydecl()
                pass

            elif la_ == 4:
                self.state = 114
                self.funcdecl()
                pass

            elif la_ == 5:
                self.state = 115
                self.builtin()
                pass

            elif la_ == 6:
                self.state = 116
                self.funccall()
                pass

            elif la_ == 7:
                self.state = 117
                self.arraydecl()
                pass

            elif la_ == 8:
                self.state = 118
                self.assignstmt()
                pass

            elif la_ == 9:
                self.state = 119
                self.ifstmt()
                pass

            elif la_ == 10:
                self.state = 120
                self.forstmt()
                pass

            elif la_ == 11:
                self.state = 121
                self.otherstmt()
                pass

            elif la_ == 12:
                self.state = 122
                self.expr()
                pass


            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 125
                    self.match(ZCodeParser.NEWLINE) 
                self.state = 130
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
            self.state = 131
            self.typ()
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 132
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 133
                self.expr7()
                pass


            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 136
                self.match(ZCodeParser.ARROW)
                self.state = 137
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
            self.state = 140
            self.match(ZCodeParser.VAR)
            self.state = 141
            self.match(ZCodeParser.IDENTIFIER)
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
            self.state = 145
            self.match(ZCodeParser.DYNAMIC)
            self.state = 146
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ARROW:
                self.state = 147
                self.match(ZCodeParser.ARROW)
                self.state = 148
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

        def func(self):
            return self.getTypedRuleContext(ZCodeParser.FuncContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(ZCodeParser.FUNC)
            self.state = 152
            self.func()
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 153
                self.funcend()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 157
            self.arg()
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
        self.enterRule(localctx, 14, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZCodeParser.LPAREN)
            self.state = 160
            self.arglist()
            self.state = 161
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
        self.enterRule(localctx, 16, self.RULE_arglist)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
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
        self.enterRule(localctx, 18, self.RULE_argprime)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.argment()
                self.state = 168
                self.match(ZCodeParser.COMMA)
                self.state = 169
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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
        self.enterRule(localctx, 20, self.RULE_argment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.typ()
            self.state = 175
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
        self.enterRule(localctx, 22, self.RULE_funcend)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.returnstmt()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
        self.enterRule(localctx, 24, self.RULE_builtin)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.readnum()
                pass
            elif token in [ZCodeParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.writenum()
                pass
            elif token in [ZCodeParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.readbool()
                pass
            elif token in [ZCodeParser.T__3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.writebool()
                pass
            elif token in [ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 185
                self.readstr()
                pass
            elif token in [ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 186
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
        self.enterRule(localctx, 26, self.RULE_readnum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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
        self.enterRule(localctx, 28, self.RULE_writenum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(ZCodeParser.T__1)
            self.state = 192
            self.expr()
            self.state = 193
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
        self.enterRule(localctx, 30, self.RULE_readbool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 32, self.RULE_writebool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ZCodeParser.T__3)
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_readstr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadstr" ):
                return visitor.visitReadstr(self)
            else:
                return visitor.visitChildren(self)




    def readstr(self):

        localctx = ZCodeParser.ReadstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_readstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
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
        self.enterRule(localctx, 36, self.RULE_writestr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(ZCodeParser.T__5)
            self.state = 204
            self.expr()
            self.state = 205
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
        self.enterRule(localctx, 38, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.typ()
            self.state = 208
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 209
            self.match(ZCodeParser.LBRACKET)
            self.state = 210
            self.arraydim()
            self.state = 211
            self.match(ZCodeParser.RBRACKET)
            self.state = 212
            self.match(ZCodeParser.ARROW)
            self.state = 213
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
        self.enterRule(localctx, 40, self.RULE_arraydim)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 216
                self.match(ZCodeParser.COMMA)
                self.state = 217
                self.arraydim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
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
        self.enterRule(localctx, 42, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(ZCodeParser.LBRACKET)
            self.state = 222
            self.arraylist()
            self.state = 223
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

        def arrayobj(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayobjContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraylist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylist" ):
                return visitor.visitArraylist(self)
            else:
                return visitor.visitChildren(self)




    def arraylist(self):

        localctx = ZCodeParser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arraylist)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.arrayobj()
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


    class ArrayobjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayelement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayelementContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrayobj(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayobjContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayobj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayobj" ):
                return visitor.visitArrayobj(self)
            else:
                return visitor.visitChildren(self)




    def arrayobj(self):

        localctx = ZCodeParser.ArrayobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arrayobj)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.arrayelement()
                self.state = 230
                self.match(ZCodeParser.COMMA)
                self.state = 231
                self.arrayobj()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.arrayelement()
                pass


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
        self.enterRule(localctx, 48, self.RULE_arrayelement)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.literals()
                pass
            elif token in [ZCodeParser.LBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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
        self.enterRule(localctx, 50, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expr()
            self.state = 241
            self.match(ZCodeParser.ARROW)
            self.state = 242
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

        def ifexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IfexprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IfexprContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF)
            else:
                return self.getToken(ZCodeParser.ELIF, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ZCodeParser.IF)
            self.state = 245
            self.ifexpr()
            self.state = 246
            self.stmt()
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.ELIF:
                    self.state = 247
                    self.match(ZCodeParser.ELIF)
                    self.state = 248
                    self.ifexpr()
                    self.state = 249
                    self.stmt()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
                self.match(ZCodeParser.ELSE)
                self.state = 257
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfexprContext(ParserRuleContext):
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
            return ZCodeParser.RULE_ifexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfexpr" ):
                return visitor.visitIfexpr(self)
            else:
                return visitor.visitChildren(self)




    def ifexpr(self):

        localctx = ZCodeParser.IfexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(ZCodeParser.LPAREN)
            self.state = 261
            self.expr()
            self.state = 262
            self.match(ZCodeParser.RPAREN)
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
        self.enterRule(localctx, 56, self.RULE_forstmt)
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
        self.enterRule(localctx, 58, self.RULE_otherstmt)
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
        self.enterRule(localctx, 60, self.RULE_breakstmt)
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
        self.enterRule(localctx, 62, self.RULE_continuestmt)
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
        self.enterRule(localctx, 64, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ZCodeParser.RETURN)
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
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
        self.enterRule(localctx, 66, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.BEGIN)
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 290
                self.match(ZCodeParser.NEWLINE)


            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 293
                    self.stmt() 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def paramdecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamdeclContext,0)


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
        self.enterRule(localctx, 68, self.RULE_funccall)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 305
                self.paramdecl()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
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


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(ZCodeParser.LPAREN)
            self.state = 310
            self.paramlist()
            self.state = 311
            self.match(ZCodeParser.RPAREN)
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
        self.enterRule(localctx, 72, self.RULE_paramlist)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.NOT, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
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
        self.enterRule(localctx, 74, self.RULE_paramprime)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.param()
                self.state = 318
                self.match(ZCodeParser.COMMA)
                self.state = 319
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
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
        self.enterRule(localctx, 76, self.RULE_param)
        try:
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.funccall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 327
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
        self.enterRule(localctx, 78, self.RULE_expr)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.expr1()
                self.state = 331
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 332
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
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
        self.enterRule(localctx, 80, self.RULE_expr1)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.expr2(0)
                self.state = 338
                self.relationals()
                self.state = 339
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 352
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 347
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 348
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 349
                    self.expr3(0) 
                self.state = 354
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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 363
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 358
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 359
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 360
                    self.expr4(0) 
                self.state = 365
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 371
                    self.expr5() 
                self.state = 376
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
        self.enterRule(localctx, 88, self.RULE_expr5)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(ZCodeParser.NOT)
                self.state = 378
                self.expr5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.MINUS, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
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
        self.enterRule(localctx, 90, self.RULE_expr6)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(ZCodeParser.MINUS)
                self.state = 383
                self.expr6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.T__5, ZCodeParser.NUMBER_LITERAL, ZCodeParser.BOOL_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.LPAREN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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

        def idxop(self):
            return self.getTypedRuleContext(ZCodeParser.IdxopContext,0)


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
        self.enterRule(localctx, 92, self.RULE_expr7)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 387
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 388
                    self.funccall()
                    pass


                self.state = 391
                self.match(ZCodeParser.LBRACKET)
                self.state = 392
                self.idxop()
                self.state = 393
                self.match(ZCodeParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def idxop(self):
            return self.getTypedRuleContext(ZCodeParser.IdxopContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_idxop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxop" ):
                return visitor.visitIdxop(self)
            else:
                return visitor.visitChildren(self)




    def idxop(self):

        localctx = ZCodeParser.IdxopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_idxop)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.expr()
                self.state = 399
                self.match(ZCodeParser.COMMA)
                self.state = 400
                self.idxop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
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
        self.enterRule(localctx, 96, self.RULE_expr9)
        try:
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.match(ZCodeParser.LPAREN)
                self.state = 407
                self.expr()
                self.state = 408
                self.match(ZCodeParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 410
                self.funccall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 411
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
        self.enterRule(localctx, 98, self.RULE_relationals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
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
        self.enterRule(localctx, 100, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
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
        self.enterRule(localctx, 102, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
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
        self._predicates[41] = self.expr2_sempred
        self._predicates[42] = self.expr3_sempred
        self._predicates[43] = self.expr4_sempred
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
         




