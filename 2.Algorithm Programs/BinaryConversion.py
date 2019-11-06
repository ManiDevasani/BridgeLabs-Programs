"""""
------------------------------------------------------------------------------------------------------------
1. Write a static function toBinary that outputs the binary (base 2) representation of
the decimal number typed as the input. It is based on decomposing the number into
a sum of powers of 2. For example, the binary representation of 106 is 11010102,
which is the same as saying that 106 = 64 + 32 + 8 + 2. Ensure necessary padding
to represent 4 Byte String.
    To compute the binary representation of n, we consider the powers of 2 less than or
equal to n in decreasing order to determine which belong in the binary
decomposition (and therefore correspond to a 1 bit in the binary representation).
------------------------------------------------------------------------------------------------------------
"""
# importing the Util class to perform the binary conversion operation
from Scripts.com.BridgeLabs.Functional.Util import Util


class Binary:
    @staticmethod
    def function():
        num = int(input("Enter the number to convert to Binary Number : "))
        # calling the method in util class and passing the number taken from the user
        binary = Util.__toBinary__(num)
        print("Binary Number for given number", num, "is : ")
        # printing the binary number
        for i in binary:
            print(i, end=" ")
        print()
        print("The Given number", num, "in th form of power of 2 is : ")
        x = 0
        # reversing the binary array for getting the number with base 10
        binary.reverse()
        print(num, end=" = ")
        for i in binary:
            # Printing the given number in 2^0 is not considerd
            # and calculating the power of 2 while the array has the value 1
            # it calculate the 2 power of that number
            if binary[x]==1:
                print(2**x, end=" + ")
            x += 1
        print("0")
        # reversing the array for satisfying the given condition
        binary.reverse()
        split1 = []
        split2 = []
        # taking the length of the array and half if length percentile is equals to 0
        x = len(binary)
        if x%2 == 0:
            half = round(x/2)
        # if length percentile is not equal to 0 then adding the 0 to the list to get divided by 2
        else:
            binary1 = [0]
            count = 1
            for i in binary:
                binary1.append(i)
                count += 1
            binary = binary1
            half = round(x / 2)
            x = len(binary)
        if x % 2 == 0:
            # spiting the array into two half's and joining the two splited array into a single array
            for i in range(0, half):
                split1.append(binary[i])
            for i in range(half, x):
                split2.append(binary[i])
            print("Swapped Binary Num : ")
            for i in range(0, len(split1)):
                split2.append(split1[i])
            for i in split2:
                print(i, end=" ")
            print()
            del split1
            x = 0
            sum = 0
            split2.reverse()
            # converting from binary num to the number with base 10
            for i in binary:
                if split2[x] == 1:
                    sum += 2**x
                x += 1
            # printing the number after nibble the binary number
            print("Decimal number for Swapped Binary num is : ", sum)
            del x
        else:
            print("Given number cannot divide into two nibbles")


Binary.function()