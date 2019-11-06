"""""
--------------------------------------------------------------------------
1 .Write a program with Static Functions to do Merge Sort of list of
Strings.
--------------------------------------------------------------------------
"""


class MergeSort:
    @staticmethod
    def mergesorting():
        arr = ['m', 'a', 'n', 'i', 'k', 'a', 'n', 't', 'a']
        # Created an array and pass the array to the merge function
        MergeSort.merge(arr)
        print(arr)

    @staticmethod
    def merge(arr):
        # calculating the mid of the array taking half of the array
        m = int(len(arr) // 2)
        # Taking the left side of the array
        left = arr[:m]
        # Taking the right side of the array
        right = arr[m:]
        if len(arr) > 1:
            # every time the left array is halved until its size becomes 0
            MergeSort.merge(left)
            # every time the left array is halved until its size becomes 0
            MergeSort.merge(right)
            # the divided array is merge inserted order by the following while loop
            a = b = c = 0
            while a < len(left) and b < len(right):
                # if left array is greater than the right array it moves to end of the list
                if left[a] <= right[b]:
                    arr[c] = left[a]
                    a += 1
                else:
                    arr[c] = right[b]
                    b += 1
                c += 1
            # if there are any remaining elements  in  the arrays are done here
            while a < len(left):
                arr[c] = left[a]
                a += 1
                c += 1
            while b < len(right):
                arr[c] = right[b]
                b += 1
                c += 1


# calling the sorting function
MergeSort.mergesorting()
