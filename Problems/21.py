'''
Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

def d(number):
    iterations = int(number / 2) + 1
    div_sum = 0
    for k in range(1, iterations):
        if number % k == 0: 
            #print k
            div_sum += k
    
    return div_sum

def find_amicable_numbers(max_num):
    amic_sum = 0
    for a in range(1, max_num + 1):
        b = d(a)
        c = d(b)
        
        if a == c and a != b:
            #print a, b, c
            amic_sum += a
        
    return amic_sum
            
print find_amicable_numbers(10000)