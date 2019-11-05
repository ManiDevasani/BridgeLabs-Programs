"""""
---------------------------------------------------------------------------------------------------
Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab.
Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
the National Weather Service defines the effective temperature (the wind chill) to
be:
---------------------------------------------------------------------------------------------------
"""
class WindChill:
    def __int__(self):
        print("Enter temperature value greater than 0 and less than 50")
        t = int(input())
        print("Enter speed value greater than 0 and less than 3  or greater than 120")
        v = int(input())
        if(t<50 and (v>120 or v<3)):
            return  35.74+0.6215*t+0.4275*t-35.75*(v**0.16)
        else:
            print("Given input is valid")
ob = WindChill()
print(ob.__int__())