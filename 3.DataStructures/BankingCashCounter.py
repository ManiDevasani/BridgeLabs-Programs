"""""
---------------------------------------------------------------------------------------
1. Create a Program which creates Banking Cash Counter where people
come in to deposit Cash and withdraw Cash. Have an input panel to add people
to Queue to either deposit or withdraw money and dequeue the people. Maintain
the Cash Balance.
---------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Queue import Queue


class CashCounter:
    if __name__ == '__main__':
        # creating the object for the queue
        q = Queue()
        # Taking 1 Persons in queue
        q.enqueue(1)
        count = int(1)
        # running the loop for count times, if in between by adding people to queue the count is increased
        while count > 0:
            # count is zero means that means there is no people in queue means stack is empty then the loop will breaks
            if count == 0:
                break
            import re
            print("---------WELCOME TO CASH-COUNTER-----------")
            print("Enter 1 to Deposit : ")
            print("Enter 2 to Withdraw : ")
            print("Enter 3 to get No of Persons in Queue : ")
            print("Enter 4 to add Persons to Queue : ")
            print("Enter 5 to exit fom Queue : ")
            # By taking the input from the user which options user will selected
            # According to that the process will takes place
            sel = input()
            x = re.findall("1|2|3|4|5", sel)
            if x:
                # if user selts '1' it will comes here
                # Takes the deposit amount and remove the person from the queue
                # means removing the element from the queue
                if sel.__contains__("1"):
                    print("Enter the amount to deposit in numbers : ")
                    depamount = input()
                    q.dequeue()
                    depamount = ""
                    d = ""
                    print("------THANK YOU VISIT AGAIN-------")
                # if the user selected '2' then it will comes here
                # Takes the withdraw amount and remove the person from the queue
                # means removing the element from the queue
                if sel.__contains__("2"):
                    print("Enter the amount to With draw in numbers : ")
                    withdrawamount = input()
                    q.dequeue()
                    withdrawamount = ""
                    w = ""
                    print("------THANK YOU VIST AGAIN-------")
                # if the user selected '3' then it will comes here
                # here it will prints the no of persons in queue means the size of queue
                if sel.__contains__("3"):
                    print("No of Persons in 'Q' are : ", q.size())
                    count += 1
                    print("------THANK YOU VIST AGAIN-------")
                # if the user selected '4' then it will comes here
                # Here it will adds the persons to the queue
                if sel.__contains__("4"):
                    print("Enter No of members to add")
                    num = int(input())
                    # based onthe user input this loop will runs and every time adding a element to the queue
                    for i in range(0, num):
                        q.enqueue(1)
                        count = num * count
                    print("You have added", num, "people to Queue")
                # if the user selected '5' then it will comes here
                # if the user want to exit from the queue then it will breaks the loop
                if sel.__contains__("5"):
                    print("------THANK YOU VIST AGAIN-------")
                    break
            # if the user would enter the wrong data then it will show the below context
            else:
                print("You have entered wrong output")
            count = count - 1
            sel = ""
            x = ""
        # if count is zero it means there are no persons in the queue
        if count < 0:
            print("----No persons are Present in queue---")
