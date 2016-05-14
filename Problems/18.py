'''
Problem 18: Maximum path sum I
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   *3*
  *7* 4
 2 *4* 6
8 5 *9* 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
'''

numbers= [ 75,
             95, 64,
            17, 47, 82,
           18, 35, 87, 10,
          20, 04, 82, 47, 65,
         19, 01, 23, 75, 03, 34,
        88, 02, 77, 73, 07, 63, 67,
       99, 65, 04, 28, 06, 16, 70, 92,
      41, 41, 26, 56, 83, 40, 80, 70, 33,
     41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
    53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
   70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
  91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
 63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
    
# numbers = [
#    3,
#   7, 4,
#  2, 4, 6,
# 8, 5, 9, 3,
# ]  

class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def create_tree(numb_array):
    arr_index = 0
    num_in_row = 1
    
    
    num_tree_array = []
    ppp = 1
    count = 0
    for num in numb_array:
        t = Tree(int(num))
        num_tree_array.append(t)
        count += 1
        if ppp == count: 
            ppp += 1
            count = 0
    
    is_done = False
    while not is_done:
        for i in range(arr_index, arr_index + num_in_row, 1):
            print num_tree_array[i].data, "=>", num_tree_array[i + num_in_row].data, ",", num_tree_array[i + num_in_row+ 1].data
            num_tree_array[i].left = num_tree_array[i + num_in_row]
            num_tree_array[i].right = num_tree_array[i + num_in_row + 1]
        
        arr_index += num_in_row
        num_in_row += 1
        
        #print arr_index, ">=", len(num_tree_array) - ppp
        if arr_index >= len(num_tree_array) - ppp:
            is_done = True
    
    return num_tree_array[0]
    

def find_maximum_path_sum(tree):
    if (tree.left == None): 
        return tree.data
    
    a = find_maximum_path_sum(tree.left)
    b = find_maximum_path_sum(tree.right)
    
    return tree.data + (a if a > b else b)
    

tree = create_tree(numbers)
result = find_maximum_path_sum(tree)
print
print result
