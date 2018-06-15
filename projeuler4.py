
# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. 

# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(i):
    return str(i) == str(i)[::-1]


max_p = 0

for i in xrange(100, 999):
    for j in xrange(i+1, 1000):
        p = i * j
        if is_palindrome(p) and p > max_p:
            max_p = p



print max_p