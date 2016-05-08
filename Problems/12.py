'''
Problem 12: Highly divisible triangular number
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 

The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''


import math

def find_divisible_number(div_target):
    max_search = 100000
    last_num = 0
    for i in range(1, max_search + 1, 1):
        last_num = last_num + i
        count = 2
        count = count + 2 if last_num % 2 == 0 else count
        for i in range(3, int(math.sqrt(last_num)) + 1, 1):
            if last_num % i == 0:
                count += 2
            
            if count > div_target:
                return last_num, count
    
    print "Search unsuccessful!"
    return -1


print find_divisible_number(500)