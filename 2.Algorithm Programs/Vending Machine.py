"""""
-------------------------------------------------------------------------------
There is 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
returned by Vending Machine. Write a Program to calculate the minimum number
of Notes as well as the Notes to be returned by the Vending Machine as a
Change
-------------------------------------------------------------------------------
"""


class VendingMachine:
    @staticmethod
    def cash():
        amount = int(input("Enter the amount  "))
        p = amount
        # taking th notes in a list notes
        notes = [1000, 500, 100, 50, 10, 5, 2, 1]
        notescount = 0
        count = 0
        print("Given amount is :", amount)
        # if the given amount is zero it will prints the 0 notes
        if amount == 0:
            print("Notes : 00")
        # this loop runs for the length of the notes
        for i in range(0, len(notes)):
            # if the given amount is greater than the index of the array at the particular index is divided to ge the
            # no of notes and next amount is replaced by the percentile between the amount and the notes of at that 
            # index until the length of the list is zero or the amount is zero evert time incrementing the count 
            # value to get the no of notes 
            if amount >= notes[i]:
                notescount = int(amount / notes[i])
                print(notes[i], "Rs notes are :", notescount)
                amount = amount % notes[i]
                count += 1
        print("No Of Notes for", p, "is :", count)


# calling the cash method by creating the object


VendingMachine.cash()
