'''
Problem 17: Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

'''

num_letter_dict = {
    '00': '',
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',
    '90' : 'ninety',
}

def calculate_word_length(number):
    number_str = str(number)
    result = ""
    index = len(number_str) - 1
    last_index = index
    
    if number <= 20:
        result = num_letter_dict[number_str]
    else:
        n1 = int(number_str[last_index - 1]) * 10
        n2 = int(number_str[last_index])
        
        if n1 + n2 > 0:
            if n1 + n2 > 20:
                result = num_letter_dict[str(n1)] + " " + num_letter_dict[str(n2)]
            else:
                result = num_letter_dict[str(n1 + n2)]
        
        index -= 2
            
        while index >= 0:
            num = number_str[index]
            
            if num == '0':
                result = num_letter_dict[num] + result
            
            elif index == last_index - 2:
                result = num_letter_dict[num] + " hundred " + ("and " if result != "" else "") + result
            
            elif index == last_index - 3:
                result = num_letter_dict[num] + " thousand " + result
        
            index -= 1
    
    return result, len(result.replace(" ", ""))


def find_number_letter_counts(min_num, max_num):
    count = 0
    for i in range(min_num, max_num + 1, 1):
        count += calculate_word_length(i)[1]
        #print str(i) + " => " + str(calculate_word_length(i)[1])
    return count

print find_number_letter_counts(1, 1000)
