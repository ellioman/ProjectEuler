'''
Problem 22: Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

'''

import string

def get_data_from_file(file_name):
    import os
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(__location__, file_name)) as f:
        read_data = f.read()
    
    return read_data

def init_dictionaries(alpha_dict, names_dict):
    ind = 0
    for letter in string.ascii_lowercase:
        ind += 1
        alpha_dict[letter] = ind
    
    ind = 0
    for name in sorted_names:
        ind += 1
        names_dict[name] = ind

def calculate_score_total(alpha_dict, names_dict):
    total_score = 0
    for name in names_dict:
        name_score = names_dict[name]
        letter_score = 0
        for l in name:
            letter_score += alpha_dict[l]
        total_score += name_score * letter_score 
    return total_score


print "Getting data from file..."
file_data = get_data_from_file('22_names.txt')
sorted_names = sorted(file_data.lower().replace("\"", "").split(','))

print "Initialising the names and alphabet dictionaries..."
names = {}
alphabet = {}
init_dictionaries(alphabet, names)

print "Calculating total score..."
print calculate_score_total(alphabet, names)







