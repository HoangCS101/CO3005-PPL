import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_not_so_simple_program(self):
        input = """func main()
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
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(i), None, var, NumLit(0.0)), VarDecl(Id(j), NumberType, None, NumLit(0.0)), For(Id(i), BinaryOp(<=, Id(i), NumLit(10.0)), NumLit(2.0), Block([For(Id(j), BinaryOp(<=, Id(j), NumLit(20.0)), NumLit(4.0), CallStmt(Id(writeNumber), [BinaryOp(*, Id(i), Id(j))]))]))]))])'''
        self.assertTrue(TestAST.test(input, expect, 300))
    def test_not_so_simple_program(self):
        input = """	var str <- "Hello world!"
        """
        expect = '''Program([VarDecl(Id(str), None, var, StringLit(Hello world!))])'''
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_302(self):
        input = """
func isPrime(number n)
    func main()
    begin
        number x
        if isPrime(x)
            number a
        else
            number b
    end
"""
        expect = "Program([FuncDecl(Id(isPrime), [VarDecl(Id(n), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, None), If((Id(x), VarDecl(Id(a), NumberType, None, None)), [], VarDecl(Id(b), NumberType, None, None))]))])"
        self.assertTrue(TestAST.test(input, expect, 302))
    def test_303(self):
        input = """
"""
        expect = "Program([None])"
        self.assertTrue(TestAST.test(input, expect, 303))
    def test_304(self):
        input = """
func main() begin
number a
if (5 < 2) a <- 1
elif (not true) a <- 2
elif ("h" == "6") a <- 3
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), If((BinaryOp(<, NumLit(5.0), NumLit(2.0)), AssignStmt(Id(a), NumLit(1.0))), [(UnaryOp(not, BooleanLit(True)), AssignStmt(Id(a), NumLit(2.0))), (BinaryOp(==, StringLit(h), StringLit(6)), AssignStmt(Id(a), NumLit(3.0)))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 304))
    def test_305(self):
        input = """number a <- "test"
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, StringLit(test))])"
        self.assertTrue(TestAST.test(input, expect, 305))
    def test_306(self):
        input = """number a <- "test"
"""
        expect = "Program([VarDecl(Id(a), NumberType, None, StringLit(test))])"
        self.assertTrue(TestAST.test(input, expect, 306))
    def test_308(self):
        input = """
func main()
begin
end
"""     
        expect = "Program([FuncDecl(Id(main), [], Block([]))])"
        self.assertTrue(TestAST.test(input, expect, 308))
    def test_309(self):
        input = """
func main()
begin
number a
var b <- a
c <- b
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), None, var, Id(a)), AssignStmt(Id(c), Id(b))]))])"
        self.assertTrue(TestAST.test(input, expect, 309))
    def test_310(self):
        input = """
func main()
number a[3]
"""
        expect = '''Program([FuncDecl(Id(main), [], None), VarDecl(Id(a), NumberType, ArrayType([3.0], None), None)])'''
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_311(self):
        input = """
func main()
begin
number a[3.5]
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, ArrayType([3.5], None), None)]))])'''
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_312(self):
        input = """
