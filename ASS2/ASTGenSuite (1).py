import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):   
    
    def test_declared(self):
        """declared  declared  declared  declared"""
        input = """
            number HienPhan
        """
        expect = str(Program([
                VarDecl(Id("HienPhan"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test_1(self):
        """declared  declared  declared"""
        input = """
            string HienPhan <- 1
        """
        expect = str(Program([
                VarDecl(Id("HienPhan"), StringType(), None, NumberLiteral(1))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test_3(self):
        input = """
            string Hien
            bool Hien
            string Hien <- 1
            bool Hien <- 1
        """
        expect = str(Program([
                VarDecl(Id("Hien"), StringType()),
                VarDecl(Id("Hien"), BoolType()),
                VarDecl(Id("Hien"), StringType(), None, NumberLiteral(1)),
                VarDecl(Id("Hien"), BoolType(), None, NumberLiteral(1))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test_4(self):
        input = """
            string HienPhan[5] <- 1
            string HienPhan[5]
        """
        expect = str(Program([
                VarDecl(Id("HienPhan"), ArrayType([5], StringType()), None, NumberLiteral(1)),
                VarDecl(Id("HienPhan"), ArrayType([5], StringType()))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test_5(self):
        input = """
            number HienPhan[5,3,4] <- 1
            bool HienPhan[2,3,4]
        """
        expect = str(Program([
                VarDecl(Id("HienPhan"), ArrayType([5, 3, 4], NumberType()), None, NumberLiteral(1)),
                VarDecl(Id("HienPhan"), ArrayType([2, 3, 4], BoolType()))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test_6(self):
        input = """
            dynamic Hien <- 1
            dynamic Hien
        """
        expect = str(Program([
                    VarDecl(Id("Hien"), None, None, NumberLiteral(1)),
                    VarDecl(Id("Hien"), None)
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test_7(self):
        input = """
            var Hien <- 1
        """
        expect = str(Program([
                    VarDecl(Id("Hien"), None, None, NumberLiteral(1))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test_8(self):
        input = """
            func main()
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], None)
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test_9(self):
        input = """
            func main()
                begin
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """
            func main()
                begin
                break
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Break()]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 310))
                
    def test_11(self):
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number Hien[1,2])
                return
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                          VarDecl(Id("a"), StringType()), 
                                          VarDecl(Id("a"), ArrayType([2], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("Hien"), ArrayType([1, 2], NumberType()))], Return(None))
                ]))
        # print(expect)
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test_Expression(self):
        """Expression Expression Expression"""
        input = """
            var x <- 1
            var x <- "123"
            var x <- true
            var x <- false
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  NumberLiteral(1)),
                    VarDecl(Id("x"), None, None,  StringLiteral("123")),
                    VarDecl(Id("x"), None, None,  BooleanLiteral(True)),
                    VarDecl(Id("x"), None, None,  BooleanLiteral(False))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_13(self):
        input = """
            var x <- [1, "a", true, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  ArrayLiteral([NumberLiteral(1), StringLiteral("a"), BooleanLiteral(True), BooleanLiteral(False)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 313))   
        
    def test_14(self):
        input = """
            var x <- [[1], [1]]
            var x <- [[1]]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  ArrayLiteral([ArrayLiteral([NumberLiteral(1)]), ArrayLiteral([NumberLiteral(1)])])),
                    VarDecl(Id("x"), None, None,  ArrayLiteral([ArrayLiteral([NumberLiteral(1)])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 314))  
        
    def test_15(self):
        input = """
            var x <- 1 ... "2"
            var x <- 1 <= "2"
            var x <- 1 and 2 or 3
            var x <- 1 + 2 - 3
            var x <- 1 * 2 / 3 % 4
            var x <- ---1
            var x <- not not 1
            var x <- x 
            var x <- a[1,2,3]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  BinaryOp("...", NumberLiteral(1), StringLiteral("2"))),
                    VarDecl(Id("x"), None, None,  BinaryOp("<=", NumberLiteral(1), StringLiteral("2"))),
                    VarDecl(Id("x"), None, None,  BinaryOp("or", BinaryOp("and", NumberLiteral(1), NumberLiteral(2)), NumberLiteral(3))),
                    VarDecl(Id("x"), None, None,  BinaryOp("-", BinaryOp("+", NumberLiteral(1), NumberLiteral(2)), NumberLiteral(3))),
                    VarDecl(Id("x"), None, None,  BinaryOp("%", BinaryOp("/", BinaryOp("*", NumberLiteral(1), NumberLiteral(2)), NumberLiteral(3)), NumberLiteral(4))),
                    VarDecl(Id("x"), None, None,  UnaryOp("-", UnaryOp("-", UnaryOp("-", NumberLiteral(1))))),
                    VarDecl(Id("x"), None, None,  UnaryOp("not", UnaryOp("not", NumberLiteral(1)))),
                    VarDecl(Id("x"), None, None,  Id("x")),
                    VarDecl(Id("x"), None, None,  ArrayCell(Id("a"), [NumberLiteral(1), NumberLiteral(2), NumberLiteral(3)]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 315))  
        
    def test_16(self):
        input = """
            var x <- 2 or 3 and 1 <= 2 ... 4 <= 5 + a * 3 + c - -1 + not - 2
        """
        expect = str(Program([
                VarDecl(Id("x"), None, None,  BinaryOp("...", BinaryOp("<=", BinaryOp("and", BinaryOp("or", NumberLiteral(2), NumberLiteral(3)), NumberLiteral(1)), NumberLiteral(2)), BinaryOp("<=", NumberLiteral(4), BinaryOp("+", BinaryOp("-", BinaryOp("+", BinaryOp("+", NumberLiteral(5), BinaryOp("*", Id("a"), NumberLiteral(3))), Id("c")), UnaryOp("-", NumberLiteral(1))), UnaryOp("not", UnaryOp("-", NumberLiteral(2)))))))
            ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 316))  
        
    def test_17(self):
        input = """
            var x <- -a[1+2] ... 2
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  BinaryOp("...", UnaryOp("-", ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1), NumberLiteral(2))])), NumberLiteral(2)))
                ]))
        #print(expect)
        # self.assertTrue(TestAST.test(input, expect, 317))  
    
    def test_18(self):
        input = """
            var x <- fun()
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  CallExpr(Id("fun"), []))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 318)) 
    
    def test_19(self):
        input = """
            var x <- fun(1+1, "a")
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  CallExpr(Id("fun"), [BinaryOp("+", NumberLiteral(1), NumberLiteral(1)), StringLiteral("a")]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 319)) 
        
    def test_20(self):
        input = """
            var x <- fun(fun())
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  CallExpr(Id("fun"), [CallExpr(Id("fun"), [])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 320)) 
            
    def test_21(self):
        input = """
            var x <- (2 ... 3) ... 4
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, None,  BinaryOp("...", BinaryOp("...", NumberLiteral(2), NumberLiteral(3)), NumberLiteral(4)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 321)) 
             
    def test_22(self):
        """Statements Statements Statements"""
        input = """
            func main()
                begin
                    continue
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue()]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 322))
    
    def test_23(self):
        input = """
            func main()
                begin
                    continue
                    continue
                    break
                    begin
                        continue
                        continue
                        break                    
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Continue(),
                    Continue(),
                    Break(),
                        Block([
                        Continue(),
                        Continue(),
                        Break()])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 323))
            
    def test_24(self):
        input = """
            func main()
                begin
                    return  1 + 1
                end
            func main()
                return 1
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Return(BinaryOp("+", NumberLiteral(1), NumberLiteral(1)))])),
                    FuncDecl(Id("main"), [], Return(NumberLiteral(1)))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 324))
    
    def test_25(self):
        input = """
            func main()
                begin
                    main(a)
                    main(1,1)
                end
            func main()
                begin
                main()
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [Id("a")]),
                    CallStmt(Id("main"), [NumberLiteral(1), NumberLiteral(1)])])),
                    FuncDecl(Id("main"), [], Block([
                    CallStmt(Id("main"), [])]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 325))
            
    def test_26(self):
        input = """
            func main()
                begin
                    a <- 1
                    a[1] <- 2
                    a[3,2] <- 4 + 2
                end
            func main()
                begin
                a[1+1, 3] <- 1
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    Assign(Id("a"), NumberLiteral(1)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(1)]), NumberLiteral(2)),
                    Assign(ArrayCell(Id("a"), [NumberLiteral(3), NumberLiteral(2)]), BinaryOp("+", NumberLiteral(4), NumberLiteral(2)))])),
                    FuncDecl(Id("main"), [], Block([
                    Assign(ArrayCell(Id("a"), [BinaryOp("+", NumberLiteral(1), NumberLiteral(1)), NumberLiteral(3)]), NumberLiteral(1))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 326))
            
    def test_27(self):
        input = """
            func main()
                begin
                    for i until i > 2 by 1 + 1
                        print(1)
                end
            func main()
                begin
                    for i until i by [1]
                    begin
                        print(1)
                    end
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), BinaryOp(">", Id("i"), NumberLiteral(2)), BinaryOp("+", NumberLiteral(1), NumberLiteral(1)), CallStmt(Id("print"), [NumberLiteral(1)]))])),
                    FuncDecl(Id("main"), [], Block([
                    For(Id("i"), Id("i"), ArrayLiteral([NumberLiteral(1)]), Block([
                    CallStmt(Id("print"), [NumberLiteral(1)])]))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 327))
            
    def test_28(self):
        input = """
            func main()
                begin
                    if (true) return 1
                end
            func main()
                begin
                    if (true) return 2
                    else return 3
                end
        """
        expect = str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1)), [] , None)])),
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(2)), [] ,Return(NumberLiteral(3)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 328))
            
    def test_29(self):
        input = """
            func main()
                begin
                    if (true) return 1
                    elif (true) return 1
                    elif (true) return 1
                    else return 1
                end

        """
        expect =str(Program([
                    FuncDecl(Id("main"), [], Block([
                    If(BooleanLiteral(True), Return(NumberLiteral(1)), 
                       [(BooleanLiteral(True),Return(NumberLiteral(1))),
                        (BooleanLiteral(True),Return(NumberLiteral(1)))] 
                    ,Return(NumberLiteral(1)))]))
                ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 329))     
            
    def test_30(self):
        input = """
            var c <- a[1,2]
            var c <- fun()[1,2]
            var c <- fun(1,2)[1,3]
        """
        expect = str(Program([
            VarDecl(Id("c"), None, None, ArrayCell(Id("a"), [NumberLiteral(1), NumberLiteral(2)])),
            VarDecl(Id("c"), None, None, ArrayCell(CallExpr(Id("fun"), []), [NumberLiteral(1), NumberLiteral(2)])),
            VarDecl(Id("c"), None, None, ArrayCell(CallExpr(Id("fun"), [NumberLiteral(1), NumberLiteral(2)]), [NumberLiteral(1), NumberLiteral(3)]))
        ]))
        #print(expect)
        self.assertTrue(TestAST.test(input, expect, 330))    
        
        
    def test_50(self):        
        input = """func main() begin
if (1) writeString("1")
elif (2) if(3) writeString("1")
elif (4) writeString("1")
else writeString("1")
end
"""
        expect = """Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"""
        self.assertTrue(TestAST.test(input, expect, 350))            