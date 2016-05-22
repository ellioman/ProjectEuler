'''
Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 

The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

def create_all_permutations(s):
    if len(s) <= 1: 
        print "=>" + s
        yield s
    else:
        for i in range(len(s)):
            for p in create_all_permutations(s[:i] + s[i+1:]):
                print "->" + s[i] + p
                yield s[i] + p


permutations = create_all_permutations("012")#3456789")

cur_index = 0
index_to_find = 999999
for perm_num in permutations:
    #if cur_index ==  index_to_find: 
    print perm_num
    cur_index += 1
