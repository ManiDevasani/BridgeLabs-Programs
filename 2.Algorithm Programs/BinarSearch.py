"""""
---------------------------------------------------------------------------------------------------------------
Read in a list of words from File. Then prompt the user to enter a word to
search the list. The program reports if the search word is found in the list.
---------------------------------------------------------------------------------------------------------------
"""
class BinarySearch:
    def searching(self):
        # reading the file
        f = open('maninums', "r")
        for i in f:
            # splitting the string and storing it into the list
            List = i.split(" ")
        List.sort()
        print(List)
        s = str(input("Enter the string to search : "))
    # taking the lower boundary as '0' and the upper boundary as the length of the list
    l = 0
    u = int(len(List) - 1)
    while (l <= u):
        if s == List[u]:
            # if the element is present at the end of the list it will print and exit from the loop
            print("Fount at index :", u)
            break
            # if the element is present at the mid of the list it will print and exit from the loop
            mid = int((l + (u - 1) / 2))
        if s == List[mid]:
            print("Fount at index :", mid)
            break
        if List[mid] < s:
            # if the middle element is greater than the given element it will neglect the left part and moves to right
            # Lower boundary changes to mid
            l = mid + 1
        elif List[mid] > s:
            # if the middle element is less than the given element it will neglect the right part and moves to left
            # upper bounadary values chanes to mid
            u = mid - 1
    else:
        # if the element is not found then it will print not found
        print("Not Found")
fileonj = BinarySearch()
fileonj.searching()