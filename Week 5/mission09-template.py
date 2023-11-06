#
# CS1010X --- Programming Methodology
#
# Mission 9 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###############
# Pre-defined #
###############

a = [6, 4, 2, 9, 10, 4, 2, 1, 3]

###################
# Helper function #
###################

def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))

###########
# Task 1a #
###########

# The enumerate function should be helpful for you here.
# It takes in a sequence (either a list or a tuple)
# and returns an iteration of pairs each of which
# contains the index of the element and the element itself.
# Here's how to use it.

# for i, elem in enumerate((4, 10, 1, 3)):
#     print("I am in the", i ,"position and I am", elem)
# 
# I am in the 0 position and I am 4
# I am in the 1 position and I am 10
# I am in the 2 position and I am 1
# I am in the 3 position and I am 3

def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """

    position_to_be = len(seq)

    for i, elem in enumerate(seq):
        if x <= elem:
            position_to_be = i
            return position_to_be
        else:
            continue
    return position_to_be

print("## Q1a ##")
print(search(-5, (1, 5, 10)))
# => 0
print(search(3, (1, 5, 10)))
# => 1
print(search(7, [1, 5, 10]))
# => 2
print(search(5, (1, 5, 10)))
# => 1
print(search(42, [1, 5, 10]))
# => 3
print(search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 1b #
###########

def binary_search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted.
    Uses O(lg n) time complexity algorithm."""
    if len(seq) == 0:
        return 0
    
    mid_index = len(seq)//2
    if x == seq[mid_index]:
        return mid_index
    elif x > seq[mid_index]:
        try:
            if x < seq[mid_index+1]:
                return mid_index+1
            else:
                return mid_index + binary_search(x, seq[mid_index:])
        except IndexError:
            return len(seq)
    else: #ie: x < seq[mid_index]       
        try:
            if x > seq[mid_index-1]:
                return mid_index
            else:
                return binary_search(x, seq[:mid_index]) #no need add/minus since counting from front anyway
        except IndexError:
            return 0
        
print("## Q1b ##")
print(binary_search(-5, (1, 5, 10)))
# => 0
print(binary_search(3, (1, 5, 10)))
# => 1
print(binary_search(7, [1, 5, 10]))
# => 2
print(binary_search(5, (1, 5, 10)))
# => 1
print(binary_search(42, [1, 5, 10]))
# => 3
print(binary_search(42, (-5, 1, 3, 5, 7, 10)))
# => 6

###########
# Task 2a #
###########

def insert_list(x, lst):
    """ Inserts element x into list lst such that x is less than or equal
        to the next element and returns the resulting list."""
    position_to_insert = binary_search(x, lst)
    lst.insert(position_to_insert, x)
    return lst

print("## Q2a ##")
print(insert_list(2, [1, 5, 9]))
#=> [1, 2, 5, 9]
print(insert_list(10, [1, 5, 9]))
#=> [1, 5, 9, 10]
print(insert_list(5, [2, 6, 8]))
#=> [2, 5, 6, 8]

###########
# Task 2b #
###########

def insert_tup(x, tup):
    """ Inserts element x into tuple tup such that x is less than or equal
        to the next element and returns the resulting tuple."""
    position_to_insert = binary_search(x, tup)
    tup = tup[:position_to_insert] + (x,) + tup[position_to_insert:]
    return tup

print("## Q2b ##")
print(insert_tup(2, (1, 5, 9)))
#=> (1, 2, 5, 9)
print(insert_tup(10, (1, 5, 9)))
#=> (1, 5, 9, 10)
print(insert_tup(5, (2, 6, 8)))
#=> (2, 5, 6, 8)

###########
# Task 2c #
###########

tup = (5, 4, 10)
output_tup = insert_tup(7, tup)
lst = [5, 4, 10]
output_lst = insert_list(7, lst)

print("## Q2c ##")
print(tup is output_tup)
#=> Output: False
print(tup == output_tup)
#=> Output: False

print(lst is output_lst)
#=> Output: True
print(lst == output_lst)
#=> Output: True
#=> Explain the outputs:
# insert_tup works by creating a copy of the original tuple (tup)
# and then amending/inserting that copy (output_tup) before returning it.
# Hence, the original tuple (tup) remains as (5, 4, 10) while the resultant tuple to be returned
# will be the amended (5, 4, 7, 10), causing (tup is output_tup) and (tup == output_tup) to
# both be False.
#
# Meanwhile, insert_list works by amending the original list (lst) and returning that
# original list. Hence, the insert_list function will change the original lst
# and return that as the result, causing (lst is output_lst) and (lst == output_lst)
# to return True. This can be further checked when insert_list is used on output_lst,
# where the function will also amend the original list (lst).


