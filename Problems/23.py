'''
Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

def d(number):
    iterations = int(number / 2) + 1
    div_sum = 0
    for k in range(1, iterations):
        if number % k == 0: 
            #print k
            div_sum += k
    
    return div_sum

def find_abundant_numbers(max_num, abundant_nums):
    for i in range(1, max_num + 1):
        if d(i) > i:
            abundant_nums.append(i)

def check_if_not_sum_of_two_abundant_numbers(num, abundant_nums):
    #print num
    if num > abundant_nums[0] * 2:
        for index1 in range(len(abundant_nums)):
            if abundant_nums[index1] + abundant_nums[index1] > num:
                break
                
            for index2 in range(index1, len(abundant_nums)):
                if abundant_nums[index1] + abundant_nums[index2] == num:
                    #print num, "=", abundant_nums[index1], "+", abundant_nums[index2]
                    return False
                elif abundant_nums[index1] + abundant_nums[index2] > num:
                    break
            
    return True

def prep_sum_dictionary(sum_dict, abundant_nums):
    for num1 in range(len(abundant_nums)):
        for num2 in range(num1, len(abundant_nums)):
            #sum_dict[str(num1) + "_" + str(num2)] = abundant_nums[num1] + abundant_nums[num2]
            sum_dict[abundant_nums[num1] + abundant_nums[num2]] = 0
    

def find_sum_of_non_abundant_numbers(max_num, sum_dict):
    sum_of_non_abundant = 0
    for num in range(max_num + 1):
        if num not in sum_dict:
            sum_of_non_abundant += num
    
    return sum_of_non_abundant

max_num = 28123
abundant_nums = []

print "Finding all abundant numbers...."
find_abundant_numbers(max_num, abundant_nums)

print
print "Creating a dictionary of all sums using two abundant numbers...."
mydict = {}
prep_sum_dictionary(mydict, abundant_nums)

print
print "Finding sum of all non abundant numbers...."
print "Result", find_sum_of_non_abundant_numbers(max_num, mydict)
#4179871