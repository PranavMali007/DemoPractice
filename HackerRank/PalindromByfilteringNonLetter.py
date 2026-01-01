#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # keep only alphabetic characters, lowercased
    filter_string = ([ch.lower() for ch in code if ch.isalpha()])
    print(filter_string)
    # check palindrome
    print(len(filter_string)//2)
    for i in range(len(filter_string) // 2):
        if filter_string[i] != filter_string[-1 - i]:
            return False
    return True


if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
