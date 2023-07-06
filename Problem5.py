# Thomas Cholak

# Problem 5

stack = []


def reverse(s):
    for i in s:
        stack.append(i)
    s = ""
    while stack:
        s += stack.pop()
    return s


text1 = input("Please enter a word: \n")
text2 = reverse(text1)

if text1 == text2:
    print(f'Your text "{text1}" is a palindrome.')
else:
    print(f'Your text "{text1}" is not a palindrome.')
