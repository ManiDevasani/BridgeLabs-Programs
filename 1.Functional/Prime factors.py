"""""
-----------------------------------------------------------------------------------
    Computes the prime factorization of N using brute force.
-----------------------------------------------------------------------------------
"""
class PrimeFactors:
    def factors(self):
        import math
        print("Enter Number : ")
        n = int(input())
        print("Prime factors for",n,"is")
        # Printing the factors of a given number until it is divided by 2
        while (n % 2 == 0):
                print("2")
                n = n / 2
        #  if the given number is not even then this loop will print the remaining factors
        for i in range(3, int(math.sqrt(n)+1)):
            while (n % i == 0):
                print(i);
                n = n / i
            i+=2
        # if the remaining factor is greater than 2 it will be printing here
        if (n > 2):
            print(n)
        else:
            print()
nums = PrimeFactors()
nums.factors()