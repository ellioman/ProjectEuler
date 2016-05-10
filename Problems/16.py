'''
Problem 16: Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

'''

def find_power_digit_sum(power):
    result = 0
    for s in str(2 ** power):
        result += int(s)
        
    return result
    

print find_power_digit_sum(1000)
