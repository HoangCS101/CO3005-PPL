import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() begin
            number a
            if (5 < 2) a <- 1
            elif (not true) a <- 2
            elif ("h" == "6") a <- 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
