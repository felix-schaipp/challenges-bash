#!/bin/bash

# Problem 
# - Read in one character from STDIN.
# - If the character is 'Y' or 'y' display "YES".
# - If the character is 'N' or 'n' display "NO".
# - No other character will be provided as input.

# Input Format
# - One character

# Constraints
# - The character will be from the set .

# Output Format
# - echo YES or NO to STDOUT.

# to test in terminal use
# printf "y" | sh 2-started-with-conditionals.sh

# inputs
read character

# logic
if [[  $character == "Y" || $character == "y" ]]; then
    echo "YES"
else
    echo "NO"
fi
