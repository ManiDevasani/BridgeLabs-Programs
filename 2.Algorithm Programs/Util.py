"""""
------------------------------------------------------------------------------------------------------------------
1.One string is an anagram of another if the second is simply a
rearrangement of the first. For example, 'heart' and 'earth' are anagrams...
2.Take a range of 0 - 1000 Numbers and find the Prime numbers in that range..
3.Extend the above program to find the prime numbers that are Anagram and
Palindrome.
4.To the Util Class add dayOfWeek static function that takes a date as input and
prints the day of the week that date falls on. Your program should take three
command-line arguments: m (month), d (day), and y (year). For m use 1 for January,
2 for February, and so forth. For output print 0 for Sunday, 1 for Monday, 2 for
Tuesday, and so forth. Use the following formulas, for the Gregorian calendar (where
/ denotes integer division):
y 0 = y − (14 − m ) / 12
x = y 0 + y 0 /4 − y 0 /100 + y 0 /400
m 0 = m + 12 × ((14 − m ) / 12) − 2
d 0 = ( d + x + 31 m 0 / 12) mod 7
5.To the Util Class add temperaturConversion static function, given the temperature
in fahrenheit as input outputs the temperature in Celsius or viceversa using the
formula
Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
Fahrenheit to Celsius: (°F − 32) x 5/9 = °C
6.Write a Util Static Function to calculate monthlyPayment that reads in three
command-line arguments P, Y, and R and calculates the monthly payments you
would have to make over Y years to pay off a P principal loan amount at R per cent
interest compounded monthly
7.Write a Util Static Function to calculate monthlyPayment that reads in three
command-line arguments P, Y, and R and calculates the monthly payments you
would have to make over Y years to pay off a P principal loan amount at R per cent
interest compounded monthly
8.Write a static function toBinary that outputs the binary (base 2) representation of
the decimal number typed as the input. It is based on decomposing the number into
a sum of powers of 2
9.  i.binarySearch method for integer
    ii. binarySearch method for String
    iii. insertionSort method for integer
    iv. insertionSort method for String
    v. bubbleSort method for integer
    vi. bubbleSort method for String

------------------------------------------------------------------------------------------------------------------
"""

