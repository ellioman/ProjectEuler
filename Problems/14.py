'''
Problem 14: Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


import math

def find_longest_collatz_sequence(max_num):
    longest_chain_length = 0
    longest_chain_number = 2
    for i in range(2, max_num + 1, 1):
        chain_counter = 1
        num = i
        while num > 1:
            if num % 2 == 0: num = num / 2
            else:  num = 3 * num  + 1
            chain_counter += 1
        
        if chain_counter > longest_chain_length:
            longest_chain_length = chain_counter
            longest_chain_number = i
            
    return longest_chain_number


print find_longest_collatz_sequence(1000000)
