import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test300(self):
        input = """number HoangLe
        """
        expect = str(Program([
            VarDecl(Id("HoangLe"), NumberType())
        ]))
        self.assertTrue(TestAST.test(input, expect, 300))


    def test301(self):
        input = """number HoangLe <- 2110182
        """
        expect = str(Program([
            VarDecl(Id("HoangLe"), NumberType(), None, NumberLiteral(2110182.0))
            ]))
        self.assertTrue(TestAST.test(input, expect, 301))


    def test302(self):
        input = """string str
        bool flg <- true"""
        expect = str(Program([
            VarDecl(Id("str"), StringType()), 
            VarDecl(Id("flg"), BoolType(), None, BooleanLiteral(True)
            )])
        )
        self.assertTrue(TestAST.test(input, expect, 302))


    def test303(self):
        input = """string str[1,1] <- meatball
        """
        expect = str(Program([
            VarDecl(Id("str"), ArrayType([1.0, 1.0], StringType()), None, Id("meatball"))
            ]))
        self.assertTrue(TestAST.test(input, expect, 303))


    def test304(self):
        input = """bool nah[1] <- iWin
        number ded[3,4,5]
        """
        expect = str(Program([
            VarDecl(Id("nah"), ArrayType([1.0], BoolType()), None, Id("iWin")), 
            VarDecl(Id("ded"), ArrayType([3.0, 4.0, 5.0], NumberType()))
            ]))
        self.assertTrue(TestAST.test(input, expect, 304))


    def test305(self):
        input = """var JoJo <- OraOra
        string Dio <- Za("Wa","RuDo")
        """
        expect = str(Program([
            VarDecl(Id("JoJo"), None, "var", Id("OraOra")), 
            VarDecl(Id("Dio"), StringType(), None, CallExpr(Id(("Za")), [StringLiteral("Wa"), StringLiteral("RuDo")]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 305))


    def test306(self):
        input = """dynamic ligma <- "baguette" + "NOW!"
        """
        expect = str(Program([
            VarDecl(Id("ligma"), None, "dynamic", BinaryOp("+", StringLiteral("baguette"), StringLiteral("NOW!")))
            ]))
        self.assertTrue(TestAST.test(input, expect, 306))


    def test307(self):
        input = """func main()
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], None)
            ]))
        self.assertTrue(TestAST.test(input, expect, 307))


    def test308(self):
        input = """func main()
        begin
        end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([]))]))
        self.assertTrue(TestAST.test(input, expect, 308))


    def test309(self):
        input = """func main()
        begin
        break
        end"""
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([Break()]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 309))


    def test310(self):
        input = """
            func main(number a)
            func main(number a, string a, bool a[2])
            func main(number leeX[1,2])
                return"""
        expect = str(Program([
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType())], None),
                    FuncDecl(Id("main"), [VarDecl(Id("a"), NumberType()), 
                                        VarDecl(Id("a"), StringType()), 
                                        VarDecl(Id("a"), ArrayType([2.0], BoolType()))], None),
                    FuncDecl(Id("main"), [VarDecl(Id("leeX"), ArrayType([1.0, 2.0], NumberType()))], Return(None))
                ]))
        self.assertTrue(TestAST.test(input, expect, 310))


    def test311(self):
        input = """
            var x <- 1
            var x <- "123"
            var x <- true
            var x <- false
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  NumberLiteral(1.0)),
                    VarDecl(Id("x"), None, "var",  StringLiteral("123")),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(True)),
                    VarDecl(Id("x"), None, "var",  BooleanLiteral(False))
                ]))
        self.assertTrue(TestAST.test(input, expect, 311))


    def test312(self):
        input = """
        var x[2] <- [1, "fish", false, false]
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([NumberLiteral(1.0), StringLiteral("fish"), BooleanLiteral(False), BooleanLiteral(False)]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 312))


    def test313(self):
        input = """
            var x <- [[2], [456]]
            var x <- [[71]]
            """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(2.0)]), ArrayLiteral([NumberLiteral(456.0)])])),
                    VarDecl(Id("x"), None, "var",  ArrayLiteral([ArrayLiteral([NumberLiteral(71.0)])]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 313))


    def test314(self):
        input = """
            var x <- 1 ... "thunder"
            var x <- 1 <= "zigzag"
            var x <- 1 and 2 or 69
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", NumberLiteral(1.0), StringLiteral("thunder"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("<=", NumberLiteral(1.0), StringLiteral("zigzag"))),
                    VarDecl(Id("x"), None, "var",  BinaryOp("or", BinaryOp("and", NumberLiteral(1.0), NumberLiteral(2.0)), NumberLiteral(69.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 314))


    def test315(self):
        input = """
        var x <- not ahamove[4*4] ... 16
        """
        expect = str(Program([
                    VarDecl(Id("x"), None, "var",  BinaryOp("...", UnaryOp("not", ArrayCell(Id("ahamove"), [BinaryOp("*", NumberLiteral(4.0), NumberLiteral(4.0))])), NumberLiteral(16.0)))
                ]))
        self.assertTrue(TestAST.test(input, expect, 315))


    def test316(self):
        input = """
        var you <- me(meat())
        """
        expect = str(Program([
                    VarDecl(Id("you"), None, "var",  CallExpr(Id("me"), [CallExpr(Id("meat"), [])]))
                ]))
        self.assertTrue(TestAST.test(input, expect, 316))


    def test317(self):
        input = """
        func main()
            begin
                var c <- 56e3
                dynamic d <- 3.14
                dynamic halo
                number three[3e3] <- 3.3
                string meep[3.00]
            end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], Block([
                VarDecl(Id("c"), None, "var", NumberLiteral(56000.0)), 
                VarDecl(Id("d"), None, "dynamic", NumberLiteral(3.14)), 
                VarDecl(Id("halo"), None, "dynamic"),
                VarDecl(Id("three"), ArrayType([3000.0], NumberType()), None, NumberLiteral(3.3)),
                VarDecl(Id("meep"), ArrayType([3.00], StringType()), None)
                ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 317))


    def test318(self):
        input = """
        number a <- 100

        func sum(number n)
        begin
            if (n = 0) return 0
            return n + sum(n - 1)
        end

        func main()
        begin
            writeNumber(sum(a))
        end
        """
        expect = str(Program([
            VarDecl(Id("a"), NumberType(), None, NumberLiteral(100.0)), 
            FuncDecl(Id("sum"), [VarDecl(Id("n"), NumberType())], 
                    Block([
                        If(BinaryOp("=", Id("n"), NumberLiteral(0.0)), Return(NumberLiteral(0.0)), [], None), 
                        Return(BinaryOp("+", Id("n"), CallExpr(Id("sum"), [BinaryOp("-", Id("n"), NumberLiteral(1.0))])))
                        ])), 
            FuncDecl(Id("main"), [], Block([CallStmt(Id("writeNumber"), [CallExpr(Id("sum"), [Id("a")])])]))]))
        self.assertTrue(TestAST.test(input, expect, 318))


    def test319(self):
        input = """
        number bob[2,3] <- lik[4, 5]
        """
        expect = str(Program([
            VarDecl(Id("bob"), ArrayType([2.0, 3.0], NumberType()), None, 
                    ArrayCell(Id("lik"), [NumberLiteral(4.0), NumberLiteral(5.0)]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 319))


    def test320(self):
        input = """
        var a55[2,3] <- [[1, 2, 3] , [4, 5,6]]
        """
        expect = str(Program([
            VarDecl(Id("a55"), None, "var", 
                    ArrayLiteral([
                        ArrayLiteral([NumberLiteral(1.0), NumberLiteral(2.0), NumberLiteral(3.0)]), 
                        ArrayLiteral([NumberLiteral(4.0), NumberLiteral(5.0), NumberLiteral(6.0)])]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 320))


    def test321(self):
        input = """
        func main()
                begin
                    if (true)
                        if(true) return 1
                        elif (true) return 1
                        else return 1
                    elif (true) return 1
                    elif (true) return 1   
                end

        """
        expect = str(Program([FuncDecl(Id("main"), [], Block([
            If(BooleanLiteral(True), 
            If(BooleanLiteral(True), Return(NumberLiteral(1.0)), [(BooleanLiteral(True),Return(NumberLiteral(1.0)))], Return(NumberLiteral(1.0)))
            , [(BooleanLiteral(True),Return(NumberLiteral(1.0))), (BooleanLiteral(True),Return(NumberLiteral(1.0)))], None)
            ]))]))
        self.assertTrue(TestAST.test(input, expect, 321))


    def test322(self):
        input = """
        func main()
        begin
            var i <- 0
            number j <- 0
            for i until i <= 10 by 2
            begin
                for j until j <= 20 by 4
                    writeNumber(i*j)
            end
        end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], 
                    Block([
                        VarDecl(Id("i"), None, "var", NumberLiteral(0.0)), 
                        VarDecl(Id("j"), NumberType(), None, NumberLiteral(0.0)), 
                        For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(10.0)), NumberLiteral(2.0), 
                        Block([
                            For(Id("j"), BinaryOp("<=", Id("j"), NumberLiteral(20.0)), NumberLiteral(4.0), CallStmt(Id("writeNumber"), [BinaryOp("*", Id("i"), Id("j"))]))
                            ]))
                        ]))
            ]))
        self.assertTrue(TestAST.test(input, expect, 322))


    def test323(self):
        input = """
        var str <- "Hello world!"
        """
        expect = str(Program([VarDecl(Id("str"), None, "var", StringLiteral("Hello world!"))]))
        self.assertTrue(TestAST.test(input, expect, 323))


    def test324(self):
        input = """
        func main() return 1
        """
        expect = str(Program([FuncDecl(Id("main"), [], Return(NumberLiteral(1.0)))]))
        self.assertTrue(TestAST.test(input, expect, 324))


    def test325(self):
        input = """
        func main()
        begin
            var i <- 770
            number j <- 0.35
            for i until i <= 1000 by 41
            begin
                for j until j <= 20 by 4
                    writeString(i and j)
            end
        end
        """
        expect = str(Program([
            FuncDecl(Id("main"), [], 
                    Block([
                        VarDecl(Id("i"), None, "var", NumberLiteral(770.0)), 
                        VarDecl(Id("j"), NumberType(), None, NumberLiteral(0.35)), 
                        For(Id("i"), BinaryOp("<=", Id("i"), NumberLiteral(1000.0)), NumberLiteral(41.0), 
                        Block([
                            For(Id("j"), BinaryOp("<=", Id("j"), NumberLiteral(20.0)), NumberLiteral(4.0), CallStmt(Id("writeString"), [BinaryOp("and", Id("i"), Id("j"))]))
                            ]))
                        ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 325))


    def test326(self):
        input = """
        var yawanna <- "SigmaDuck"
        """
        expect = str(Program([VarDecl(Id("yawanna"), None, "var", StringLiteral("SigmaDuck"))]))
        self.assertTrue(TestAST.test(input, expect, 326))


    def test327(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 327))


    def test328(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 328))


    def test329(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 329))


    def test330(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 330))


    def test331(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 331))


    def test332(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 332))


    def test333(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 333))


    def test334(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 334))


    def test335(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 335))


    def test336(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 336))


    def test337(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 337))


    def test338(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 338))


    def test339(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 339))


    def test340(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 340))


    def test341(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 341))


    def test342(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 342))


    def test343(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 343))


    def test344(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 344))


    def test345(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 345))


    def test346(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 346))


    def test347(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 347))


    def test348(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 348))


    def test349(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 349))


    def test350(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 350))


    def test351(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 351))


    def test352(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 352))


    def test353(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 353))


    def test354(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 354))


    def test355(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 355))


    def test356(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 356))


    def test357(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 357))


    def test358(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 358))


    def test359(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 359))


    def test360(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 360))


    def test361(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 361))


    def test362(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 362))


    def test363(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 363))


    def test364(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 364))


    def test365(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 365))


    def test366(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 366))


    def test367(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 367))


    def test368(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 368))


    def test369(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 369))


    def test370(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 370))


    def test371(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 371))


    def test372(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 372))


    def test373(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 373))


    def test374(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 374))


    def test375(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 375))


    def test376(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 376))


    def test377(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 377))


    def test378(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 378))


    def test379(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 379))


    def test380(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 380))


    def test381(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 381))


    def test382(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 382))


    def test383(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 383))


    def test384(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 384))


    def test385(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 385))


    def test386(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 386))


    def test387(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 387))


    def test388(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 388))


    def test389(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 389))


    def test390(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 390))


    def test391(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 391))


    def test392(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 392))


    def test393(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 393))


    def test394(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 394))


    def test395(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 395))


    def test396(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 396))


    def test397(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 397))


    def test398(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 398))


    def test399(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 399))
