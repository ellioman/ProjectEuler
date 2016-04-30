'''
Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def is_prime(n):
    """Returns True if n is prime."""
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    
    # Beyond 2 and 3, all prime numbers are of the form 6n-1 or 6n+1.
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        
        i += w
        w = 6 - w

    return True

def find_sum_of_primes_below(number):
    prime_sum = 0
    for num in range(2, number, 1):
        if is_prime(num):
            prime_sum += num
            
    return prime_sum

num = 2000000
print find_sum_of_primes_below(num)