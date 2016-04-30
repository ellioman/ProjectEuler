'''
Problem 3: Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

# Good article about finding prime factors
# http://thetaoishere.blogspot.com/2009/04/finding-largest-prime-factor.html
def prime_factors(n):
    largestPrimeFactor = 1
    factors = []
    
    if(n % 2 == 0):
        largestPrimeFactor = 2
        factors.append(largestPrimeFactor)
        while(n % 2 == 0):
            n = n / 2
    
    if(n % 3 == 0):
        largestPrimeFactor = 3
        factors.append(largestPrimeFactor)
        while(n % 3 == 0):
            n = n / 3
    
    # Beyond 2 and 3, all prime numbers are of the form 6n-1 or 6n+1.
    multOfSix = 6
    while(multOfSix - 1 < n):
        if(n % (multOfSix - 1) == 0):
            largestPrimeFactor = multOfSix - 1
            factors.append(largestPrimeFactor)
            
            while(n % largestPrimeFactor == 0):
                n = n / largestPrimeFactor
        
        if (n % (multOfSix + 1) == 0):
            largestPrimeFactor = multOfSix - 1
            factors.append(largestPrimeFactor)
            while(n % largestPrimeFactor == 0):
                n = n / largestPrimeFactor
        
        multOfSix+=6
    return factors

target = 600851475143
print prime_factors(target)
