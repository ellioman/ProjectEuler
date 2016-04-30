'''
Problem 1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def get_sum_of_multiples(max_num, multiples):
    sum = 0
    for num in range(max_num):
        if (num % 5 == 0 or num % 3 == 0): sum += num
        
    return sum
    

multiples = [3, 5]
max_num = 1000
print get_sum_of_multiples(max_num, multiples)