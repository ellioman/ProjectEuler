'''
Problem 4: Largest palindrome product
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(num_to_check):
    #print "checking", num_to_check
    str_num = str(num_to_check)
    length = len(str_num)
    
    # even number = length / 2 iterations, odd number = ((length - 1) / 2) iterations
    iterations = (length / 2) if (length % 2 == 0) else (length-1) / 2
    for i in range(length / 2):
        if (str_num[i] != str_num[length - i - 1]):
            return False
    return True
    
def find_largest_palindrome(num_of_digits):
    largest_num = int("9" * num_of_digits)
    largest = 0
    for n in range(largest_num, 0, -1):
        
        for i in range(n):
            num = n * (n - i)
            if (is_palindrome(num)):
                if (largest < num):
                    largest = num
                else: 
                    break
    
    return largest
    



digits = 3
print find_largest_palindrome(digits)