###########
# Task 3a #
###########

def sort_list(lst):
    """ Sorts list lst in ascending order."""
    new_lst = []
    for element in lst:
        insert_list(element, new_lst)
    return new_lst

print("## Q3a ##")
print(sort_list([9, 6, 2, 4, 5]))
#=> [2, 4, 5, 6, 9]
print(sort_list([42, 7, 6, -42, 0]))
#=> [-42, 0, 6, 7, 42]
print(sort_list(["soda", "cola", "sprite", "root beer", "apple cider"]))
#=> ['apple cider', 'cola', 'root beer', 'soda', 'sprite']
print(sort_list(["turtle", "penguin", "dog", "cat", "ant eater", "butterfly"]))
#=> ['ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle']

###########
# Task 3b #
###########

#=> Time complexity of sort_list: The sort_list function uses my insert_list function,
# which in turn uses python's list.insert feature and my binary_search function.
# Since my binary_search function has time complexity of O(log n),
# and list.insert's is O(1) ==> time complexity of insert_list will be
# O(log n). Hence, time complexity of sort_list, which iterates n times
# and calls insert_list each time, will have a time complexity of O(n log n).

# If search was used in my insert_list instead, it will cause the time compelxity of
# sort_list to be O(n^2) instead.
###########
# Task 3c #
###########

def sort_tup(tup):
    """ Sorts tuple tup in an ascending order."""
    return accumulate(insert_tup, (), tup)

print("## Q3c ##")
print(sort_tup((9, 6, 2, 4, 5)))
#=> (2, 4, 5, 6, 9)
print(sort_tup((42, 7, 6, -42, 0)))
#=> (-42, 0, 6, 7, 42)
print(sort_tup(("soda", "cola", "sprite", "root beer", "apple cider")))
#=> ('apple cider', 'cola', 'root beer', 'soda', 'sprite')
print(sort_tup(("turtle", "penguin", "dog", "cat", "ant eater", "butterfly")))
#=> ('ant eater', 'butterfly', 'cat', 'dog', 'penguin', 'turtle')

###########
# Task 4a #
###########

import shelf

# Please uncomment the test function calls to see the animation

def insert_animate(block_pos, shelf, high):
    """
    Pops the block at block_pos and inserts it in the position in the shelf
    such that its size is less than or equal to the one succeeding it. It searches
    for this position within zero and high.

    NOTE: To actually see the animation, please uncomment the testing function
    below.
    """
    removed = shelf.pop(block_pos)
    height_in_list = []
    for block in shelf[:high]:
        height_in_list.append(block.size)
    position_to_put = binary_search(removed.size, height_in_list)
    shelf.insert(position_to_put, removed)    
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for insert_animate

def test_insert_animate():
    shelf.clear_window()
    s = shelf.init_shelf((2, 6, 1, 4, 8, 3, 9))
    print("## Q4a ##")
    print(insert_animate(0, s, 0))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(1, s, 1))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(2, s, 2))
    # => [Block size: 1, Block size: 2, Block size: 6, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(3, s, 3))
##    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(6, s, 6))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]

# Uncomment function call to test insert_animate()
test_insert_animate()

###########
# Task 4b #
###########

def sort_me_animate(shelf):
    """
    Maintains a sorted portion and inserts every block in the shelf into the
    sorted portion.

    NOTE: To actually see the animation, please uncomment the testing function
    below.

    """
    for i in range(len(shelf)):
        insert_animate(i, shelf, i)
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for sort_me_animate

def test_sort_me_animate():
    shelf.clear_window()
    s = shelf.init_shelf((5,2,6,9,1,4,8,3))
    print("## Q4b ##")
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 3, Block size: 4, Block size: 5, Block size: 6, Block size: 8, Block size: 9]
    shelf.clear_window()
    s = shelf.init_shelf((4, 8, 2, 9, 3, 1, 2, 3, 4, 10, 7, 5, 6))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 2, Block size: 3, Block size: 3, Block size: 4, Block size: 4, Block size: 5, Block size: 6, Block size: 7, Block size: 8, Block size: 9, Block size: 10]

# Test case to catch mutation while sorting

def test_sort_me_with_duplicates():
    shelf.clear_window()
    s = shelf.init_shelf((1,3,4,1,3,2))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 1, Block size: 2, Block size: 3, Block size: 3, Block size: 4]

# Uncomment function call to test sort_me_animate()
##test_sort_me_animate()
##test_sort_me_with_duplicates()
