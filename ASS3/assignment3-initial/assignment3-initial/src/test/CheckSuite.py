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
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test_redeclared_2(self):
        input = """
        var a <- 4
        var a <- 5
        func main()
            begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 402))