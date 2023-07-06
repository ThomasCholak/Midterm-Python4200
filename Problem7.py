# Thomas Cholak

# Problem 7

from collections import Counter
import re

txt = input('Please enter text: \n')

x = txt.split()


def count_words(k):
    y = Counter(k)
    a = y.most_common(1)  # finds most common word

    string = str(a)  # converts dictionary entry to string
    s = re.sub(r'[^A-Za-z0-9 ]+', '', string)  # removes all non-alphanumeric characters except spaces
    b = s.split()
    return b


c = count_words(x)  # most common word is returned to main code body


print(f"The most common word is '{c[0]}' and it appears {c[1]} times.")
