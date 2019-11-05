"""""
----------------------------------------------------------------------------------------
    Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
------------------------------------------------------------------------------------------
"""
class Gambler:
    def printing(self):
        win=0
        loss=0
        # Taking input stake amount,goal amount, no of times to play
        print("Enter stake amount")
        s = int(input())
        print("Enter goal amount")
        g = int(input())
        print("Enter no of times to play")
        n = int(input())
        # this loop will run untill the no of times the user given
        for i in range(0,n):
            cash = s
            # untill the cash gets less than 0 this loop will calculate the wins and loose
            while(cash>0 and cash<g):
                import random
                x = random.random()
                if(x<0.5):
                    cash+=1
                else:
                    cash-=1
            # if cash is equals the goal it means win
            if(cash==g):
                win+=1
            else:
                loss+=1
        # Printing the win,loss percentage and no fo times wins
        print("No of Wins : ",win)
        print("Wins percentage : ",100*win/n)
        print("loss percentage : ",100*loss/n)
ob = Gambler()
ob.printing()