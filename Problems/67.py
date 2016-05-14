'''
Problem 67: Maximum path sum II
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''


class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.high_sum = 0

def create_tree(numb_array):
    arr_index = len(numb_array) - 1
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
    num_in_row = ppp
    
    is_done = False
    while not is_done:
        for i in range(arr_index, arr_index - num_in_row + 1, -1):
            if i != arr_index - num_in_row + 2:
                num_tree_array[i - num_in_row + 1].right = num_tree_array[i]
                
                if num_tree_array[i - num_in_row + 1].high_sum < num_tree_array[i].data + num_tree_array[i].high_sum:
                    num_tree_array[i - num_in_row + 1].high_sum = num_tree_array[i].data + num_tree_array[i].high_sum
            
            if i != arr_index:
                num_tree_array[i - num_in_row + 2].left = num_tree_array[i]
                
                if num_tree_array[i - num_in_row + 2].high_sum < num_tree_array[i].data + num_tree_array[i].high_sum:
                    num_tree_array[i - num_in_row + 2].high_sum = num_tree_array[i].data + num_tree_array[i].high_sum
        
        arr_index -= num_in_row -1
        num_in_row -= 1
        
        if arr_index <= 0:
            is_done = True
    
    return num_tree_array[0]
    

def find_maximum_path_sum(tree):
    
    if (tree.left == None): 
        return tree.data
    
    a = find_maximum_path_sum(tree.left)
    b = find_maximum_path_sum(tree.right)
    
    return tree.data + (a if a > b else b)


def get_numbers_from_file(file_name):
    import os
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    with open(os.path.join(__location__, file_name)) as f:
        read_data = f.read()
    
    return read_data.replace('\n', ' ').split()


print "Getting numbers from file..."
numbers = get_numbers_from_file('67_triangle.txt')
print "Creating Tree...."
tree = create_tree(numbers)
print "Finding maximum path...."
#print find_maximum_path_sum(tree)
print tree.data + tree.high_sum
