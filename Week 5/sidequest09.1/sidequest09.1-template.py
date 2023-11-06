#
# CS1010X --- Programming Methodology
#
# Sidequest 9.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json
import time

#####################
# Reading json file #
#####################

def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google it :P

    For example, file.txt contains:
    [["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"], ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"], ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]]

    Calling read_json('file.txt') will return the following array
    [
        ["CS3216", "SOFTWARE DEVELOPMENT ON EVOLVING PLATFORMS", "TAN KENG YAN, COLIN"],
        ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"],
        ["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"]
    ]
    """
    datafile = open(filename, 'r', encoding='utf-8')
    return json.loads(datafile.read())

#############
# Accessors #
#############

def module_code(module):
    return module[0]

def module_name(module):
    return module[1]

def module_prof(module):
    return module[2]


###########
# Task 1a #
###########
def insert_list(x, lst):
    """ Inserts element x into list lst such that x is less than or equal
        to the next element and returns the resulting list."""
    position_to_insert = binary_search(x, lst)
    lst.insert(position_to_insert, x)
    return lst

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


def merge_lists(all_lst):
    result = []
    for lst in all_lst:
        for element in lst:
            insert_list(element, result)
    return result
    

all_lst = [[2, 7, 10], [0, 4, 6], [3, 11]]
print("## Q1a ##")
print(merge_lists(all_lst)) # [0, 2, 3, 4, 6, 7, 10, 11]


###########
# Task 1b #
###########

def merge(lists, field):
    result = []

    def find_smallest(lists, field):
        smallest = lists[0][0]
        for sorted_sublist in lists:
            if field(sorted_sublist[0]) < field(smallest):
                smallest = sorted_sublist[0]
        return smallest

    def remove_smallest_and_append(smallest, lists, result):
        result += smallest,
        for sublist in lists:
            if smallest in sublist:
                sublist.remove(smallest)
                if sublist == []:
                    lists.remove(sublist)

    while lists:
        remove_smallest_and_append(find_smallest(lists, field),
                                   lists, result)
    return result


list_of_lists = [[["CS1010S", "PROGRAMMING METHODOLOGY", "LEONG WING LUP, BEN"],
                  ["CS3235", "COMPUTER SECURITY", "NORMAN HUGH ANDERSON"]],
                 [["CS4221", "DATABASE DESIGN", "LING TOK WANG"],
                  ["CS2010", "DATA STRUCTURES & ALGORITHMS II", "STEVEN HALIM"]]]
print("## Q1b ##")
print(merge(list_of_lists, module_prof))
# [[’CS1010S’, ’PROGRAMMING METHODOLOGY’, ’LEONG WING LUP, BEN’],
#  [’CS4221’, ’DATABASE DESIGN’, ’LING TOK WANG’],
#  [’CS3235’, ’COMPUTER SECURITY’, ’NORMAN HUGH ANDERSON’],
#  [’CS2010’, ’DATA STRUCTURES & ALGORITHMS II’, ’STEVEN HALIM’]

##########
# Task 2 #
##########

def merge_sort(lst, k, field):
    #first, need to split lst into k parts
    total_num_of_mods = len(lst)
    from math import ceil
    mods_per_sublist = ceil(total_num_of_mods/k) #just an approx for even-ness
    new_lst = []
    index_start = 0
    while total_num_of_mods > len(new_lst)*mods_per_sublist:
        new_lst += lst[index_start:index_start + mods_per_sublist],
        index_start += mods_per_sublist
        
    #now, we have sublists which are unsorted

    #if able to directly sort the k unsorted sublists,
    def search_modified(x, seq, field):
        """ Takes in a value x and a sorted sequence seq, and returns the
        position that x should go to such that the sequence remains sorted """
        position_to_be = len(seq)
        for i, elem in enumerate(seq):
            if field(x) <= field(elem):
                position_to_be = i
                return position_to_be
            else:
                continue
        return position_to_be
    def insert_list_modified(x, lst, field):
        """ Inserts element x into list lst such that x is less than or equal
        to the next element and returns the resulting list."""
        position_to_insert = search_modified(x, lst, field)
        lst.insert(position_to_insert, x)
        return lst

    result = []
    for sublist in new_lst:
        for mod in sublist:
            insert_list_modified(mod, result, field)
    return result

    #if unable to directly use k unsorted sublist,
    """find way to sort the k sublists first then use merge"""


# For your own debugging
modules = read_json('modules_small.txt')
for module in merge_sort(modules, 2, module_code):
    print(module)


########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########
########### DO NOT REMOVE THE TEST BELOW ###########

def print_list_to_str(list):
    return '\n'.join(str(x) for x in list)

def test(testfile_prefix):
    print("\n*** Testing with ",testfile_prefix,".txt ***")
    modules = read_json(testfile_prefix+'.txt')
    total_time = 0

    # Open correct answers
    modules_sorted_code = open(testfile_prefix+'_sorted_code.txt', 'r', encoding='utf-8').read()
    modules_sorted_name = open(testfile_prefix+'_sorted_name.txt', 'r', encoding='utf-8').read()
    modules_sorted_prof = open(testfile_prefix+'_sorted_prof.txt', 'r', encoding='utf-8').read()

    ks = [2,3,5,8,13,21,34,55,89,144]
    pass_k = 0

    for k in ks:
        start_time = time.time()
        # Execute
        modules_answer_code = merge_sort(modules, k, module_code)
        modules_answer_name = merge_sort(modules, k, module_name)
        modules_answer_prof = merge_sort(modules, k, module_prof)
        end_time = time.time()
        total_time += (end_time - start_time)

        # Check
        code_same = print_list_to_str(modules_answer_code) == modules_sorted_code
        name_same = print_list_to_str(modules_answer_name) == modules_sorted_name
        prof_same = print_list_to_str(modules_answer_prof) == modules_sorted_prof
        if (code_same and name_same and prof_same):
            pass_k += 1
        print("k = ", k, ", code: ",code_same,", name: ", name_same,", prof: ",prof_same)

    print(pass_k,"/", len(ks), " correct! Total time taken: ", total_time, " seconds.")

print("## Q2 ##")
test('modules_small')
test('modules')
test('modules_empty')
