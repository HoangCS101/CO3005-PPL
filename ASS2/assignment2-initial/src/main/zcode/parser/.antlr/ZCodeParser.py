# Generated from d:/232/PPL/ASSignments/CO3005-PPL/ASS2/assignment2-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,57,420,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,1,0,4,0,106,
        8,0,11,0,12,0,107,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,124,8,1,1,1,4,1,127,8,1,11,1,12,1,128,1,2,1,2,1,2,
        3,2,134,8,2,1,2,1,2,3,2,138,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,3,4,149,8,4,1,5,1,5,1,5,3,5,154,8,5,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,8,1,8,3,8,165,8,8,1,9,1,9,1,9,1,9,1,9,3,9,172,8,9,1,10,1,10,
        1,10,1,11,1,11,3,11,179,8,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        187,8,12,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,
        1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,3,20,219,8,20,1,21,1,21,1,21,1,21,
        1,22,1,22,3,22,227,8,22,1,23,1,23,1,23,1,23,1,23,3,23,234,8,23,1,
        24,1,24,3,24,238,8,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,5,26,251,8,26,10,26,12,26,254,9,26,1,26,1,26,3,26,258,
        8,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,
        271,8,28,1,28,1,28,1,29,1,29,1,29,1,29,3,29,279,8,29,1,30,1,30,1,
        31,1,31,1,32,1,32,3,32,287,8,32,1,33,1,33,3,33,291,8,33,1,33,5,33,
        294,8,33,10,33,12,33,297,9,33,1,33,3,33,300,8,33,1,33,1,33,1,34,
        1,34,1,34,3,34,307,8,34,1,35,1,35,1,35,1,35,1,36,1,36,3,36,315,8,
        36,1,37,1,37,1,37,1,37,1,37,3,37,322,8,37,1,38,1,38,1,38,1,38,3,
        38,328,8,38,1,39,1,39,1,39,1,39,1,39,3,39,335,8,39,1,40,1,40,1,40,
        1,40,1,40,3,40,342,8,40,1,41,1,41,1,41,1,41,1,41,1,41,5,41,350,8,
        41,10,41,12,41,353,9,41,1,42,1,42,1,42,1,42,1,42,1,42,5,42,361,8,
        42,10,42,12,42,364,9,42,1,43,1,43,1,43,1,43,1,43,1,43,5,43,372,8,
        43,10,43,12,43,375,9,43,1,44,1,44,1,44,3,44,380,8,44,1,45,1,45,1,
        45,3,45,385,8,45,1,46,1,46,3,46,389,8,46,1,46,1,46,1,46,1,46,1,46,
        3,46,396,8,46,1,47,1,47,1,47,1,47,1,47,3,47,403,8,47,1,48,1,48,1,
        48,1,48,1,48,1,48,1,48,3,48,412,8,48,1,49,1,49,1,50,1,50,1,51,1,
        51,1,51,1,295,3,82,84,86,52,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,0,6,1,0,35,36,
        1,0,29,30,1,0,31,33,3,0,37,37,39,43,45,45,1,0,12,14,1,0,7,9,425,
        0,105,1,0,0,0,2,123,1,0,0,0,4,130,1,0,0,0,6,139,1,0,0,0,8,144,1,
        0,0,0,10,150,1,0,0,0,12,155,1,0,0,0,14,158,1,0,0,0,16,164,1,0,0,
        0,18,171,1,0,0,0,20,173,1,0,0,0,22,178,1,0,0,0,24,186,1,0,0,0,26,
        188,1,0,0,0,28,190,1,0,0,0,30,194,1,0,0,0,32,196,1,0,0,0,34,200,
        1,0,0,0,36,202,1,0,0,0,38,206,1,0,0,0,40,218,1,0,0,0,42,220,1,0,
        0,0,44,226,1,0,0,0,46,233,1,0,0,0,48,237,1,0,0,0,50,239,1,0,0,0,
        52,243,1,0,0,0,54,259,1,0,0,0,56,263,1,0,0,0,58,278,1,0,0,0,60,280,
        1,0,0,0,62,282,1,0,0,0,64,284,1,0,0,0,66,288,1,0,0,0,68,306,1,0,
        0,0,70,308,1,0,0,0,72,314,1,0,0,0,74,321,1,0,0,0,76,327,1,0,0,0,
        78,334,1,0,0,0,80,341,1,0,0,0,82,343,1,0,0,0,84,354,1,0,0,0,86,365,
        1,0,0,0,88,379,1,0,0,0,90,384,1,0,0,0,92,395,1,0,0,0,94,402,1,0,
        0,0,96,411,1,0,0,0,98,413,1,0,0,0,100,415,1,0,0,0,102,417,1,0,0,
        0,104,106,3,2,1,0,105,104,1,0,0,0,106,107,1,0,0,0,107,105,1,0,0,
        0,107,108,1,0,0,0,108,109,1,0,0,0,109,110,5,0,0,1,110,1,1,0,0,0,
        111,124,3,4,2,0,112,124,3,6,3,0,113,124,3,8,4,0,114,124,3,10,5,0,
        115,124,3,24,12,0,116,124,3,68,34,0,117,124,3,38,19,0,118,124,3,
        50,25,0,119,124,3,52,26,0,120,124,3,56,28,0,121,124,3,58,29,0,122,
        124,3,78,39,0,123,111,1,0,0,0,123,112,1,0,0,0,123,113,1,0,0,0,123,
        114,1,0,0,0,123,115,1,0,0,0,123,116,1,0,0,0,123,117,1,0,0,0,123,
        118,1,0,0,0,123,119,1,0,0,0,123,120,1,0,0,0,123,121,1,0,0,0,123,
        122,1,0,0,0,124,126,1,0,0,0,125,127,5,53,0,0,126,125,1,0,0,0,127,
        128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,3,1,0,0,0,130,133,
        3,100,50,0,131,134,5,51,0,0,132,134,3,92,46,0,133,131,1,0,0,0,133,
        132,1,0,0,0,134,137,1,0,0,0,135,136,5,38,0,0,136,138,3,78,39,0,137,
        135,1,0,0,0,137,138,1,0,0,0,138,5,1,0,0,0,139,140,5,16,0,0,140,141,
        5,51,0,0,141,142,5,38,0,0,142,143,3,78,39,0,143,7,1,0,0,0,144,145,
        5,17,0,0,145,148,5,51,0,0,146,147,5,38,0,0,147,149,3,78,39,0,148,
        146,1,0,0,0,148,149,1,0,0,0,149,9,1,0,0,0,150,151,5,18,0,0,151,153,
        3,12,6,0,152,154,3,22,11,0,153,152,1,0,0,0,153,154,1,0,0,0,154,11,
        1,0,0,0,155,156,5,51,0,0,156,157,3,14,7,0,157,13,1,0,0,0,158,159,
        5,47,0,0,159,160,3,16,8,0,160,161,5,48,0,0,161,15,1,0,0,0,162,165,
        3,18,9,0,163,165,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,17,
        1,0,0,0,166,167,3,20,10,0,167,168,5,46,0,0,168,169,3,18,9,0,169,
        172,1,0,0,0,170,172,3,20,10,0,171,166,1,0,0,0,171,170,1,0,0,0,172,
        19,1,0,0,0,173,174,3,100,50,0,174,175,3,78,39,0,175,21,1,0,0,0,176,
        179,3,64,32,0,177,179,3,66,33,0,178,176,1,0,0,0,178,177,1,0,0,0,
        179,23,1,0,0,0,180,187,3,26,13,0,181,187,3,28,14,0,182,187,3,30,
        15,0,183,187,3,32,16,0,184,187,3,34,17,0,185,187,3,36,18,0,186,180,
        1,0,0,0,186,181,1,0,0,0,186,182,1,0,0,0,186,183,1,0,0,0,186,184,
        1,0,0,0,186,185,1,0,0,0,187,25,1,0,0,0,188,189,5,1,0,0,189,27,1,
        0,0,0,190,191,5,2,0,0,191,192,3,78,39,0,192,193,5,48,0,0,193,29,
        1,0,0,0,194,195,5,3,0,0,195,31,1,0,0,0,196,197,5,4,0,0,197,198,3,
        78,39,0,198,199,5,48,0,0,199,33,1,0,0,0,200,201,5,5,0,0,201,35,1,
        0,0,0,202,203,5,6,0,0,203,204,3,78,39,0,204,205,5,48,0,0,205,37,
        1,0,0,0,206,207,3,100,50,0,207,208,5,51,0,0,208,209,5,49,0,0,209,
        210,3,40,20,0,210,211,5,50,0,0,211,212,5,38,0,0,212,213,3,42,21,
        0,213,39,1,0,0,0,214,215,5,7,0,0,215,216,5,46,0,0,216,219,3,40,20,
        0,217,219,5,7,0,0,218,214,1,0,0,0,218,217,1,0,0,0,219,41,1,0,0,0,
        220,221,5,49,0,0,221,222,3,44,22,0,222,223,5,50,0,0,223,43,1,0,0,
        0,224,227,3,46,23,0,225,227,1,0,0,0,226,224,1,0,0,0,226,225,1,0,
        0,0,227,45,1,0,0,0,228,229,3,48,24,0,229,230,5,46,0,0,230,231,3,
        46,23,0,231,234,1,0,0,0,232,234,3,48,24,0,233,228,1,0,0,0,233,232,
        1,0,0,0,234,47,1,0,0,0,235,238,3,102,51,0,236,238,3,42,21,0,237,
        235,1,0,0,0,237,236,1,0,0,0,238,49,1,0,0,0,239,240,3,78,39,0,240,
        241,5,38,0,0,241,242,3,78,39,0,242,51,1,0,0,0,243,244,5,24,0,0,244,
        245,3,54,27,0,245,257,3,2,1,0,246,247,5,26,0,0,247,248,3,54,27,0,
        248,249,3,2,1,0,249,251,1,0,0,0,250,246,1,0,0,0,251,254,1,0,0,0,
        252,250,1,0,0,0,252,253,1,0,0,0,253,255,1,0,0,0,254,252,1,0,0,0,
        255,256,5,25,0,0,256,258,3,2,1,0,257,252,1,0,0,0,257,258,1,0,0,0,
        258,53,1,0,0,0,259,260,5,47,0,0,260,261,3,78,39,0,261,262,5,48,0,
        0,262,55,1,0,0,0,263,264,5,19,0,0,264,265,5,51,0,0,265,266,5,20,
        0,0,266,267,3,78,39,0,267,268,5,21,0,0,268,270,3,78,39,0,269,271,
        5,53,0,0,270,269,1,0,0,0,270,271,1,0,0,0,271,272,1,0,0,0,272,273,
        3,2,1,0,273,57,1,0,0,0,274,279,3,60,30,0,275,279,3,62,31,0,276,279,
        3,64,32,0,277,279,3,66,33,0,278,274,1,0,0,0,278,275,1,0,0,0,278,
        276,1,0,0,0,278,277,1,0,0,0,279,59,1,0,0,0,280,281,5,22,0,0,281,
        61,1,0,0,0,282,283,5,23,0,0,283,63,1,0,0,0,284,286,5,15,0,0,285,
        287,3,78,39,0,286,285,1,0,0,0,286,287,1,0,0,0,287,65,1,0,0,0,288,
        290,5,27,0,0,289,291,5,53,0,0,290,289,1,0,0,0,290,291,1,0,0,0,291,
        295,1,0,0,0,292,294,3,2,1,0,293,292,1,0,0,0,294,297,1,0,0,0,295,
        296,1,0,0,0,295,293,1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,298,
        300,5,53,0,0,299,298,1,0,0,0,299,300,1,0,0,0,300,301,1,0,0,0,301,
        302,5,28,0,0,302,67,1,0,0,0,303,304,5,51,0,0,304,307,3,70,35,0,305,
        307,3,24,12,0,306,303,1,0,0,0,306,305,1,0,0,0,307,69,1,0,0,0,308,
        309,5,47,0,0,309,310,3,72,36,0,310,311,5,48,0,0,311,71,1,0,0,0,312,
        315,3,74,37,0,313,315,1,0,0,0,314,312,1,0,0,0,314,313,1,0,0,0,315,
        73,1,0,0,0,316,317,3,76,38,0,317,318,5,46,0,0,318,319,3,74,37,0,
        319,322,1,0,0,0,320,322,3,76,38,0,321,316,1,0,0,0,321,320,1,0,0,
        0,322,75,1,0,0,0,323,328,3,102,51,0,324,328,3,68,34,0,325,328,5,
        51,0,0,326,328,3,78,39,0,327,323,1,0,0,0,327,324,1,0,0,0,327,325,
        1,0,0,0,327,326,1,0,0,0,328,77,1,0,0,0,329,330,3,80,40,0,330,331,
        5,44,0,0,331,332,3,80,40,0,332,335,1,0,0,0,333,335,3,80,40,0,334,
        329,1,0,0,0,334,333,1,0,0,0,335,79,1,0,0,0,336,337,3,82,41,0,337,
        338,3,98,49,0,338,339,3,82,41,0,339,342,1,0,0,0,340,342,3,82,41,
        0,341,336,1,0,0,0,341,340,1,0,0,0,342,81,1,0,0,0,343,344,6,41,-1,
        0,344,345,3,84,42,0,345,351,1,0,0,0,346,347,10,2,0,0,347,348,7,0,
        0,0,348,350,3,84,42,0,349,346,1,0,0,0,350,353,1,0,0,0,351,349,1,
        0,0,0,351,352,1,0,0,0,352,83,1,0,0,0,353,351,1,0,0,0,354,355,6,42,
        -1,0,355,356,3,86,43,0,356,362,1,0,0,0,357,358,10,2,0,0,358,359,
        7,1,0,0,359,361,3,86,43,0,360,357,1,0,0,0,361,364,1,0,0,0,362,360,
        1,0,0,0,362,363,1,0,0,0,363,85,1,0,0,0,364,362,1,0,0,0,365,366,6,
        43,-1,0,366,367,3,88,44,0,367,373,1,0,0,0,368,369,10,2,0,0,369,370,
        7,2,0,0,370,372,3,88,44,0,371,368,1,0,0,0,372,375,1,0,0,0,373,371,
        1,0,0,0,373,374,1,0,0,0,374,87,1,0,0,0,375,373,1,0,0,0,376,377,5,
        34,0,0,377,380,3,88,44,0,378,380,3,90,45,0,379,376,1,0,0,0,379,378,
        1,0,0,0,380,89,1,0,0,0,381,382,5,30,0,0,382,385,3,90,45,0,383,385,
        3,92,46,0,384,381,1,0,0,0,384,383,1,0,0,0,385,91,1,0,0,0,386,389,
        5,51,0,0,387,389,3,68,34,0,388,386,1,0,0,0,388,387,1,0,0,0,389,390,
        1,0,0,0,390,391,5,49,0,0,391,392,3,94,47,0,392,393,5,50,0,0,393,
        396,1,0,0,0,394,396,3,96,48,0,395,388,1,0,0,0,395,394,1,0,0,0,396,
        93,1,0,0,0,397,398,3,78,39,0,398,399,5,46,0,0,399,400,3,94,47,0,
        400,403,1,0,0,0,401,403,3,78,39,0,402,397,1,0,0,0,402,401,1,0,0,
        0,403,95,1,0,0,0,404,412,3,102,51,0,405,406,5,47,0,0,406,407,3,78,
        39,0,407,408,5,48,0,0,408,412,1,0,0,0,409,412,3,68,34,0,410,412,
        5,51,0,0,411,404,1,0,0,0,411,405,1,0,0,0,411,409,1,0,0,0,411,410,
        1,0,0,0,412,97,1,0,0,0,413,414,7,3,0,0,414,99,1,0,0,0,415,416,7,
        4,0,0,416,101,1,0,0,0,417,418,7,5,0,0,418,103,1,0,0,0,38,107,123,
        128,133,137,148,153,164,171,178,186,218,226,233,237,252,257,270,
        278,286,290,295,299,306,314,321,327,334,341,351,362,373,379,384,
        388,395,402,411
    ]

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
        self.checkVersion("4.13.1")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2392555720274942) != 0)):
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


            self.state = 126 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 125
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 128 
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




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.typ()
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 131
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 132
                self.expr7()
                pass


            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
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




    def im_vardecl(self):

        localctx = ZCodeParser.Im_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_im_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ZCodeParser.VAR)
            self.state = 140
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 141
            self.match(ZCodeParser.ARROW)
            self.state = 142
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




    def im_dydecl(self):

        localctx = ZCodeParser.Im_dydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_im_dydecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.DYNAMIC)
            self.state = 145
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
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




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ZCodeParser.FUNC)
            self.state = 151
            self.func()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15 or _la==27:
                self.state = 152
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




    def func(self):

        localctx = ZCodeParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 156
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




    def arg(self):

        localctx = ZCodeParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZCodeParser.LPAREN)
            self.state = 159
            self.arglist()
            self.state = 160
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




    def arglist(self):

        localctx = ZCodeParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arglist)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.argprime()
                pass
            elif token in [48]:
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




    def argprime(self):

        localctx = ZCodeParser.ArgprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argprime)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.argment()
                self.state = 167
                self.match(ZCodeParser.COMMA)
                self.state = 168
                self.argprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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




    def argment(self):

        localctx = ZCodeParser.ArgmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.typ()
            self.state = 174
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




    def funcend(self):

        localctx = ZCodeParser.FuncendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcend)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.returnstmt()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
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




    def builtin(self):

        localctx = ZCodeParser.BuiltinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_builtin)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.readnum()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.writenum()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.readbool()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.writebool()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.readstr()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 185
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




    def readnum(self):

        localctx = ZCodeParser.ReadnumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_readnum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
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




    def writenum(self):

        localctx = ZCodeParser.WritenumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_writenum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(ZCodeParser.T__1)
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


    class ReadboolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_readbool




    def readbool(self):

        localctx = ZCodeParser.ReadboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_readbool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
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




    def writebool(self):

        localctx = ZCodeParser.WriteboolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_writebool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(ZCodeParser.T__3)
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


    class ReadstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_readstr




    def readstr(self):

        localctx = ZCodeParser.ReadstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_readstr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
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




    def writestr(self):

        localctx = ZCodeParser.WritestrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_writestr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(ZCodeParser.T__5)
            self.state = 203
            self.expr()
            self.state = 204
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




    def arraydecl(self):

        localctx = ZCodeParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.typ()
            self.state = 207
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 208
            self.match(ZCodeParser.LBRACKET)
            self.state = 209
            self.arraydim()
            self.state = 210
            self.match(ZCodeParser.RBRACKET)
            self.state = 211
            self.match(ZCodeParser.ARROW)
            self.state = 212
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




    def arraydim(self):

        localctx = ZCodeParser.ArraydimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arraydim)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 215
                self.match(ZCodeParser.COMMA)
                self.state = 216
                self.arraydim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(ZCodeParser.LBRACKET)
            self.state = 221
            self.arraylist()
            self.state = 222
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




    def arraylist(self):

        localctx = ZCodeParser.ArraylistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arraylist)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.arrayobj()
                pass
            elif token in [50]:
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




    def arrayobj(self):

        localctx = ZCodeParser.ArrayobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arrayobj)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.arrayelement()
                self.state = 229
                self.match(ZCodeParser.COMMA)
                self.state = 230
                self.arrayobj()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
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




    def arrayelement(self):

        localctx = ZCodeParser.ArrayelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arrayelement)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.literals()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
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




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.expr()
            self.state = 240
            self.match(ZCodeParser.ARROW)
            self.state = 241
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




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ZCodeParser.IF)
            self.state = 244
            self.ifexpr()
            self.state = 245
            self.stmt()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 246
                    self.match(ZCodeParser.ELIF)
                    self.state = 247
                    self.ifexpr()
                    self.state = 248
                    self.stmt()
                    self.state = 254
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 255
                self.match(ZCodeParser.ELSE)
                self.state = 256
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




    def ifexpr(self):

        localctx = ZCodeParser.IfexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ifexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ZCodeParser.LPAREN)
            self.state = 260
            self.expr()
            self.state = 261
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




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ZCodeParser.FOR)
            self.state = 264
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 265
            self.match(ZCodeParser.UNTIL)
            self.state = 266
            self.expr()
            self.state = 267
            self.match(ZCodeParser.BY)
            self.state = 268
            self.expr()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 269
                self.match(ZCodeParser.NEWLINE)


            self.state = 272
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




    def otherstmt(self):

        localctx = ZCodeParser.OtherstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_otherstmt)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.breakstmt()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.continuestmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.returnstmt()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
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




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
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




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
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




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(ZCodeParser.RETURN)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392555555652606) != 0):
                self.state = 285
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




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ZCodeParser.BEGIN)
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 289
                self.match(ZCodeParser.NEWLINE)


            self.state = 295
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 292
                    self.stmt() 
                self.state = 297
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 298
                self.match(ZCodeParser.NEWLINE)


            self.state = 301
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




    def funccall(self):

        localctx = ZCodeParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_funccall)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 304
                self.paramdecl()
                pass
            elif token in [1, 2, 3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
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




    def paramdecl(self):

        localctx = ZCodeParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_paramdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.LPAREN)
            self.state = 309
            self.paramlist()
            self.state = 310
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




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_paramlist)
        try:
            self.state = 314
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 30, 34, 47, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.paramprime()
                pass
            elif token in [48]:
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




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_paramprime)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
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




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_param)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
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




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
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




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr1)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
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
            self.state = 344
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
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
                    if not(_la==35 or _la==36):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 348
                    self.expr3(0) 
                self.state = 353
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
            self.state = 355
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
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
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 359
                    self.expr4(0) 
                self.state = 364
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
            self.state = 366
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 370
                    self.expr5() 
                self.state = 375
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




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr5)
        try:
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.match(ZCodeParser.NOT)
                self.state = 377
                self.expr5()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 30, 47, 51]:
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




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr6)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(ZCodeParser.MINUS)
                self.state = 382
                self.expr6()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 47, 51]:
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




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr7)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
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
                self.idxop()
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




    def idxop(self):

        localctx = ZCodeParser.IdxopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_idxop)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.expr()
                self.state = 398
                self.match(ZCodeParser.COMMA)
                self.state = 399
                self.idxop()
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




    def expr9(self):

        localctx = ZCodeParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr9)
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
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




    def relationals(self):

        localctx = ZCodeParser.RelationalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_relationals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 52364241272832) != 0)):
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




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
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




    def literals(self):

        localctx = ZCodeParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
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
         




