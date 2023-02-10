"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
"""
numbe = [1,[2,3],4,5]
numbe2 = [1,2,3,4,5]

def square_sum(numbers):
    empty = 0
    for i in numbers:
        empty += i*i
    print(empty)
    return empty

square_sum(numbe2)

# Best Answer:

"""
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
"""