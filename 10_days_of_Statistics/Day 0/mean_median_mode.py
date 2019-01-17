# -------------------------------------------------------------------------------------------------------------
# Task:
# Given an array, X , of N integers, calculate and print the respective mean, median, and mode on separate lines. 
# If your array contains more than one modal value, choose the numerically smallest one.
# -------------------------------------------------------------------------------------------------------------
# Input Format:
# The first line contains an integer,N, denoting the number of elements in the array. 
# The second line contains N space-separated integers describing the array's elements.
# 
# Constraints:
# 10 <= N <=2500
# 0 < x_i <= 10^5
# 
# Output Format:
# Print  lines of output in the following order =>
# 1. Print the mean on a new line, to a scale of  decimal place (i.e., 12.3, 7.0 ).
# 2. Print the median on a new line, to a scale of  decimal place (i.e.12.3, 7.0).
# 3. Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
# -------------------------------------------------------------------------------------------------------------
# Sample Input:
# 10
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
# 
# Sample Output:
# 43900.6
# 44627.5
# 4978
# -------------------------------------------------------------------------------------------------------------
import collections

N = int(input()) # no of elements
X = [int(x) for x in input().split()] # given array

def mean(n, arr):
    sum = 0
    for element in arr:
        sum += element
    return sum/n

def median(n, arr):
    arr = sorted(arr)
    if n%2 == 0:
        return (arr[int(n/2)-1] + arr[int(n/2)]) / 2
    else:
        return arr[int(n/2)]

def mode_(arr):
    # Generate a table of sorted (value, frequency) pairs.
    table = _counts(arr)
    if len(table) == 1:
        return table[0][0]
    elif table:
        return min(table)
    else:
        raise StatisticsError('no mode for empty data')

def _counts(data):
    # Generate a table of sorted (value, frequency) pairs.
    table = collections.Counter(iter(data)).most_common()
    if not table:
        return table
    # Extract the values with the highest frequency.
    maxfreq = table[0][1]
    for i in range(1, len(table)):
        if table[i][1] != maxfreq:
            table = table[:i]
            break
    return table

print(f"Mean: {mean(N,X):.1f}")
print(f"Median: {median(N,X):.1f}")
print(f"Mode: {mode_(X)}")

class StatisticsError(ValueError):
    pass
