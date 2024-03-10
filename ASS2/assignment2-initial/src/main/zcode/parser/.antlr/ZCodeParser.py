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
        4,1,57,437,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,5,0,98,8,0,10,0,12,0,101,9,0,1,0,1,0,4,0,105,
        8,0,11,0,12,0,106,1,0,5,0,110,8,0,10,0,12,0,113,9,0,1,0,4,0,116,
        8,0,11,0,12,0,117,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,134,8,1,1,2,1,2,1,2,3,2,139,8,2,1,2,1,2,3,2,143,8,
        2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,154,8,4,1,5,1,5,1,5,1,
        5,3,5,160,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,3,7,170,8,7,1,8,1,
        8,1,8,1,8,1,8,3,8,177,8,8,1,9,1,9,1,9,1,10,1,10,1,10,3,10,185,8,
        10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,193,8,11,1,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,
        15,1,15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,233,8,19,10,19,12,
        19,236,9,19,1,20,1,20,1,20,1,20,5,20,242,8,20,10,20,12,20,245,9,
        20,1,20,1,20,1,21,1,21,3,21,251,8,21,1,22,1,22,1,22,1,22,1,23,1,
        23,1,23,5,23,260,8,23,10,23,12,23,263,9,23,1,23,1,23,1,23,1,23,1,
        24,1,24,1,24,1,24,5,24,273,8,24,10,24,12,24,276,9,24,1,24,1,24,1,
        24,1,24,3,24,282,8,24,1,25,1,25,1,25,1,25,3,25,288,8,25,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,3,26,297,8,26,1,26,1,26,1,27,1,27,1,27,
        1,27,3,27,305,8,27,1,28,1,28,1,29,1,29,1,30,1,30,3,30,313,8,30,1,
        31,1,31,1,31,1,31,1,31,5,31,320,8,31,10,31,12,31,323,9,31,1,31,1,
        31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,3,32,334,8,32,1,33,1,33,3,
        33,338,8,33,1,34,1,34,1,34,1,34,1,34,3,34,345,8,34,1,35,1,35,1,35,
        1,35,1,35,3,35,352,8,35,1,36,1,36,1,36,1,36,1,36,3,36,359,8,36,1,
        37,1,37,1,37,1,37,1,37,1,37,5,37,367,8,37,10,37,12,37,370,9,37,1,
        38,1,38,1,38,1,38,1,38,1,38,5,38,378,8,38,10,38,12,38,381,9,38,1,
        39,1,39,1,39,1,39,1,39,1,39,5,39,389,8,39,10,39,12,39,392,9,39,1,
        40,1,40,1,40,3,40,397,8,40,1,41,1,41,1,41,3,41,402,8,41,1,42,1,42,
        3,42,406,8,42,1,42,1,42,1,42,1,42,1,42,3,42,413,8,42,1,43,1,43,1,
        43,1,43,1,43,3,43,420,8,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,3,
        44,429,8,44,1,45,1,45,1,46,1,46,1,47,1,47,1,47,1,99,3,74,76,78,48,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        90,92,94,0,6,1,0,35,36,1,0,29,30,1,0,31,33,3,0,37,37,39,43,45,45,
        1,0,12,14,1,0,7,9,445,0,99,1,0,0,0,2,133,1,0,0,0,4,135,1,0,0,0,6,
        144,1,0,0,0,8,149,1,0,0,0,10,155,1,0,0,0,12,163,1,0,0,0,14,169,1,
        0,0,0,16,176,1,0,0,0,18,178,1,0,0,0,20,184,1,0,0,0,22,192,1,0,0,
        0,24,194,1,0,0,0,26,198,1,0,0,0,28,203,1,0,0,0,30,207,1,0,0,0,32,
        212,1,0,0,0,34,216,1,0,0,0,36,221,1,0,0,0,38,229,1,0,0,0,40,237,
        1,0,0,0,42,250,1,0,0,0,44,252,1,0,0,0,46,256,1,0,0,0,48,281,1,0,
        0,0,50,287,1,0,0,0,52,289,1,0,0,0,54,304,1,0,0,0,56,306,1,0,0,0,
        58,308,1,0,0,0,60,310,1,0,0,0,62,314,1,0,0,0,64,333,1,0,0,0,66,337,
        1,0,0,0,68,344,1,0,0,0,70,351,1,0,0,0,72,358,1,0,0,0,74,360,1,0,
        0,0,76,371,1,0,0,0,78,382,1,0,0,0,80,396,1,0,0,0,82,401,1,0,0,0,
        84,412,1,0,0,0,86,419,1,0,0,0,88,428,1,0,0,0,90,430,1,0,0,0,92,432,
        1,0,0,0,94,434,1,0,0,0,96,98,5,53,0,0,97,96,1,0,0,0,98,101,1,0,0,
        0,99,100,1,0,0,0,99,97,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,
        111,3,2,1,0,103,105,5,53,0,0,104,103,1,0,0,0,105,106,1,0,0,0,106,
        104,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,110,3,2,1,0,109,
        104,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,
        115,1,0,0,0,113,111,1,0,0,0,114,116,5,53,0,0,115,114,1,0,0,0,116,
        117,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,119,1,0,0,0,119,
        120,5,0,0,1,120,1,1,0,0,0,121,134,3,4,2,0,122,134,3,6,3,0,123,134,
        3,8,4,0,124,134,3,10,5,0,125,134,3,22,11,0,126,134,3,64,32,0,127,
        134,3,36,18,0,128,134,3,44,22,0,129,134,3,46,23,0,130,134,3,52,26,
        0,131,134,3,54,27,0,132,134,3,70,35,0,133,121,1,0,0,0,133,122,1,
        0,0,0,133,123,1,0,0,0,133,124,1,0,0,0,133,125,1,0,0,0,133,126,1,
        0,0,0,133,127,1,0,0,0,133,128,1,0,0,0,133,129,1,0,0,0,133,130,1,
        0,0,0,133,131,1,0,0,0,133,132,1,0,0,0,134,3,1,0,0,0,135,138,3,92,
        46,0,136,139,5,51,0,0,137,139,3,84,42,0,138,136,1,0,0,0,138,137,
        1,0,0,0,139,142,1,0,0,0,140,141,5,38,0,0,141,143,3,70,35,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,5,1,0,0,0,144,145,5,16,0,0,145,146,5,
        51,0,0,146,147,5,38,0,0,147,148,3,70,35,0,148,7,1,0,0,0,149,150,
        5,17,0,0,150,153,5,51,0,0,151,152,5,38,0,0,152,154,3,70,35,0,153,
        151,1,0,0,0,153,154,1,0,0,0,154,9,1,0,0,0,155,156,5,18,0,0,156,157,
        5,51,0,0,157,159,3,12,6,0,158,160,5,53,0,0,159,158,1,0,0,0,159,160,
        1,0,0,0,160,161,1,0,0,0,161,162,3,20,10,0,162,11,1,0,0,0,163,164,
        5,47,0,0,164,165,3,14,7,0,165,166,5,48,0,0,166,13,1,0,0,0,167,170,
        3,16,8,0,168,170,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,15,
        1,0,0,0,171,172,3,18,9,0,172,173,5,46,0,0,173,174,3,16,8,0,174,177,
        1,0,0,0,175,177,3,18,9,0,176,171,1,0,0,0,176,175,1,0,0,0,177,17,
        1,0,0,0,178,179,3,92,46,0,179,180,3,70,35,0,180,19,1,0,0,0,181,185,
        3,60,30,0,182,185,3,62,31,0,183,185,1,0,0,0,184,181,1,0,0,0,184,
        182,1,0,0,0,184,183,1,0,0,0,185,21,1,0,0,0,186,193,3,24,12,0,187,
        193,3,26,13,0,188,193,3,28,14,0,189,193,3,30,15,0,190,193,3,32,16,
        0,191,193,3,34,17,0,192,186,1,0,0,0,192,187,1,0,0,0,192,188,1,0,
        0,0,192,189,1,0,0,0,192,190,1,0,0,0,192,191,1,0,0,0,193,23,1,0,0,
        0,194,195,5,1,0,0,195,196,5,47,0,0,196,197,5,48,0,0,197,25,1,0,0,
        0,198,199,5,2,0,0,199,200,5,47,0,0,200,201,3,70,35,0,201,202,5,48,
        0,0,202,27,1,0,0,0,203,204,5,3,0,0,204,205,5,47,0,0,205,206,5,48,
        0,0,206,29,1,0,0,0,207,208,5,4,0,0,208,209,5,47,0,0,209,210,3,70,
        35,0,210,211,5,48,0,0,211,31,1,0,0,0,212,213,5,5,0,0,213,214,5,47,
        0,0,214,215,5,48,0,0,215,33,1,0,0,0,216,217,5,6,0,0,217,218,5,47,
        0,0,218,219,3,70,35,0,219,220,5,48,0,0,220,35,1,0,0,0,221,222,3,
        92,46,0,222,223,5,51,0,0,223,224,5,49,0,0,224,225,3,38,19,0,225,
        226,5,50,0,0,226,227,5,38,0,0,227,228,3,40,20,0,228,37,1,0,0,0,229,
        234,5,7,0,0,230,231,5,46,0,0,231,233,5,7,0,0,232,230,1,0,0,0,233,
        236,1,0,0,0,234,232,1,0,0,0,234,235,1,0,0,0,235,39,1,0,0,0,236,234,
        1,0,0,0,237,238,5,49,0,0,238,243,3,42,21,0,239,240,5,46,0,0,240,
        242,3,42,21,0,241,239,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,
        244,1,0,0,0,244,246,1,0,0,0,245,243,1,0,0,0,246,247,5,50,0,0,247,
        41,1,0,0,0,248,251,3,70,35,0,249,251,3,40,20,0,250,248,1,0,0,0,250,
        249,1,0,0,0,251,43,1,0,0,0,252,253,3,70,35,0,253,254,5,38,0,0,254,
        255,3,70,35,0,255,45,1,0,0,0,256,257,5,24,0,0,257,261,3,70,35,0,
        258,260,5,53,0,0,259,258,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,
        261,262,1,0,0,0,262,264,1,0,0,0,263,261,1,0,0,0,264,265,3,2,1,0,
        265,266,3,48,24,0,266,267,3,50,25,0,267,47,1,0,0,0,268,269,5,53,
        0,0,269,270,5,26,0,0,270,274,3,70,35,0,271,273,5,53,0,0,272,271,
        1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,1,0,0,0,275,277,
        1,0,0,0,276,274,1,0,0,0,277,278,3,2,1,0,278,279,3,48,24,0,279,282,
        1,0,0,0,280,282,1,0,0,0,281,268,1,0,0,0,281,280,1,0,0,0,282,49,1,
        0,0,0,283,284,5,53,0,0,284,285,5,25,0,0,285,288,3,2,1,0,286,288,
        1,0,0,0,287,283,1,0,0,0,287,286,1,0,0,0,288,51,1,0,0,0,289,290,5,
        19,0,0,290,291,5,51,0,0,291,292,5,20,0,0,292,293,3,70,35,0,293,294,
        5,21,0,0,294,296,3,70,35,0,295,297,5,53,0,0,296,295,1,0,0,0,296,
        297,1,0,0,0,297,298,1,0,0,0,298,299,3,2,1,0,299,53,1,0,0,0,300,305,
        3,56,28,0,301,305,3,58,29,0,302,305,3,60,30,0,303,305,3,62,31,0,
        304,300,1,0,0,0,304,301,1,0,0,0,304,302,1,0,0,0,304,303,1,0,0,0,
        305,55,1,0,0,0,306,307,5,22,0,0,307,57,1,0,0,0,308,309,5,23,0,0,
        309,59,1,0,0,0,310,312,5,15,0,0,311,313,3,70,35,0,312,311,1,0,0,
        0,312,313,1,0,0,0,313,61,1,0,0,0,314,315,5,27,0,0,315,316,5,53,0,
        0,316,321,3,2,1,0,317,318,5,53,0,0,318,320,3,2,1,0,319,317,1,0,0,
        0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,324,1,0,0,
        0,323,321,1,0,0,0,324,325,5,53,0,0,325,326,5,28,0,0,326,63,1,0,0,
        0,327,328,5,51,0,0,328,329,5,47,0,0,329,330,3,66,33,0,330,331,5,
        48,0,0,331,334,1,0,0,0,332,334,3,22,11,0,333,327,1,0,0,0,333,332,
        1,0,0,0,334,65,1,0,0,0,335,338,3,68,34,0,336,338,1,0,0,0,337,335,
        1,0,0,0,337,336,1,0,0,0,338,67,1,0,0,0,339,340,3,70,35,0,340,341,
        5,46,0,0,341,342,3,68,34,0,342,345,1,0,0,0,343,345,3,70,35,0,344,
        339,1,0,0,0,344,343,1,0,0,0,345,69,1,0,0,0,346,347,3,72,36,0,347,
        348,5,44,0,0,348,349,3,72,36,0,349,352,1,0,0,0,350,352,3,72,36,0,
        351,346,1,0,0,0,351,350,1,0,0,0,352,71,1,0,0,0,353,354,3,74,37,0,
        354,355,3,90,45,0,355,356,3,74,37,0,356,359,1,0,0,0,357,359,3,74,
        37,0,358,353,1,0,0,0,358,357,1,0,0,0,359,73,1,0,0,0,360,361,6,37,
        -1,0,361,362,3,76,38,0,362,368,1,0,0,0,363,364,10,2,0,0,364,365,
        7,0,0,0,365,367,3,76,38,0,366,363,1,0,0,0,367,370,1,0,0,0,368,366,
        1,0,0,0,368,369,1,0,0,0,369,75,1,0,0,0,370,368,1,0,0,0,371,372,6,
        38,-1,0,372,373,3,78,39,0,373,379,1,0,0,0,374,375,10,2,0,0,375,376,
        7,1,0,0,376,378,3,78,39,0,377,374,1,0,0,0,378,381,1,0,0,0,379,377,
        1,0,0,0,379,380,1,0,0,0,380,77,1,0,0,0,381,379,1,0,0,0,382,383,6,
        39,-1,0,383,384,3,80,40,0,384,390,1,0,0,0,385,386,10,2,0,0,386,387,
        7,2,0,0,387,389,3,80,40,0,388,385,1,0,0,0,389,392,1,0,0,0,390,388,
        1,0,0,0,390,391,1,0,0,0,391,79,1,0,0,0,392,390,1,0,0,0,393,394,5,
        34,0,0,394,397,3,80,40,0,395,397,3,82,41,0,396,393,1,0,0,0,396,395,
        1,0,0,0,397,81,1,0,0,0,398,399,5,30,0,0,399,402,3,82,41,0,400,402,
        3,84,42,0,401,398,1,0,0,0,401,400,1,0,0,0,402,83,1,0,0,0,403,406,
        5,51,0,0,404,406,3,64,32,0,405,403,1,0,0,0,405,404,1,0,0,0,406,407,
        1,0,0,0,407,408,5,49,0,0,408,409,3,86,43,0,409,410,5,50,0,0,410,
        413,1,0,0,0,411,413,3,88,44,0,412,405,1,0,0,0,412,411,1,0,0,0,413,
        85,1,0,0,0,414,415,3,70,35,0,415,416,5,46,0,0,416,417,3,86,43,0,
        417,420,1,0,0,0,418,420,3,70,35,0,419,414,1,0,0,0,419,418,1,0,0,
        0,420,87,1,0,0,0,421,429,3,94,47,0,422,423,5,47,0,0,423,424,3,70,
        35,0,424,425,5,48,0,0,425,429,1,0,0,0,426,429,3,64,32,0,427,429,
        5,51,0,0,428,421,1,0,0,0,428,422,1,0,0,0,428,426,1,0,0,0,428,427,
        1,0,0,0,429,89,1,0,0,0,430,431,7,3,0,0,431,91,1,0,0,0,432,433,7,
        4,0,0,433,93,1,0,0,0,434,435,7,5,0,0,435,95,1,0,0,0,38,99,106,111,
        117,133,138,142,153,159,169,176,184,192,234,243,250,261,274,281,
        287,296,304,312,321,333,337,344,351,358,368,379,390,396,401,405,
        412,419,428
    ]

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
        self.checkVersion("4.13.1")
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
                        if not (_la==53):
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
                if not (_la==53):
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
            if _la==38:
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
            if _la==38:
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




    def arglist(self):

        localctx = ZCodeParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arglist)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
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




    def funcend(self):

        localctx = ZCodeParser.FuncendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcend)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.returnstmt()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.blockstmt()
                pass
            elif token in [53]:
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




    def builtin(self):

        localctx = ZCodeParser.BuiltinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_builtin)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.readnum()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.writenum()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.readbool()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.writebool()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.readstr()
                pass
            elif token in [6]:
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
            while _la==46:
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
            while _la==46:
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




    def arrayelement(self):

        localctx = ZCodeParser.ArrayelementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arrayelement)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 30, 34, 47, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.expr()
                pass
            elif token in [49]:
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
            while _la==53:
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
                while _la==53:
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
            if _la==53:
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




    def otherstmt(self):

        localctx = ZCodeParser.OtherstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_otherstmt)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.breakstmt()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.continuestmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 302
                self.returnstmt()
                pass
            elif token in [27]:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2392555555652606) != 0):
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




    def funccall(self):

        localctx = ZCodeParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_funccall)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
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
            elif token in [1, 2, 3, 4, 5, 6]:
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




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_paramlist)
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 30, 34, 47, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime




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
                    if not(_la==35 or _la==36):
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
                    if not(_la==29 or _la==30):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
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




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr5)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.match(ZCodeParser.NOT)
                self.state = 394
                self.expr5()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 30, 47, 51]:
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




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr6)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.MINUS)
                self.state = 399
                self.expr6()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 47, 51]:
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




    def relationals(self):

        localctx = ZCodeParser.RelationalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_relationals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
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
        self.enterRule(localctx, 92, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
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
        self.enterRule(localctx, 94, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
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
         




