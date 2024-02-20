import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test201(self):
        input = """number a[5] <- [1, 2, 3, 4, 5]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 201 ))

    def test202(self):
        input = """number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 202 ))

    def test203(self):
        input = """a[3 + foo(2)] <- a[b[2, 3]] + 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 203 ))

    def test204(self):
        input = """func foo(number a[5], string b)
        begin
        var i <- 0
        for i until i >= 5 by 1
        begin
        a[i] <- i * i + 5
        end
        return -1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 204 ))

    def test205(self):
        input = """aPI <- 3.14
        l[3] <- value * aPi
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 205 ))

    def test206(self):
        input = """if (a == 69) for c until c >= 20 by 96 return
        elif (b = 420) kakanku <- 123
        elif (ambatunat = "imbacsi~") continue
        elif (true == false) break
        else print("breaking bad")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 206 ))

    def test207(self):
        input = """begin
        number r
        number s
        r <- 2.0
        number a[5]
        number b[5]
        s <- r * r * 3.14
        a[0] <- s
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 207 ))

    def test208(self):
        input = """func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                
                if (areDivisors(num1, num2)) writeString("Yes")
                else writeString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 208 ))

    def test209(self):
        input = """func isPrime(number x)
        
        func main()
            begin
                number x <- readNumber()
                if (isPrime(x)) writeString("Yes")
                else writeString("No")
            end
        
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
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 209 ))

    def test210(self):
        input = """number x <- readNumber()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 210 ))

    def test211(self):
        input = """number abC <- 5 - 71 % 2 + hue(6, color(90))
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 211 ))

    def test212(self):
        input = """number mrLee <- randomArray[12]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 212 ))

    def test213(self):
        input = """32 / 3 + 91 % foo(a[345] - foo(4 % 6) , 113) / bv2ld[666]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 213 ))

    def test214(self):
        input = """72 / 7 + 111 %* aiue * aaa[333] / 2
        """
        expect = "Error on line 1 col 14: *"
        self.assertTrue(TestParser.test(input,expect, 214 ))

    def test215(self):
        input = """ true and FACT or not Cul
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 215 ))

    def test216(self):
        input = """false or not (true and true or Hector)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 216 ))

    def test217(self):
        input = """not (ME and U)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 217 ))

    def test218(self):
        input = """not not much and chicken
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 218 ))

    def test219(self):
        input = """not and nothing or everything
        """
        expect = "Error on line 1 col 4: and"
        self.assertTrue(TestParser.test(input,expect, 219 ))

    def test220(self):
        input = """ \"day with no quaso\" ... \"is saddest day\"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 220 ))

    def test221(self):
        input = """ \"you should treat yourself\" ... \"NOW\" ... \"thunder sound effect\"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 221 ))

    def test222(self):
        input = """ \" here goes nothing\" ...
        """
        expect = "Error on line 1 col 25: \n\n"
        self.assertTrue(TestParser.test(input,expect, 222 ))

    def test223(self):
        input = """3 * 2 >= 6
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 223 ))

    def test224(self):
        input = """ true != false
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 224 ))

    def test225(self):
        input = """ 1 <== 3
        """
        expect = "Error on line 1 col 5: ="
        self.assertTrue(TestParser.test(input,expect, 225 ))

    def test226(self):
        input = """ a[2 , 2] <- a + 56 - iluvhen(a[11] + 45)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 226 ))

    def test227(self):
        input = """ a[4 , 9] <- func fusion(0.e456)
        """
        expect = "Error on line 1 col 13: func"
        self.assertTrue(TestParser.test(input,expect, 227 ))

    def test228(self):
        input = """fucncalla(a[444] , true , \"genGAY\")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 228 ))

    def test229(self):
        input = """callfuncwrong(number Hitloan , 78)
        """
        expect = "Error on line 1 col 14: number"
        self.assertTrue(TestParser.test(input,expect, 229 ))

    def test230(self):
        input = """jpee(L44 , false
        """
        expect = "Error on line 1 col 16: \n\n"
        self.assertTrue(TestParser.test(input,expect, 230 ))

    def test231(self):
        input = """var interMAN
        """
        expect = "Error on line 1 col 12: \n\n"
        self.assertTrue(TestParser.test(input,expect, 231 ))

    def test232(self):
        input = """var interMAN <- \"need coffee\"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 232 ))

    def test233(self):
        input = """dynamic musshi
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 233 ))

    def test234(self):
        input = """dynamic thundercloud <- 34567.e-3334
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 234 ))

    def test235(self):
        input = """bool arrash[5] <- [true,false,false,false,true]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 235 ))

    def test236(self):
        input = """string alanWake <- [444]
        """
        expect = "Error on line 1 col 19: ["
        self.assertTrue(TestParser.test(input,expect, 236 ))

    def test237(self):
        input = """string BigBang[3] <- [\"haru haru\",\"blue\",\"loser\"]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 237 ))

    def test238(self):
        input = """func main()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 238 ))

    def test239(self):
        input = """func index(bool true , number DIGIT)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 239 ))

    def test240(self):
        input = """ func decc(bool apex) return 100
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 240 ))

    def test241(self):
        input = """func yandex(number code)
        begin
            sussyImage <- Chiori
            return insanity
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 241 ))

    def test242(self):
        input = """func ffufufuuf() begin
        smocc == sad
        return ressin
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect, 242 ))

    def test243(self):
        input = """continue
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 243 ))

    def test244(self):
        input = """pytago <- a2 + b2 = c2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 244 ))

    def test245(self):
        input = """if (U == gay) Away()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 245 ))

    def test246(self):
        input = """if (true == false) NAH()
        elif (false == false) yield = yeet
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect, 246 ))

    def test247(self):
        input = """bool dream
        if (I and U == true) dream = true
        else dream = false
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 247 ))

    def test248(self):
        input = """for Time until Eternity by Second ThinkOf(You)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 248 ))

    def test249(self):
        input = """for time until by 12 break
        """
        expect = "Error on line 1 col 15: by"
        self.assertTrue(TestParser.test(input,expect, 249 ))

    def test250(self):
        input = """ return 555-444*calling(\"number meat\")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 250 ))

    def test251(self):
        input = """begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 251 ))

    def test252(self):
        input = """func areDivisors(number num1, number num2)
        return ((num1 % num2 = 0) or (num2 % num1 = 0))

        func main()
        begin
            var num1 <- readNumber()
            var num2 <- readNumber()

            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 252 ))

    def test253(self):
        input = """func add(number x, number y)
        return x + y

        func subtract(number x, number y)
        return x - y

        func multiply(number x, number y)
        return x * y

        func divide(number x, number y)
        return x / y
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 253 ))

    def test254(self):
        input = """var isTrue <- true
        var isFalse <- false

        if (isTrue and (not isFalse)) writeString("Boolean expression: True")
        else writeString("Boolean expression: False")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 254 ))

    def test255(self):
        input = """func isPrime(number n)
        begin
            if (n <= 1) return false
            for i until n by 1
                if ((i > 1) and (n % i = 0)) return false
            return true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 255 ))

    def test256(self):
        input = """func factorial(number n)
        begin
            if (n <= 1) return 1
            else return n * factorial(n - 1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 256 ))

    def test257(self):
        input = """var fact <- factorial(input)
        writeString("Factorial: ")
        writeNumber(fact)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 257 ))

    def test258(self):
        input = """var numbers[5] <- [1, 2, 3, 4, 5]
        writeString("Array elements: ")
        for i until 5 by 1
            writeNumber(numbers[i])
            writeString(",")
        """
        expect = "Error on line 1 col 11: [" # implicit keywords cannot be used here
        self.assertTrue(TestParser.test(input,expect, 258 ))

    def test259(self):
        input = """number numbers[5] <- [1, 2, 3, 4, 5]
        writeString("Array elements: ")
        for i until 5 by 1
            writeNumber(numbers[i])
            writeString(",")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 259 ))

    def test260(self):
        input = """var greeting <- "Hello"
        var name <- "World"
        var message <- greeting + " " + name + "!"
        writeString(message)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 260 ))

    def test261(self):
        input = """begin
        var x <- 10
        writeString("Inside block: ")
        writeNumber(x)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 261 ))

    def test262(self):
        input = """func fibonacci(number n)
        begin
            if (n <= 1) return n
            else return fibonacci(n - 1) + fibonacci(n - 2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 262 ))

    def test263(self):
        input = """func main()
        begin
            writeString("Enter a number for Fibonacci: ")
            var fibInput <- readNumber()
            var fibResult <- fibonacci(fibInput)
            writeString("Fibonacci result: ")
            writeNumber(fibResult)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 263 ))

    def test264(self):
        input = """func isEven(number x)
        return (x % 2 = 0)

        func main()
        begin
            writeString("Enter a number to check if it's even: ")
            var num <- readNumber()

            if (isEven(num)) writeString("The number is even")
            else writeString("The number is odd")
            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 264 ))

    def test265(self):
        input = """func main() return true or false
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 265 ))

    def test266(self):
        input = """func main()
        begin
            writeString("NumberArray: ")
            for i until 5 by 1
                writeNumber(i)
                writeString(",")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 266 ))

    def test267(self):
        input = """func main()
        begin
            writeString("NumberArray: ")
            for i until 9 by 1
                writeNumber(i + 124)
                writeString("1003")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 267 ))

    def test268(self):
        input = """printf(\" I love baguette \")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 268 ))

    def test269(self):
        input = """my_bool = True 
        my_bool = False

        bool(0)
        ## => False
        bool(1)
        ## => True
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 269 ))

    def test270(self):
        input = """string list1[3] <- ["apple", "banana", "cherry"]
        bool list2[3] <- [true, false, false]
        number list3[5] <- [1, 5, 7, 9, 3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 270 ))

    def test271(self):
        input = """number myList[7] <- [9, 5, 4, 1, 3, 2]
        heapify(myList)
        print(myList)
        print(myList[0])

        heappush(myList, 10)
        x = heappop(myList)
        print(x)

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 271 ))

    def test272(self):
        input = """number myList[\"7\"] <- [9, 5, 4, 1, 3, 2]
        heapify(myList)
        print(myList)
        print(myList[0])

        heappush(myList, 10)
        x = heappop(myList)
        print(x)

        """
        expect = "Error on line 1 col 22: ["
        self.assertTrue(TestParser.test(input,expect, 272 ))

    def test273(self):
        input = """writeString("Enter your name: ")
        string name <- readString()
        print(name)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 273 ))

    def test274(self):
        input = """65 - 123 % fool(\"number five\") + 111 * a[3,5]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 274 ))

    def test275(self):
        input = """func recursion(number a)
        if (a >= 100) return a + recursion(a - 1)
        else return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 275 ))

    def test276(self):
        input = """begin
        for i until 81 by 4 + 5 - 8 writeString(\"dwayne the rocc joystick\")
        if (a >= 100) continue
        else break
        func dec(number int, number exp) begin various <- a end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 276 ))

    def test277(self):
        input = """func calcArea(number a, number b)
        begin
            return a * b
        end
        func main()
        begin
            writeString(\"Area is: \")
            number result <- calcArea(6 , 9)
            writeNumber(result)
            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 277 ))

    def test278(self):
        input = """func calcVolume(number length, number width, number height)
        begin
            return length * width * height
        end

        func main()
        begin
            writeString("Enter the length of the rectangular prism: ")
            number prismLength <- readNumber()

            writeString("Enter the width of the rectangular prism: ")
            number prismWidth <- readNumber()

            writeString("Enter the height of the rectangular prism: ")
            number prismHeight <- readNumber()

            writeString("Volume is: ")
            number result <- calcVolume(prismLength, prismWidth, prismHeight)
            writeNumber(result)

            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 278 ))

    def test279(self):
        input = """func calcAbsoluteDifference(number x, number y)
        begin
            var difference <- x - y
            if (difference < 0) return -difference
            else return difference
        end

        func main()
        begin
            writeString("Enter the first number: ")
            number num1 <- readNumber()

            writeString("Enter the second number: ")
            number num2 <- readNumber()

            writeString("Absolute difference is: ")
            number result <- calcAbsoluteDifference(num1, num2)
            writeNumber(result)

            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 279 ))

    def test280(self):
        input = """func fibonacciSequence(number n)
        begin
            var a <- 0
            var b <- 1
            for i until n by 1
                writeNumber(a)
                var temp <- a + b
                a <- b
                b <- temp
            writeString(",")
        end

        func main()
        begin
            writeString("Enter the number of terms for the Fibonacci sequence: ")
            number terms <- readNumber()

            writeString("Fibonacci sequence: ")
            fibonacciSequence(terms)

            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 280 ))

    def test281(self):
        input = """writeString(\"Hello World\")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 281 ))

    def test282(self):
        input = """func concatenateStrings(string str1, string str2)
        begin
            return str1 ... str2
        end

        func main()
        begin
            writeString("Enter the first string: ")
            string input1 <- readString()

            writeString("Enter the second string: ")
            string input2 <- readString()

            writeString("Concatenated string is: ")
            string result <- concatenateStrings(input1, input2)
            writeString(result)

            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 282 ))

    def test283(self):
        input = """func compareStrings(string str1, string str2)
        begin
            if (str1 == str2) return "The strings are equal"
            else return "The strings are not equal"
        end

        func main()
        begin
            writeString("Enter the first string: ")
            string input1 <- readString()

            writeString("Enter the second string: ")
            string input2 <- readString()

            string result <- compareStrings(input1, input2)
            writeString(result)

            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 283 ))

    def test284(self):
        input = """## simple swapping
        if (arr[j] > arr[j + 1]) begin
                var temp <- arr[j]
                arr[j] <- arr[j + 1]
                arr[j + 1] <- temp
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 284 ))

    def test285(self):
        input = """func dontReceiveVal(4,6,8,9)
        """
        expect = "Error on line 1 col 20: 4"
        self.assertTrue(TestParser.test(input,expect, 285 ))

    def test286(self):
        input = """ var noInitialVal
        """
        expect = "Error on line 1 col 17: \n\n"
        self.assertTrue(TestParser.test(input,expect, 286 ))

    def test287(self):
        input = """fomula <- pow(a , 3)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 287 ))

    def test288(self):
        input = """ string Im <- \"the storm that is approaching\"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 288 ))

    def test289(self):
        input = """func isPalindrome(string str)
        begin
            var reversed <- ""
            for i until length(str) by -1
                reversed <- reversed ... str[i - 1]

            return str == reversed
        end

        func main()
        begin
            writeString("Enter a string to check for palindrome: ")
            string input <- readString()

            if (isPalindrome(input)) writeString("Yes, it's a palindrome")
            else writeString("No, it's not a palindrome")

            return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 289 ))

    def test290(self):
        input = """func celsiusToFahrenheit(number celsius)
        begin
            var fahrenheit <- (celsius * 9/5) + 32
            return fahrenheit
        end

        func main()
        begin
            writeString("Enter the temperature in Celsius: ")
            number tempCelsius <- readNumber()

            var tempFahrenheit <- celsiusToFahrenheit(tempCelsius)

            writeString("Temperature in Fahrenheit: ")
            writeNumber(tempFahrenheit)

            return 0
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 290 ))

    def test291(self):
        input = """func kilometersToMiles(number kilometers)
        begin
            var miles <- kilometers * 0.621371
            return miles
        end

        func main()
        begin
            writeString("Enter the distance in kilometers: ")
            number string distanceKm <- readNumber()

            var distanceMiles <- kilometersToMiles(distanceKm)

            writeString("Distance in miles: ")
            writeNumber(distanceMiles)

            return 0
        end

        """
        expect = "Error on line 10 col 19: string"
        self.assertTrue(TestParser.test(input,expect, 291 ))

    def test292(self):
        input = """number rev -> 78
        """
        expect = "Error on line 1 col 12: >"
        self.assertTrue(TestParser.test(input,expect, 292 ))

    def test293(self):
        input = """func calculateTriangleArea(number base, number height)
        begin
            var area <- 0.5 * base * height
            return area
        end

        func calculateHypotenuse(number base, number height)
        begin
            var hypotenuse <- sqrt(pow(base,2) + pow(height,2))
            return hypotenuse
        end

        func main()
        begin
            writeString("Enter the base of the right-angled triangle: ")
            number triangleBase <- readNumber()

            writeString("Enter the height of the right-angled triangle: ")
            number triangleHeight <- readNumber()

            var triangleArea <- calculateTriangleArea(triangleBase, triangleHeight)
            var hypotenuse <- calculateHypotenuse(triangleBase, triangleHeight)

            writeString("Area of the right-angled triangle: ")
            writeNumber(triangleArea)
            
            writeString("Hypotenuse length: ")
            writeNumber(hypotenuse)

            return 0
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 293 ))

    def test294(self):
        input = """func calculateCircleArea(number radius)
        begin
            var area <- 3.14 * pow(radius,2)
            return area
        end

        func calculateCircleCircumference(number radius)
        begin
            var circumference <- 2 * 3.14 * radius
            return circumference
        end

        func main()
        begin
            writeString("Enter the radius of the circle: ")
            number circleRadius <- readNumber()

            var circleArea <- calculateCircleArea(circleRadius)
            var circleCircumference <- calculateCircleCircumference(circleRadius)

            writeString("Area of the circle: ")
            writeNumber(circleArea)
            
            writeString("Circumference of the circle: ")
            writeNumber(circleCircumference)

            return 0
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 294 ))

    def test295(self):
        input = """foo(4 , a) <- 7 - -100
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 295 ))

    def test296(self):
        input = """if (a == c) return 6 elif (b == c) continue else break
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 296 ))

    def test297(self):
        input = """for a until foo() + 3 by 69 if (a == c) break
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 297 ))

    def test298(self):
        input = """func main(number a, number b)
        begin
        return 2
        if (a == c) break
        ## i like cat continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 298 ))

    def test299(self):
        input = """writeString(\"This is last testcase, i shouldn't be wrong\")
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect, 299 ))