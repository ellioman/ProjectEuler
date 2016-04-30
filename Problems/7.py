'''
Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

def isprime(n):
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

def prime_factors(number_of_primes):
    counter = 0
    num = 2
    while counter <= number_of_primes:
        if (isprime(num)):
            counter += 1
            if counter == number_of_primes:
                return num
        num += 1

numbers = 10001
print prime_factors(numbers)