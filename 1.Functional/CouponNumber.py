"""""
------------------------------------------------------------------------------------------------------

Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.

-------------------------------------------------------------------------------------------------------
"""

class CouponNumber:
    def Number(self):
        print("Enter how many random numbers need to generate")
        # taking input from the user how many coupon numbers need to gnerate
        n = int(input())
        import random
        x = random.random()*100000000
        a = [0]
        count  = 0
        # Generating the random numbers and checking wheather it is new or not,if it is new one added to the array
        for i in range(0,n):
            y = random.random()*100000000
            if(a[i]==x):
                print("Repeated num :",a[i])
                count+=1
            else:
                a.append(y)
        char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8',9]
        a.pop(0)
        subString = ""
        leng = len(char)
        # using the array having random numbers generating the coupon numbers
        print("Coopon Numbers are : ")
        for i in range(0,n):
            subString = ""
            while(a[i]>0):
                index = int(a[i]%leng)
                subString += char[index]
                a[i] = int(a[i]/leng)
            print(subString)
        print("No of repeated numbers :",count)
Num = CouponNumber()
Num.Number()
