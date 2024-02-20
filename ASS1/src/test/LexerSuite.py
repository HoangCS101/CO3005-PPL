import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test100(self):
        self.assertTrue(TestLexer.test("aBc4_9D", "aBc4_9D,<EOF>", 100)) # identifier
    
    def test101(self):
        self.assertTrue(TestLexer.test("\t\b\f", "<EOF>", 101 )) # white space

    def test102(self):
        self.assertTrue(TestLexer.test("## this is comment", "<EOF>", 102 )) # comment

    def test103(self):
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 103 ))

    def test104(self):
        self.assertTrue(TestLexer.test("false", "false,<EOF>", 104 ))

    def test105(self):
        self.assertTrue(TestLexer.test("number", "number,<EOF>", 105 ))

    def test106(self):
        self.assertTrue(TestLexer.test("bool", "bool,<EOF>", 106 ))

    def test107(self):
        self.assertTrue(TestLexer.test("string", "string,<EOF>", 107 ))

    def test108(self):
        self.assertTrue(TestLexer.test("return", "return,<EOF>", 108 ))

    def test109(self):
        self.assertTrue(TestLexer.test("var", "var,<EOF>", 109 ))

    def test110(self):
        self.assertTrue(TestLexer.test("dynamic", "dynamic,<EOF>", 110 ))

    def test111(self):
        self.assertTrue(TestLexer.test("func", "func,<EOF>", 111 ))

    def test112(self):
        self.assertTrue(TestLexer.test("for", "for,<EOF>", 112 ))

    def test113(self):
        self.assertTrue(TestLexer.test("until", "until,<EOF>", 113 ))

    def test114(self):
        self.assertTrue(TestLexer.test("by", "by,<EOF>", 114 ))

    def test115(self):
        self.assertTrue(TestLexer.test("break", "break,<EOF>", 115 ))

    def test116(self):
        self.assertTrue(TestLexer.test("continue", "continue,<EOF>", 116 ))

    def test117(self):
        self.assertTrue(TestLexer.test("if", "if,<EOF>", 117 ))

    def test118(self):
        self.assertTrue(TestLexer.test("else", "else,<EOF>", 118 ))

    def test119(self):
        self.assertTrue(TestLexer.test("elif", "elif,<EOF>", 119 ))

    def test120(self):
        self.assertTrue(TestLexer.test("begin", "begin,<EOF>", 120 ))

    def test121(self):
        self.assertTrue(TestLexer.test("end", "end,<EOF>", 121 ))

    def test122(self):
        self.assertTrue(TestLexer.test("not", "not,<EOF>", 122 ))

    def test123(self):
        self.assertTrue(TestLexer.test("and", "and,<EOF>", 123 ))

    def test124(self):
        self.assertTrue(TestLexer.test("or", "or,<EOF>", 124 ))

    def test125(self):
        self.assertTrue(TestLexer.test("+", "+,<EOF>", 125 ))

    def test126(self):
        self.assertTrue(TestLexer.test("-", "-,<EOF>", 126 ))

    def test127(self):
        self.assertTrue(TestLexer.test("*", "*,<EOF>", 127 ))

    def test128(self):
        self.assertTrue(TestLexer.test("/", "/,<EOF>", 128 ))

    def test129(self):
        self.assertTrue(TestLexer.test("%", "%,<EOF>", 129 ))

    def test130(self):
        self.assertTrue(TestLexer.test("=", "=,<EOF>", 130 ))

    def test131(self):
        self.assertTrue(TestLexer.test("<-", "<-,<EOF>", 131 ))

    def test132(self):
        self.assertTrue(TestLexer.test("!=", "!=,<EOF>", 132 ))

    def test133(self):
        self.assertTrue(TestLexer.test("<", "<,<EOF>", 133 ))

    def test134(self):
        self.assertTrue(TestLexer.test("<=", "<=,<EOF>", 134 ))

    def test135(self):
        self.assertTrue(TestLexer.test(">", ">,<EOF>", 135 ))

    def test136(self):
        self.assertTrue(TestLexer.test(">=", ">=,<EOF>", 136 ))

    def test137(self):
        self.assertTrue(TestLexer.test("...", "...,<EOF>", 137 ))

    def test138(self):
        self.assertTrue(TestLexer.test("==", "==,<EOF>", 138 ))

    def test139(self):
        self.assertTrue(TestLexer.test("(", "(,<EOF>", 139 ))

    def test140(self):
        self.assertTrue(TestLexer.test(")", "),<EOF>", 140 ))

    def test141(self):
        self.assertTrue(TestLexer.test("[", "[,<EOF>", 141 ))

    def test142(self):
        self.assertTrue(TestLexer.test("]", "],<EOF>", 142 ))

    def test143(self):
        self.assertTrue(TestLexer.test("\n", "\n\n,<EOF>", 143 ))

    def test144(self):
        self.assertTrue(TestLexer.test("144", "144,<EOF>", 144 ))

    def test145(self):
        self.assertTrue(TestLexer.test("0", "0,<EOF>", 145 ))

    def test146(self):
        self.assertTrue(TestLexer.test("45.", "45.,<EOF>", 146 ))

    def test147(self):
        self.assertTrue(TestLexer.test("87.7", "87.7,<EOF>", 147 ))

    def test148(self):
        self.assertTrue(TestLexer.test("96.6999", "96.6999,<EOF>", 148 ))

    def test149(self):
        self.assertTrue(TestLexer.test("71.e54", "71.e54,<EOF>", 149 ))

    def test150(self):
        self.assertTrue(TestLexer.test("6785.E-11", "6785.E-11,<EOF>", 150 ))

    def test151(self):
        self.assertTrue(TestLexer.test("543.75755E9993", "543.75755E9993,<EOF>", 151 ))

    def test152(self):
        self.assertTrue(TestLexer.test("2.454545e-22", "2.454545e-22,<EOF>", 152 ))

    def test153(self):
        self.assertTrue(TestLexer.test("\"He asked me: \'\"Where is John Cena?\'\"\"", "He asked me: \'\"Where is John Cena?\'\",<EOF>", 153 ))

    def test154(self):
        self.assertTrue(TestLexer.test("\"Here comes tab \\t\"", "Here comes tab \\t,<EOF>", 154 ))

    def test155(self):
        self.assertTrue(TestLexer.test("AAb+-break===*/25.e4", "AAb,+,-,break,==,=,*,/,25.e4,<EOF>", 155 ))

    def test156(self):
        self.assertTrue(TestLexer.test("return func \"Meatballs \\b haiyaa \'\" \\n\"", "return,func,Meatballs \\b haiyaa \'\" \\n,<EOF>", 156 ))
    
    def test157(self):
        self.assertTrue(TestLexer.test("(),,,[]", "(,),,,,,,,[,],<EOF>", 157 ))

    def test158(self):
        self.assertTrue(TestLexer.test("a@AS$s", "a,Error Token @", 158 ))

    def test159(self):
        self.assertTrue(TestLexer.test("# wrong comment", "Error Token #", 159 ))

    def test160(self):
        self.assertTrue(TestLexer.test("12..3e-+55", "12.,Error Token .", 160 ))

    def test161(self):
        self.assertTrue(TestLexer.test("\"String with \n before last double quotes should be wrong\"", "Error Token \"", 161 ))

    def test162(self):
        self.assertTrue(TestLexer.test("\"Here goes EOF", "Error Token \"", 162 ))

    def test163(self):
        self.assertTrue(TestLexer.test("x = 5", "x,=,5,<EOF>", 163 ))

    def test164(self):
        self.assertTrue(TestLexer.test("x <- y + z", "x,<-,y,+,z,<EOF>", 164 ))

    def test165(self):
        self.assertTrue(TestLexer.test("if (x == y) return true", "if,(,x,==,y,),return,true,<EOF>", 165 ))

    def test166(self):
        self.assertTrue(TestLexer.test("writeString(\"Hello, World!\")", "writeString(,Hello, World!,),<EOF>", 166 ))

    def test167(self):
        self.assertTrue(TestLexer.test("for i until 10 by 1 print(i)", "for,i,until,10,by,1,print,(,i,),<EOF>", 167 ))
        
    def test168(self):
        self.assertTrue(TestLexer.test("var i <- 0", "var,i,<-,0,<EOF>", 168 ))

    def test169(self):
        self.assertTrue(TestLexer.test("func add(a, b) return a + b", "func,add,(,a,,,b,),return,a,+,b,<EOF>", 169 ))

    def test170(self):
        self.assertTrue(TestLexer.test("if (x == y) return true", "if,(,x,==,y,),return,true,<EOF>", 170 ))

    def test171(self):
        self.assertTrue(TestLexer.test("x <- y + z", "x,<-,y,+,z,<EOF>", 171 ))

    def test172(self):
        self.assertTrue(TestLexer.test("123var", "123,var,<EOF>", 172 ))

    def test173(self):
        self.assertTrue(TestLexer.test("identifierWithUnderscore_123", "identifierWithUnderscore_123,<EOF>", 173 ))

    def test174(self):
        self.assertTrue(TestLexer.test("writeString(\"Hello\")", "writeString(,Hello,),<EOF>", 174 ))

    def test175(self):
        self.assertTrue(TestLexer.test("for i until 5 by 1 print(i)", "for,i,until,5,by,1,print,(,i,),<EOF>", 175 ))

    def test176(self):
        self.assertTrue(TestLexer.test("var name <- \"John\"", "var,name,<-,John,<EOF>", 176 ))

    def test177(self):
        self.assertTrue(TestLexer.test("var flag <- true", "var,flag,<-,true,<EOF>", 177 ))

    def test178(self):
        self.assertTrue(TestLexer.test("readBool()", "readBool(),<EOF>", 178 ))

    def test179(self):
        self.assertTrue(TestLexer.test("readNumber()", "readNumber(),<EOF>", 179 ))

    def test180(self):
        self.assertTrue(TestLexer.test("readString()", "readString(),<EOF>", 180 ))

    def test181(self):
        self.assertTrue(TestLexer.test("\"I sure love being BKer ngl\"", "I sure love being BKer ngl,<EOF>", 181 ))

    def test182(self):
        self.assertTrue(TestLexer.test("\"A statement noone asked for\"", "A statement noone asked for,<EOF>", 182 ))

    def test183(self):
        self.assertTrue(TestLexer.test("+_*/%======...===", "+,_,*,/,%,==,==,==,...,==,=,<EOF>", 183 ))

    def test184(self):
        self.assertTrue(TestLexer.test("234252.4544e-343256667", "234252.4544e-343256667,<EOF>", 184 ))

    def test185(self):
        self.assertTrue(TestLexer.test("a[6]", "a,[,6,],<EOF>", 185 ))

    def test186(self):
        self.assertTrue(TestLexer.test("moist", "moist,<EOF>", 186 ))

    def test187(self):
        self.assertTrue(TestLexer.test("56 - 88 * (12 + -3)", "56,-,88,*,(,12,+,-,3,),<EOF>", 187 ))

    def test188(self):
        self.assertTrue(TestLexer.test("caster hallal", "caster,hallal,<EOF>", 188 ))

    def test189(self):
        self.assertTrue(TestLexer.test("(((([[[[[]]]]]))))", "(,(,(,(,[,[,[,[,[,],],],],],),),),),<EOF>", 189 ))

    def test190(self):
        self.assertTrue(TestLexer.test("\"Nah, I'd win\"", "Nah, I'd win,<EOF>", 190 ))

    def test191(self):
        self.assertTrue(TestLexer.test("number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]", "number,b,[,2,,,3,],<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],],<EOF>", 191 ))

    def test192(self):
        self.assertTrue(TestLexer.test("number x <- readNumber()", "number,x,<-,readNumber(),<EOF>", 192 ))

    def test193(self):
        self.assertTrue(TestLexer.test("01234567", "01234567,<EOF>", 193 ))

    def test194(self):
        self.assertTrue(TestLexer.test("\"Hello \'\"bus\'\"\"", "Hello \'\"bus\'\",<EOF>", 194 ))

    def test195(self):
        self.assertTrue(TestLexer.test("\"I am tab \\t\"", "I am tab \\t,<EOF>", 195 ))

    def test196(self):
        self.assertTrue(TestLexer.test("4.96 +-*/ 3", "4.96,+,-,*,/,3,<EOF>", 196 ))

    def test197(self):
        self.assertTrue(TestLexer.test("I like \nbaguette", "I,like,\n\n,baguette,<EOF>", 197 ))

    def test198(self):
        self.assertTrue(TestLexer.test("3 = 5", "3,=,5,<EOF>", 198 ))

    def test199(self):
        self.assertTrue(TestLexer.test("rizz", "rizz,<EOF>", 199 ))
        

    # def test127(self):
    #     self.assertTrue(TestLexer.test("01234567", "01234567,<EOF>", 127))
        
    # def test169(self):
    #     self.assertTrue(TestLexer.test("\"Hello \'\"bus\'\"\"", "Hello \'\"bus\'\",<EOF>", 169))
        
    # def test196(self):
    #     self.assertTrue(TestLexer.test("\"I am tab \\t\"", "I am tab \\t,<EOF>", 196))
        
    # def test153(self):
    #     self.assertTrue(TestLexer.test("4.96 +-*/ 3", "4.e10,<EOF>", 153))
        
    # def test171(self):
    #     self.assertTrue(TestLexer.test("I like \nbaguette", "4.e10,<EOF>", 171))
        
    # def test185(self):
    #     self.assertTrue(TestLexer.test("\t", "4.e10,<EOF>", 185))