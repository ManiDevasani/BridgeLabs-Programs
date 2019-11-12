#!/bin/bash
#Taking the numbers from the user
echo "Enter first number"
#By using the read command we can take the input from the user
read num1
echo "Enter te second number"
read num2
#By using the below cmd (()) and * we can multiply
ans=$(($num1*$num2))
#Printing the sum
echo "Multiplication of the Given numbers is : $ans "
