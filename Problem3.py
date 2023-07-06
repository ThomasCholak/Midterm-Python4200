# Thomas Cholak

# Problem 3

from array import *

arr = []


def sort():
    for k in range(len(lst)):
        for j in range(k + 1, len(lst)):
            if lst[k] > lst[j]:
                lst[k], lst[j] = lst[j], lst[k]
    print(f'The top three values are {lst[9]}, {lst[8]} and {lst[7]}.')


print('Please enter 10 numbers (hit enter after entering each integer):')
for i in range(0, 10):
    ele = int(input())
    arr.append(ele)

lst = array('i', arr)
sort()
