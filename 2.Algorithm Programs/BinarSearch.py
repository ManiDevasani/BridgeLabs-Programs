"""""
---------------------------------------------------------------------------------------------------------------
Read in a list of words from File. Then prompt the user to enter a word to
search the list. The program reports if the search word is found in the list.
---------------------------------------------------------------------------------------------------------------
"""


class BinarySearch:
    @staticmethod
    def searching():
        # reading the file
        f = open('maninums', "r")
        for i in f:
            # splitting the string and storing it into the list
            arr = i.split(" ")
        arr.sort()
        print(arr)
        s = str(input("Enter the string to search : "))
        # taking the lower boundary as '0' and the upper boundary as the length of the list
        low = 0
        u = int(len(arr) - 1)
        while low <= u:
            mid = int((low + (u - 1) / 2))
            if s == arr[u]:
                # if the element is present at the end of the list it will print and exit from the loop
                print("Fount at index :", u)
                break
                # if the element is present at the mid of the list it will print and exit from the loop
            if s == arr[mid]:
                print("Fount at index :", mid)
                break
            if arr[mid] < s:
                # if the middle element is greater than the given element
                # it will neglect the left part and moves to right
                # Lower boundary changes to mid
                low = mid + 1
            elif arr[mid] > s:
                # if the middle element is less than the given element it will neglect the right part and moves to left
                # upper boundary values changes to mid
                u = mid - 1
        else:
            # if the element is not found then it will print not found
            print("Not Found")


BinarySearch.searching()