"""""
--------------------------------------------------------------------------------------
Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
--------------------------------------------------------------------------------------
"""
class Harmonic:
    def number(self):
        print("Enter number")
        n = int(input())
        sum=1
        for i in range(2,n+1):
            # Every time of the loop taking the sum of the next harmonic number
            sum+=1/i
            if(n==i):
                print(n,"th Value",1 /i)
        print("Sum of harmonic numbers of",n,"is",sum)
num = Harmonic()
num.number()