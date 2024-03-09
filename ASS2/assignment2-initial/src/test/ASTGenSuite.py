import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """func main()
        begin 
        if (a = b) 
            number a
        elif (a > b)
            begin
                if a - b = 4
                    begin
                        a <- b * 123.e45
                        return 1
                    end
                elif a - b = 3
                    return 2
                else 
                    return 3
            break
            end ## test break
        elif (a + b = 10)
            return 4
        else return 0
        end
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test_simple_program1(self):
        input = """if (a = b) a + 2
        elif (a = 3) return 5
        elif (a = 4)
            begin
                continue
            end
        else return 100
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test_simple_program2(self):
        input = """number a[5,5] <- [1, 2, 3, 4, 5]
        """
        expect = str(Program([VarDecl(Id("a"), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 302))
