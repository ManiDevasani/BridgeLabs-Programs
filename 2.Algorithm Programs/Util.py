class Util:
    # Finding anagram
    @staticmethod
    def anagram(s1, s2):
        s1 = s1
        s2 = s2
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) == len(s2):
            a = []
            b = []
            for i in s1:
                a.append(i)
            for i in s2:
                b.append(i)
            a.sort()
            b.sort()
            if a == b:
                print("Given string is Anagram")
            else:
                print("Given string is not Anagram")
        else:
            print("Given strings are different length")

    # Finding prime number s between 1 to 1000
    @staticmethod
    def primenum(a):
        a = [2]
        polin = []
        for i in range(3, 10):
            if i % 2 != 0:
                a.append(i)
        for i in range(10, 1000):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
                a.append(i)
        print("Prime Numbers in range 1 to 1000 are : ")
        print(a)
        for i in a:
            if i > 0:
                s = str(i)
                rev = ''.join(reversed(s))
                if rev == s:
                    polin.append(s)
        print("Palindrome Numbers are : ")
        print(polin)

    # Finding the day of the date
    @staticmethod
    def dayOfWeek(y, m, d):
        y0 = 0
        x = 0
        m0 = 0
        d0 = 0
        if d <= 31 and m < 12:
            y0 = y - 14 - m / 12
            x = y0 + y0 / 4 - y0 / 100 + y0 / 400
            m0 = m + 12 * 14 - m / 12 - 2
            d0 = int((d + x + 31 * m0 / 12) % 7 - 1)
            if d0 == 0:
                print("Sunday")
            elif d0 == 1:
                print("Monday")
            elif d0 == 2:
                print("Tuesday")
            elif d0 == 3:
                print("Wednesay")
            elif d0 == 4:
                print("Thrusday")
            elif d0 == 5:
                print("Friday")
            elif d0 == 6:
                print("Saturday")
        else:
            print("Wrong input")

    # Using for temperature Conversion for fahrenheit to cecelsiusice-verse
    @staticmethod
    def temperatureConversion(t, type):
        type = type.lower()
        if type == "c":
            f = f = t * 9 / 5 + 32
            print("Fahrenheit Temp : ", f)
        elif type == "f":
            c = (t - 32) * (5 / 9)
            print("Centigrade Temp : ", c)
        else:
            print("Wrong Input")

    # Using for monthly payments
    @staticmethod
    def monthlyPayment(P, Y, R):
        r = int(R / (12 * 100))
        n = 12 * Y
        div = 1 - (1 + r) ** (-n)
        if div != 0:
            payment = float(P * r / div)
            print("The monthly payments would have to make over", Y, "years", P, "principal", R, "percent is :",
                  payment)
        else:
            print("Payment is : 0")

    # Finding the square root of the number
    @staticmethod
    def sqrt(c):
        import math
        t = c
        count = 0
        epsilon = 0.00278
        var1 = abs(t - (c / t))
        var2 = epsilon * t
        while var1 > var2:
            count += 1
            t = ((c / t) + t) / 2
            if c % t == 0:
                print(t)
                break
            if count == 30:
                break
        if count == 30:
            print("Given no is not perfect square")

    # For converting Decimal number to binary number
    @staticmethod
    def __toBinary__(num):
        list = []
        n = 0
        while num > 0:
            n = num % 2
            list.append(n)
            num = int(num / 2)
        list.reverse()
        return list

    # For finding the given number in list using binary search
    @staticmethod
    def binarysearchint(list, num):
        l = 0
        u = int(len(list) - 1)
        while l <= u:
            mid = int(l + u) // 2
            pos = (num == list[mid])
            if pos:
                return "Fount at index :", mid
            if pos != True and pos > 0:
                l = mid + 1
            else:
                u = mid - 1

    # For finding the given String in list using binary search
    @staticmethod
    def binarySearchString(list, string):
        l = 0
        u = int(len(list))
        while l <= u:
            mid = int(l + u - 1 / 2)
            pos = (string == list[mid])
            if pos:
                return "Fount at index :", mid
            if pos != True and pos > 0:
                l = mid + 1
            else:
                u = mid - 1

    # sorting the list using bubble sort
    @staticmethod
    def bubbleSortInt(list):
        for i in range(len(list) - 1, 0, -1):
            for j in range(i):
                if list[j] > list[j + 1]:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp
        return list

    # sorting the list using bubble sort
    @staticmethod
    def bubbleSortStr(list):
        for i in range(len(list) - 1, 0, -1):
            for j in range(i):
                if list[j] > list[j + 1]:
                    temp = list[j]
                    list[j] = list[j + 1]
                    list[j + 1] = temp
        return list

    # sorting the list using insertion sort
    @staticmethod
    def insertionsortInt(list):
        for i in range(0, len(list)):
            j = i + 1
            for j in range(len(list)):
                if list[i] < list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        return list

    # sorting the list using insertion sort
    @staticmethod
    def insertionsortStr(list):
        for i in range(0, len(list)):
            j = i + 1
            for j in range(len(list)):
                if list[i] < list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        return list
