'''
Problem 4: Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def find_sum_of_squares(numbers):
    sum_sqr = 0
    for i in range(numbers + 1):
        sum_sqr += i*i
    return sum_sqr
    

def find_square_of_sum(numbers):
    sqr_sum = 0
    
    for i in range(numbers + 1):
        sqr_sum += i
        
    return sqr_sum * sqr_sum

def find_sum_square_difference(numbers):
    sum_sqr = find_sum_of_squares(numbers)
    sqr_sum = find_square_of_sum(numbers)
    
    return sqr_sum - sum_sqr


numbers = 100
print find_sum_square_difference(numbers)