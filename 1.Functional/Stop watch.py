"""""
-----------------------------------------------------------------------------------------------
Write a Stopwatch Program for measuring the time that elapses between
the start and end clicks
-----------------------------------------------------------------------------------------------
"""
class StopWatch:
    def method(self):
        print("Enter any key to start")
        import time
        key = input()
        # By using the method time() taking the current instance time
        if(key==key):
            start = time.time()
        print("Enter any key to stop")
        key = input()
        if (key == key):
           stop= time.time()
        #     By subracting the values the resultant will be the elapsed time
        print("Elapsed time : ",stop-start)
p1 = StopWatch()
p1.method()