#!/bin/bash
#Taking the numbers from the user
echo "Enter first number"
#By using the read command we can take the input from the user
read num1
echo "Enter te second number"
read num2
#By using the below cmd (()) we can add the numbers and Storing the result in the sum
sum=$(($num1+$num2))
#Printing the sum
echo "Sum of the two numbers is : $sum "
