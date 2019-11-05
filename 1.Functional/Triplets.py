"""""
----------------------------------------------------------------------------------------------------------------
    A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
----------------------------------------------------------------------------------------------------------------
"""
class Triplets:
    def printing(self):
        a = []
        print("Enter the size of array")
        n = int(input())
        print("Enter elements into array")
        sum=0;
        for i in range(0,n):
            a.append(int(input()))
        #   finding the sum of three elemnts in the array and if there sum is zero counting the value
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if(a[i]+a[j]+a[k]==0):
                        print\
                            (a[i],end=" ")
                        print(a[j],end =" ")
                        print(a[k],end = " ")
                        print('\r')
                        sum+=1
        # After counting the no of triplets printing the value
        print("No Of Triplets : ",sum)
ob = Triplets()
ob.printing()