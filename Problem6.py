# Thomas Cholak

# Problem 6

d = [3, 10, 4, 32, 22, 23, 15, 5, 4, 8]  # string of 10 random integers

squares = []
for i in d:
    square = i ** 2
    squares.append(square)

# print(squares)

# initializing list
"""
table = [{'num': d[0], 'square': squares[0]},
         {'num': d[1], 'square': squares[1]},
         {'num': d[2], 'square': squares[2]},
         {'num': d[3], 'square': squares[3]},
         {'num': d[4], 'square': squares[4]},
         {'num': d[5], 'square': squares[5]},
         {'num': d[6], 'square': squares[6]},
         {'num': d[7], 'square': squares[7]},
         {'num': d[8], 'square': squares[8]},
         {'num': d[9], 'square': squares[9]}]
"""
# print("The original list is : " + str(test_list))

table = {
    d[0]: [squares[0]],
    d[1]: [squares[1]],
    d[2]: [squares[2]],
    d[3]: [squares[3]],
    d[4]: [squares[4]],
    d[5]: [squares[5]],
    d[6]: [squares[6]],
    d[7]: [squares[7]],
    d[8]: [squares[8]],
    d[9]: [squares[9]],
}

headers = ['Numbers', 'dth power']

print(f'{headers[0]: <10}{headers[1]}')

for key, value in table.items():
    print(f'{key: <10}{value[0]: <15}')
