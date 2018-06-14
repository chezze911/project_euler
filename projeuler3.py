# Largest prime factor
# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


n = 600851475143
i = 2

while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print n


# n = 13195
# output = 29
# [Finished in 0.5s]

# n = 600851475143
# 6857
# [Finished in 0.6s]