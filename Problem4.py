# Thomas Cholak

# Problem 4

n = int(input("Please enter an integer:\n"))

lst = []


def printing_factorial(m):
    for i in reversed(range(m + 1)):
        lst.append(i)
    del lst[-1]
    string = ','.join(str(x) for x in lst)
    string = string.replace(',', ' * ')
    print(f'{string} = {calculate_factorial(n)}')


def calculate_factorial(m):
    if m == 1:
        return 1
    else:
        return m * calculate_factorial(m - 1)


printing_factorial(n)
