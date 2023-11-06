##CS1010X,      Tutorial 6,         8 Feb 2023,         Ricco Lim

##Question 1
#1(a)

"""
The implementation is wrong because as elements are removed in lst during the iteration,
the range(len(lst)) which has been computed will remain as range(len(lst)) BEFORE any
removal from lst.remove(lst[i]). This will result in an IndexError as elements are removed
and i value iterating to an index value that the shorter lst is out of range of.
"""

#1(b)

"""
Similar to the previous implementation, editing the lst while iterating will cause issues.
This time, it is because as the lst has elements removed, the i value in "for i in lst"
still increases and skips elements like 2 and 4.
Moral of story is not to edit the lst while iterating.
"""

#1(c)
def at_least_n(lst, n):
    lst[:] = [x for x in lst if x>=n]
    return lst

#1(d)
def at_least_n(lst, n):
    lst_new = [x for x in lst if x>=n]
    return lst_new

##Question 2
#2(a)
def col_sum(matrix):
    return row_sum(transpose(matrix))
##    result = matrix[0]
##    num_of_col = len(matrix)
##    num_of_rows = len(matrix[0])
##    for x in range(1, num_of_rows):
##        for y in range(num_of_col):
##            result[y] += matrix[x][y]
##    return result

#2(b)
def row_sum(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result

#2(c)
def transpose(matrix):
    num_of_row = len(matrix)
    num_of_col = len(matrix[0])
    for index in range(num_of_col):
        matrix.append([matrix[0][index]])
    matrix.pop(0)
    while num_of_row > 1:
        for index in range(num_of_col):
            matrix[num_of_row - 1 + index].append(matrix[0][index])
        matrix.pop(0)
        num_of_row -= 1
    return matrix


##Question 3
#3(a)
#3(b)
#3(c)
#3(d)

##Question 4
#4(a)
def mode_score(list_of_students):
    
    def determine_mode(list_of_scores):
        result = []
        highest_counter = 0
        mode = list_of_scores[0]
        counter = 0
        highest_counter = 0
        list_of_scores.sort()
        current_score = list_of_scores[0]
        
        for score in list_of_scores:
            if score == current_score:
                counter += 1
                if counter > highest_counter:
                    highest_counter = counter
                    mode = current_score
                    result = [mode]
                elif counter == highest_counter:
                    result.append(current_score)
            else:
                counter = 1
                current_score = score
        return result
    
    list_of_students_scores = []
    for student in list_of_students:
        list_of_students_scores.append(student[2])
    return determine_mode(list_of_students_scores)

##4(b)
def top_k(list_of_students, k):
    list_of_students.sort(key = lambda x:x[2], reverse=True) #sorts according to score, descending
    subresult = list_of_students[:k-1]
    kth_student_score = list_of_students[k-1][2]
    for student in list_of_students[k-1:]:
        score = student[2]
        if score == kth_student_score:
            subresult.append(student)
    ##now that we have the top students, we need to arrange by name/alphabetical order too 
    current_score = subresult[0][2]
    same_score_students = []
    result = []
    for student in subresult:
        score = student[2]
        if score == current_score:
            same_score_students.append(student)
        else: #if lower score already,
            same_score_students.sort()
            result += same_score_students
            current_score = score
            same_score_students = [student]
    same_score_students.sort()
    result += same_score_students
    return result
