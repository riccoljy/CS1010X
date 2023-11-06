#
# CS1010X --- Programming Methodology
#
# Mission 10 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.


####################
# Helper functions #
# - print_tree     #
# - accumulate     #
####################

def print_tree(tree, print_output=True):
    """
    Helper function to print trees in this mission.

    Yes, it looks scary. Nothing to see here (:
    """
    def get_elements_at_level(tree, level):
        def helper(tree, level, cur):
            if is_empty_tree(tree) and cur < level:
                dummy = build_tree(" ", make_empty_tree(), make_empty_tree())
                return helper(left_branch(dummy), level, cur + 1) + helper(right_branch(dummy), level, cur + 1)
            if cur == level:
                if is_empty_tree(tree):
                    return (" ", )
                else:
                    return (entry(tree), )
            elif cur < level:
                return helper(left_branch(tree), level, cur + 1) + helper(right_branch(tree), level, cur + 1)
        return helper(tree, level, 0)

    def height(tree):
        if is_empty_tree(tree):
            return 0
        else:
            return 1 + max(height(left_branch(tree)), height(right_branch(tree)))

    h = height(tree)
    output_string = ""

    for level in range(h):
        indent = 2 ** (h - (level + 1)) - 1
        spacing = 2 ** (h - level) - 1

        output = " " * indent

        for i, e in enumerate(get_elements_at_level(tree, level)):
            if level == 0 or i == 0:
                output = output + str(e)
            else:
                output = output + " " * spacing + str(e)
        if print_output:
            print(output)
        else:
            output_string += output + '/'
    if not print_output:
        return output_string

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))


###########
# Task 1a #
###########

def build_tree(entry, left, right):
    return [left, entry, right]


###########
# Task 1b #
###########

def entry(tree):
    return tree[1]

def left_branch(tree):
    return tree[0]

def right_branch(tree):
    return tree[2]


###########
# Task 1c #
###########

def make_empty_tree():
    return []


###########
# Task 1d #
###########

def is_empty_tree(tree):
    return tree == make_empty_tree()

t1 = build_tree(2, build_tree(1, make_empty_tree(),
                                 make_empty_tree()),
                   build_tree(3, make_empty_tree(),
                                 make_empty_tree()))
print_tree(t1)
#=> 2
#=>1 3

t2 = build_tree(5, build_tree(2, build_tree(1, make_empty_tree(),
                                               make_empty_tree()),
                                 make_empty_tree()),
                   build_tree(7, make_empty_tree(),
                                 build_tree(10, make_empty_tree(),
                                                make_empty_tree())))
print_tree(t2)
#=>   5
#=> 2   7
#=>1     10


###########
# Task 2a #
###########

def insert_tree(x, tree):
    """
    - tree is empty -> return a tree with x as entry and empty left and right branches
    - x <= entry -> return new tree with x inserted into left sub tree
    - otherwise -> return new tree with x inserted into right sub tree
    """
    if is_empty_tree(tree):
        return build_tree(x, make_empty_tree(), make_empty_tree())
    elif x <= entry(tree):
        left_sub_tree = left_branch(tree)
        right_sub_tree = right_branch(tree)
        if is_empty_tree(left_sub_tree):
            return build_tree(entry(tree), build_tree(x, make_empty_tree(), make_empty_tree()), right_sub_tree)
        else:
            return build_tree(entry(tree), insert_tree(x, left_sub_tree), right_sub_tree)
    else: #if x > entry
        left_sub_tree = left_branch(tree)
        right_sub_tree = right_branch(tree)
        if is_empty_tree(right_sub_tree):
            return build_tree(entry(tree), left_sub_tree, build_tree(x, make_empty_tree(), make_empty_tree()))
        else:
            return build_tree(entry(tree), left_sub_tree, insert_tree(x, right_sub_tree))
        
         

t1 = insert_tree(5, t1)
print_tree(t1)
#=> 2           insert_tree(5, t1)        2
#=>1 3               ===>               1   3
#=>                                          5

t2 = insert_tree(6, t2)
print_tree(t2)
#=>   5         insert_tree(6, t2)        5
#=> 2   7            ===>               2   7
#=>1     10                            1   6 10

t2 = insert_tree(3, t2)
print_tree(t2)
#=>   5         insert_tree(3, t2)        5
#=> 2   7            ===>               2   7
#=>1   6 10                            1 3 6 10


###########
# Task 2b #
###########

# Time complexity of insert_tree: O(log n) where n is the number of elements in the tree


###########
# Task 2c #
###########

def contains(x, tree):
    """ Returns true if x is in binary tree, otherwise return false """
    if x == entry(tree):
        return True
    elif x <= entry(tree) and not is_empty_tree(left_branch(tree)):
        return contains(x, left_branch(tree))
    elif x > entry(tree) and not is_empty_tree(right_branch(tree)):
        return contains(x, right_branch(tree))
    else:
        return False

print(contains(1, t1))
#=> True

print(contains(5, t1))
#=> True

print(contains(42, t1))
#=> False

print(contains(10, t2))
#=> True

print(contains(6, t2))
#=> True

print(contains(11, t2))
#=> False


###########
# Task 2d #
###########

# Time complexity of contains: O(log n) where n is the number of elements in the tree


###########
# Task 2e #
###########

def flatten(tree):
    """ flattens tree with the following rule:
        visit left branch, visit entry then visit right branch """
    result = []
    
    if is_empty_tree(tree):
        return result
    
    left_subtree, right_subtree = left_branch(tree), right_branch(tree)

    if not is_empty_tree(left_subtree): #if left_subtree is not empty,
        left_subtree_result = flatten(left_subtree)
        result += left_subtree_result
        
##    elif is_empty_tree(left_subtree): #if left_subtree is empty,
##        if entry(tree) not in result: result.append(entry(tree))
        
    result.append(entry(tree))

    if not is_empty_tree(right_subtree):
        right_subtree_result = flatten(right_subtree)
        result += right_subtree_result
        
##    elif is_empty_tree(right_subtree): #if left_subtree is empty,
##        result.append(entry(tree))
##        return result
    
    return result
    

print(flatten(t1))
#=> [1, 2, 3, 5]

print(flatten(t2))
#=> [1, 2, 3, 5, 6, 7, 10]


###########
# Task 2f #
###########

# Time complexity of flatten: O(n) where n is the number of elements in the tree


###########
# Task 3a #
###########

def sort_it(lst):
    tree = make_empty_tree()
    for num in lst:
        tree = insert_tree(num, tree)
    return flatten(tree)

print(sort_it([5, 3, 2, 1, 4, 6, 7, 9]))
#=> [1, 2, 3, 4, 5, 6, 7, 9]

print(sort_it([5, 3, 2, 1, 4, -1, 6, 0, 7, 9]))
#=> [-1, 0, 1, 2, 3, 4, 5, 6, 7, 9]


###########
# Task 3b #
###########

# Time complexity of sort_it: O(n) to iterate * O(log n) for insert_tree * O(n) for flatten ==> O(n^2*log n)
