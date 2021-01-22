#!/bin/bash

# Problem 
# Given two integers, X and Y, identify whether X < Y or X > Y or X = Y.

# Exactly one of the following lines:
# - X is less than Y
# - X is greater than Y
# - X is equal to Y

# to test in terminal use
# printf "5\n2" | sh 1-comparing-numbers.sh

# inputs
read x
read y

# logic
if [[  $x > $y ]]; then
    echo "X is greater than Y"
elif [[ $x < $y ]]; then
    echo "X is less than Y"
else
    echo "X is equal to Y"
fi
