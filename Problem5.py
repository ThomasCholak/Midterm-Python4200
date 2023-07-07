# Thomas Cholak

# Problem 5

import re

stack = []


def reverse(s):  # function for reversing string using stack
    for i in s:
        stack.append(i)  # adds to stack
    s = ""
    while stack:
        s += stack.pop()  # removes top-layer of stack
    return s


def is_palindrome(m):
    text2 = reverse(re.sub(r'\W+', '', m))  # removes all non-alphanumeric characters
    return bool(text1 == text2)  # returns true or false value


text1 = input("Please enter a word: \n")

if is_palindrome(text1):  # outputs based on boolean value
    print(f'Your text "{text1}" is a palindrome.')
else:
    print(f'Your text "{text1}" is not a palindrome.')