'''
Problem 4: Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def find_smallest_divisible(numbers):
    
    max_tries = 1000000000
    cur_num = 0
    for k in range(max_tries):
        cur_num += 1
        success = True
        for i in range(1, numbers + 1, 1):
            if cur_num % i != 0:
                success = False
                break
        
        if success:
            return cur_num
    
    print "Search unsuccessful"
    return 0


numbers = 20
results = find_smallest_divisible(numbers)

for i in range(1, numbers + 1, 1):
    print results, "/", i, "=", (results/i)