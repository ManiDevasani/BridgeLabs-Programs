#!/bin/bash
#Taking the Strings from the input
echo "Enter the 1st String"
read s1
echo "Enter the 2nd String"
read s2
#Comparing the Strings 
if [ $s1 == $s2 ]
then
#If it is equal prints below context
   echo "Given Strings are equal"
else  
   echo "Given Strings are not equal" 
fi
