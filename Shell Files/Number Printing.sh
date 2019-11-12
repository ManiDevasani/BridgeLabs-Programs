#!bin/bash
#Initiating the num variable with 1
num=1
#Running the loop for 10 times
while [ $num -le 10 ]
do
#each time printing the numbers
  echo $num
  num=$((num+1))
done