class Util:
    # ----------------------   Finding anagram  -------------------------------------
    @staticmethod
    def anagram(a, b):
        import math
        # Taking two empty arrays for checking the euqals condition
        a1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        temp1 = a
        # this while loop is increment the values in array a1
        while (temp1 != 0):
            r = math.floor(temp1 % 10)
            a1[r] += 1
            temp1 = math.floor(temp1 / 10)
        temp2 = b
        # this loop increment the values in array a2
        while (temp2 != 0):
            r = math.floor(temp2 % 10)
            a2[r] += 1
            temp2 = math.floor(temp2 / 10)
        # if both arrays are equals then the given strings are  anagram
        if (a1 == a2):
            return True
        else:
            return False
    # -------------------------  Finding prime numbers betwween 1 to 1000  ---------------------------
    @staticmethod
    def primenum():
        a = []
        polin = []
        anagram = []
        # Finding the prime numbers and storing in an array 'a'
        for i in range(2 ,1000):
            count = 0
            num = i
            for num in range(2,(i//2+1)):
                # Everey time it checks the remainder '0' if it is '0' it is a prime number
                if i%num ==0:
                    count+=1
            if count==0 and i!=1:
                a.append(i)
        print("Prime Numbers in range 1 to 1000 are : ")
        print(a)
        for i in a:
            if(i>10):
                s = str(i)
                # By using the join keyword finding the polindrome strings and stroring in the array 'polindrome'
                rev = ''.join(reversed(s))
                if(rev==s):
                    polin.append(s)
        for i in range(0,len(a)):
            for j in range(i+1,len(a)):
                # Every time passing the two strings to the anagram method until the length of the array 'a' and the resultant
                # storing in a new array anagram
                if(Util.anagram(a[i],a[j])):
                    anagram.append(a[i])
                    anagram.append(a[j])
        print("Polindrome between 0 to 100 are : ")
        print(polin)
        print("Anagarams between 0 to 100 are : ")
        print(anagram)
    # -------------------------------  Finding the day of the date  ----------------------------------------------------
    @staticmethod
    def dayOfWeek(y,m,d):
        # this mehtod takes input  date,month,year
        y0 = 0
        x = 0
        m0 = 0
        d0 = 0
        if(d<=31 and m<12):
            # Using the gauss formulas finding the d0 value from which the day is finfing out
            y0 = y-14-m/12
            x = y0 + y0 / 4 - y0 / 100 + y0 / 400
            m0 = m + 12 * 14 - m / 12 - 2
            d0 = int((d + x + 31 * m0 / 12) % 7-1)
            # fro 0-6 ht edays will ordrerd as follows
            if(d0==0):
                print("Sunday")
            elif (d0 == 1):
                print("Monday")
            elif (d0 == 2):
                print("Tuesday")
            elif (d0 == 3):
                print("Wednesay")
            elif (d0 == 4):
                print("Thrusday")
            elif (d0 == 5):
                print("Friday")
            elif (d0 == 6):
                print("Saturday")
        else:
                print("Wrong input")
    # ----------------  Using for temperature Conversion for faherienheit to celsis vice-verse  ------------------------
    @staticmethod
    def temperatureConversion(t,type):
        # this method takes temperature value and the type to which to convert
        # changing ht case of the type. then it will accepts any case
        type = type.lower()
        # if the given conversion is to centigrade by uding the conversion formula change the value and printing the values
        if(type=="c"):
            f = f = t*9/5+32
            print("Fahrenheit Temp : ",f)
            # if the given conversion is to farheinheit by uding the conversion formula change the value and printing the values
        elif(type=="f"):
            c = (t-32)*(5/9)
            print("Centigrade Temp : ", c);
        else:
            print("Wrong Input")
    # ----------------------------------  Using for monthly payments  --------------------------------------------------
    @staticmethod
    def monthlyPayment(P,Y,R):
        # this mehtod takes input principle amount,year,rate of intert
        # Using given formulas substituing the pyr values to find out the payment
        r = int(R/(12*100))
        n = 12*Y
        div = 1-(1+r)**(-n)
        if(div!=0):
            payment = float(P*r/div)
            print("The monthly payments would have to make over", Y, "years", P, "principal", R, "percent is :",
                  payment)
        else:
            print("Payment is : 0")
    # ----------------------  Finding the square root of the number  ---------------------------------------------------
    @staticmethod
    def  sqrt(c):
        # this method takes a number as input
        import math
        t = c
        count = 0
        epsilon = 0.00278
        var1 = abs(t-(c/t))
        var2 = epsilon*t
        # using given formula and eplsilon value find the perfect square of thegiven value
        while(var1>var2):
            count+=1
            t = ((c/t)+t)/2
            if(c%t==0):
                print(t)
                break
            if(count ==30):
                break
        if(count==30):
            print("Given no is not perfect square")
    # ------------------------  For converting Decimal number to binary number  ----------------------------------------
    @staticmethod
    def __toBinary__(num):
        # define an empty list
        list  = []
        n = 0
        # Every time append the remainders to the list
        while(num>0):
            n = num%2
            list.append(n)
            num = int(num/2)
        #    after appending revere the list to get the binary number of the given number
        list.reverse()
        return list
    # ----------------------------  For finding the given number in list using binary search  --------------------------
    @staticmethod
    def binarysearchint(list,num):
        l = 0
        u = int(len(list))
        # Every time checking the condition that lower boundary is less than upper boundary or not
        while (l <= u):
            # finding the mid value
            mid = int(l + u - 1 / 2)
            pos = (num == list[mid])
            if pos:
                return "Fount at index :", mid
            # if mid element is greater than the given element then leave the left part of hte list and search
            # right side of the list vice-versa
            if (pos != True and pos > 0):
                l = mid + 1
            else:
                u = mid - 1
    # ---------------------------  For finding the given String in list using binary search  ---------------------------
    @staticmethod
    def binarySearchString(list,string):
        l = 0
        u = int(len(list))
        while (l <= u):
            mid = int(l + u - 1 / 2)
            pos = (string == list[mid])
            if pos:
                return "Fount at index :", mid
            if (pos != True and pos > 0):
                l = mid + 1
            else:
                u = mid - 1
    # ---------------------------------  sorting the list using bubble sort  -------------------------------------------
    @staticmethod
    def bubbleSortInt(list):
        # Taking the list as input and finding the sorted lis
        # First for loop runs for length-1 times
        for i in range(len(list) - 1, 0, -1):
          for j in range(i):
            #   if the left elemrnt is grater than the right element is=t will moves to end of the list
            #  and the smaler element will moves to first of the list
            if(list[j]>list[j+1]):
                # By using swapping shifting the values
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        return list
    # ---------------------------------  sorting the list using bubble sort  -------------------------------------------
    @staticmethod
    def bubbleSortStr(list):
        for i in range(len(list) - 1, 0, -1):
          for j in range(i):
            if(list[j]>list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        return list
    # -------------------------------  sorting the list using insertion sort  ------------------------------------------
    @staticmethod
    def insertionsortInt(list):
        for i in range(0,len(list)):
            j = i+1
            for j in range(len(list)):
                # this will check every time that the subsequent element is grater means it will moves
                # to the end of the list af vice-verse
                if (list[i]<list[j]):
                    temp = list[i];
                    list[i] = list[j];
                    list[j] = temp
        return list
    # -------------------------------  sorting the list using insertion sort  ------------------------------------------
    @staticmethod
    def insertionsortStr(list):
        for i in range(0,len(list)):
            j = i+1
            for j in range(len(list)):
                if (list[i]<list[j]):
                    temp = list[i];
                    list[i] = list[j];
                    list[j] = temp
        return list

