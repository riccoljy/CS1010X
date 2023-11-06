##CS1010X        Recitation 6       Ricco Lim       29/3/2023

#Question 1
many_things = [1 , 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')]
print (many_things)
#[1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')]

numbers = [2 , 3 , 4 ]
print ( numbers )
#[2, 3, 4]

concatenated = many_things + numbers
print ( concatenated )
#[1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), 2, 3, 4]

appended = many_things . append ( numbers )
print ( appended )
#None
print ( many_things )
#[1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), [2, 3, 4]]

extended = many_things . extend ( numbers )
print ( extended )
#None
print ( many_things )
#[1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), 2, 3, 4]

many_things [ 0 ] = 7
print ( many_things )
#[7, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), 2, 3, 4]

can_be_indexed = concatenated [ 2 ]
print ( can_be_indexed )
#('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')
can_be_indexed_multiple_times = concatenated [ 2 ][ 1 ]
print ( can_be_indexed_multiple_times )
#'can'

a_shallow_copy = concatenated [:]
print ( a_shallow_copy )
#[1, 'a', ('I', 'can ', 'have ', 'tuples ', 'in ', 'lists '), 2, 3, 4]
print ( a_shallow_copy == concatenated )
#True
print ( a_shallow_copy is concatenated )
#False
woops = a_shallow_copy [ 2 ]
print ( woops )
#('I', 'can ', 'have ', 'tuples ', 'in ', 'lists ')
print ( woops is can_be_indexed )
#True
singleton = ['blah ']
print ( singleton )

#['blah ']

#Question 2

def bubble_sort(lst):
    for i in range(len(lst)): #can just range(len(lst) - 1) because 2nd last will be compared with last
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
#Time: O(n^2),

#Space: O(n) wrong
##Space actually  O(1)??
#because never create a NEW list that is n elements long

#Question 3
def selection_sort(lst):
    for i in range(len(lst)):
        minval, pos = lst[i], i
        for j in range(i, len(lst)):
            if lst[j] < minval:
                minval, pos = lst[j], j
        lst[i], lst[pos] = minval, lst[i]
    return lst
        

#Question 4
students = [('tiffany', 'A', 15), ('jane', 'B', 10), ('ben', 'C', 8), ('simon', 'A', 21), ('john', 'A', 15), ('jimmy', 'F', 1), ('charles', 'C', 9), ('freddy', 'D', 4), ('dave', 'B', 12)]
students.sort(reverse=True)
students.sort(key = lambda x: x[1])
students.sort(key = lambda x: (x[1], x[0]))
tuple(map(lambda x: x[0], tuple(filter(lambda x: len(x[0]) < 6, students))))
def grade_count(lst): ##assuming given lst is already sorted by grade
    lst.sort(lambda x: x[1]) # to sort the lst by grade if not yet already
    curr_counter = 0
    curr_grade = lst[0][1]
    res = []
    for person in lst:
        grade = person[1]
        if grade == curr_grade:
            curr_counter += 1
        else:
            res.append((curr_grade, curr_counter))
            curr_grade, curr_counter = grade, 1
    res.append((curr_grade, curr_counter))
    return tuple(res)
grade_count(students)

def grade_count_using_dict(lst):
    res = {}
    for student in lst:
        if student[1] in res:
            res[student[1]] += 1
        else:
            res[student[1]] = 1
    return tuple(map(lambda x: (x, res[x]), res))

