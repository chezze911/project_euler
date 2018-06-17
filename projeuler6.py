# Sum square difference
# Problem 6 
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 minus 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(limit):
    total = 0
    for i in range(limit+1):
        total += i**2
    return total


def square_of_sum(limit):
    total = 0
    for i in range(limit+1):
        total += i
    return total**2

sum_1 = sum_of_squares(100)
sum_2 = square_of_sum(100)

print("Answer:" + str(sum_2-sum_1))


# output:  
# Answer:25164150
# [Finished in 0.6s]