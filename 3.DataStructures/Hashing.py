"""""
-----------------------------------------------------------------------------------------------
    Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
    efficiently search a number from a given set of number
-----------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.LinkedList import LinkedList
class Hashing:
    if __name__ == '__main__':
        # creating a new dictionary for storing the numbers having the same remainders
        # Creating the object and  storing the remainders after diviing with 11
        # creating 10 empty slots in the form of lists
        s1 = []
        s2 = []
        s3 = []
        s4 = []
        s5 = []
        s6 = []
        s7 = []
        s8 = []
        s9 = []
        s10 = []
        s11 = []
        hash = {}
        list = LinkedList()
        L = []
        f = open("maninums",'r')
        # Splitting the numbers by space
        for i in f :
            L = i.split(",")
        #   inserting the elemnts to the linked list
        for i in L:
            n = int(i)
            list.add(n)
        # taking input number from the user
        print("Enter the number to search : ")
        num = int(input())
        # checking the given number is present in the list
        # if it is present remove from the list else add to the list
        if (list.search(num)):
            print("Given Number is Present in the list,therefore removing the number from the list ")
            list.pop(num)
        else:
            print("Given Number is  not Present in the list,therefore adding the number from the list ")
            list.add(num)
        #Checking the numebers inthe list are divisible by 11 or not
        # Storing the elemnts with respect to their remainders in the slots
        size = list.size()
        for i in range(size):
            n = int(list.index(i))
            rem = n%11
            if rem == 0:
                s1.append(list.index(i))
            if rem == 1:
                s2.append(list.index(i))
            if rem==2:
                s3.append(list.index(i))
            if rem == 3:
                s4.append(list.index(i))
            if rem == 4:
                s5.append(list.index(i))
            if rem == 5:
                s6.append(list.index(i))
            if rem == 6:
                s7.append(list.index(i))
            if rem == 7:
                s8.append(list.index(i))
            if rem == 8:
                s9.append(list.index(i))
            if rem == 9:
                s10.append(list.index(i))
            if rem == 10:
                s11.append(list.index(i))
        # Mapping the slots to the respected remainders if the partcular slot is not empty
        # after mapping deleting the slots in the form of lists
        hash[0] = s1
        del s1
        hash[1] = s2
        del s2
        hash[2] = s3
        del s3
        hash[3] = s4
        del s4
        hash[4] = s5
        del s5
        hash[5] = s6
        del s6
        hash[6] = s7
        del s7
        hash[7] = s8
        del s8
        hash[8] = s9
        del s9
        hash[9] = s10
        del s10
        hash[10] = s11
        del s11
        # printing the slots with remainders
        # In the dictionary key values as the dictionary and the numbers are the dictionary under the key value
        print(hash)