func main()
begin
number a[2,3] <- 5
end
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, ArrayType([2.0, 3.0], None), NumLit(5.0))]))])'''
        self.assertTrue(TestAST.test(input, expect, 312))
#     def test_313(self):
#         input = """

# func main()
# begin
# number a[2,3] <- a[5,2]
# end
# """
#         expect = ''''''
#         self.assertTrue(TestAST.test(input, expect, 313))
    def test_314(self):
        input = """
func main()
begin
number a[2] <- [1, "test", true]
"""
        expect = '''Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, ArrayType([2.0], None), ArrayLit(NumLit(1.0), StringLit(test), BooleanLit(True)))]))])'''
        self.assertTrue(TestAST.test(input, expect, 314))
    def test_315(self):
        input = """
func main()
begin
break
continue
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Break, Continue]))])"
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_316(self):
        input = """
func main() begin
if (1) writeString("1")
elif (2) if(3) writeString("1")
elif (4) writeString("1")
else writeString("1")
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((NumLit(1.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(2.0), If((NumLit(3.0), CallStmt(Id(writeString), [StringLit(1)])), [(NumLit(4.0), CallStmt(Id(writeString), [StringLit(1)]))], CallStmt(Id(writeString), [StringLit(1)])))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_317(self):
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
        expect = "Program([VarDecl(Id(a), NumberType, None, NumLit(100.0)), FuncDecl(Id(sum), [VarDecl(Id(n), NumberType, None, None)], Block([If((BinaryOp(=, Id(n), NumLit(0.0)), Return(NumLit(0.0))), [], None), Return(BinaryOp(+, Id(n), CallExpr(Id(sum), [BinaryOp(-, Id(n), NumLit(1.0))])))])), FuncDecl(Id(main), [], Block([CallStmt(Id(writeNumber), [CallExpr(Id(sum), [Id(a)])])]))])"
        self.assertTrue(TestAST.test(input, expect, 317))
    def test_318(self):
        input = """
func isPrime(number x)
    begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
        return true
    end
"""
        expect = "Program([FuncDecl(Id(isPrime), [VarDecl(Id(x), NumberType, None, None)], Block([If((BinaryOp(<=, Id(x), NumLit(1.0)), Return(BooleanLit(False))), [], None), VarDecl(Id(i), None, var, NumLit(2.0)), For(Id(i), BinaryOp(>, Id(i), BinaryOp(/, Id(x), NumLit(2.0))), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(x), Id(i)), NumLit(0.0)), Return(BooleanLit(False))), [], None)])), Return(BooleanLit(True))]))])"
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = """
func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
    end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, None), VarDecl(Id(num2), None, var, None), If((CallExpr(Id(areDivisors), [Id(num1), Id(num2)]), CallStmt(Id(writeString), [StringLit(Yes)])), [], CallStmt(Id(writeString), [StringLit(No)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = """
func main()
begin
    var num1 <- var num2
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(num1), None, var, None)]))])"
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = """
func main()
return main
"""
        expect = "Program([FuncDecl(Id(main), [], Return(Id(main)))])"
        self.assertTrue(TestAST.test(input, expect, 321))
    
    def test_322(self):
        input = """
## test comments
"""
        expect = "Program([None])"
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = """
var x <- [[1], [1]]
var x <- [[1]]
"""
        expect = "Program([VarDecl(Id(x), None, var, ArrayLit(ArrayLit(NumLit(1.0)), ArrayLit(NumLit(1.0)))), VarDecl(Id(x), None, var, ArrayLit(ArrayLit(NumLit(1.0))))])"
        self.assertTrue(TestAST.test(input, expect, 323))
    def test_324(self):
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
        expect = '''Program([VarDecl(Id(x), None, var, BinaryOp(..., NumLit(1.0), StringLit(2))), VarDecl(Id(x), None, var, BinaryOp(<=, NumLit(1.0), StringLit(2))), VarDecl(Id(x), None, var, BinaryOp(or, BinaryOp(and, NumLit(1.0), NumLit(2.0)), NumLit(3.0))), VarDecl(Id(x), None, var, BinaryOp(-, BinaryOp(+, NumLit(1.0), NumLit(2.0)), NumLit(3.0))), VarDecl(Id(x), None, var, BinaryOp(%, BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(2.0)), NumLit(3.0)), NumLit(4.0))), VarDecl(Id(x), None, var, UnaryOp(-, UnaryOp(-, UnaryOp(-, NumLit(1.0))))), VarDecl(Id(x), None, var, UnaryOp(not, UnaryOp(not, NumLit(1.0)))), VarDecl(Id(x), None, var, Id(x)), VarDecl(Id(x), None, var, ArrayCell(None, [NumLit(1.0)]))])'''
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = """
func foo(string b, bool c)
begin
var i <- 0
for i until i >= 5 by 1
begin
a[i] <- i * i + 5
end
return -1
end
"""
        expect = "Program([FuncDecl(Id(foo), [VarDecl(Id(a), NumberType, ArrayType([5.0], None), None), VarDecl(Id(b), StringType, None, None)], Block([VarDecl(Id(i), None, var, NumLit(0.0)), For(Id(i), BinaryOp(>=, Id(i), NumLit(5.0)), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(a), [Id(i)]), BinaryOp(+, BinaryOp(*, Id(i), Id(i)), NumLit(5.0)))])), Return(UnaryOp(-, NumLit(1.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 325))
