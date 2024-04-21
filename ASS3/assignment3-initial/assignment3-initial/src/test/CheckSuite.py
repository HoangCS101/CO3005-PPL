import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """func man()
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared(self):
        input = """
        func main()
            begin
                var a <- 4
                var a <- 5
            end
        """
        expect = "Redeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_redeclared_2(self):
        input = """
        var a <- 4
        var a <- 5
        func main()
            begin
            end
        """
        expect = "Redeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_undeclared(self):
        input = """
        func main()
            begin
            a <- 5
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_mustinloop(self):
        input = """
        func main()
        begin
            var i <- 0
            for i until i <= 10 by 2
            begin
                var j <- 0
            end
            break
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_undeclared_2(self):
        input = """
        func main()
        begin
            for i until i <= 10 by 2
            begin
                var j <- 0
            end
            break
        end
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test_typemismatch(self):
        input = """
        func main()
        begin
            number a <- 0
            a <- a + true
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 406))