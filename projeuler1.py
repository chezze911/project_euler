# Problem 1 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


#     sum(x for x in range(1000) if x % 3 == 0  or x % 5 == 0)
    
def f(x, n):
    divisor = (n - 1) // x
    return (divisor * x * (divisor + 1)) // 2

>>> def f(x, n):
		divisor = (n - 1) // x
        return (divisor * x * (divisor + 1)) // 2

>>> f(3, 1000) + f(5, 1000) - f(3 * 5, 1000)
2333168