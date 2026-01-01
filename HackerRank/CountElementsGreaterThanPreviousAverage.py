#!/bin/python3
from traceback import print_tb

from pycparser.ply.yacc import resultlimit

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    count = 0
    if len(responseTimes) <= 1:
        return 0

    running_sum = responseTimes[0]

    for i in range(1, len(responseTimes)):
        # Calculate average of all previous elements
        average = running_sum / i  # Check if current element is greater than average
        print(average)
        if responseTimes[i] > average:
            count += 1
            # Update running sum for next iteration
        running_sum += responseTimes[i]

    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)

# list_iterator= [3,2,4]
# result = []
# div = 2
# for i in range(0,len(list_iterator)):
#     avg = sum(list_iterator[0:i+1])/div
#     div +=1
#     print(f'sum = {(sum(list_iterator[0:i+1]))}')
#     print(f'{(sum(list_iterator[0:i+1]))}/{div}= {avg}')
#     # print(avg)