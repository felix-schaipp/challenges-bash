#!/bin/bash

# Problem
# A mathematical expression containing +,-,*,^, / and parenthesis will be provided. Read in the expression, then evaluate it. Display the result rounded to  decimal places.

# Constraints

# All numeric values are <= 999.

# Sample Input
# - 5+50*3/20 + (19*2)/7
# Sample Input 1
# -105+50*3/20 + (19^2)/7

# to test in terminal use
# echo "- 5+50*3/20 + (19*2)/7" | sh 4-arithmetic-operations.sh

# use double pipe here to first evaluate the expression then pipe the example again and round with printf to 3 decimals
# input
read expression
echo $expression | bc -l | xargs printf "%.*f\n" 3 
