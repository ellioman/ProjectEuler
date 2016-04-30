'''
Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find_pythogorean_triplet_sum(num_to_find):
    
    for a in range(1, num_to_find, 1):
        for b in range(a + 1, num_to_find, 1):
            for c in range(b + 1, num_to_find, 1):
                if (a + b + c == num_to_find):
                    if (a*a + b*b) == c*c:
                        return a*b*c
    
    print "Search unsuccessful"
    return 0

num_to_find = 1000
print find_pythogorean_triplet(num_to_find)