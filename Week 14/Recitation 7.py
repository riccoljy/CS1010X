##CS1010X        Recitation 7

##Question 1

def make_matrix(seq):
    mat = []
    for row in seq:
        mat.append(list(row))
    return mat

#1(a)
#Assuming the nested lists all have the same length, then yes. Otherwise, if the list of lists
#is [[1,2,3],[4,5]], this would be a matrix with a "blank spot".

#1(b)(i)
def rows(m):
    return len(m)

#1(b)(ii)
def cols(m):
    if len(m):
        return len(m[0])
    return 0

#1(b)(iii)
def get(m, i, j):
    return m[i][j]
#time space both O(1)

#1(b)(iv)
def set(mat, i, j, val):
    mat[i][j] = val
#time O(1)

#1(b)(v)
    
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
    
#1(b)(vi)
def print_matrix(mat):
    for i in range(rows(mat)):
        row = "|"
        for j in range(cols(mat)):
            row += " \t" + str(get(mat, i, j)) + " \t"
        row += "|"
        print(row)

##Question 2
def make_matrix2(seq):
	data = []
	for i in range(len(seq)):
		for j in range(len(seq[0])):
			if seq[i][j] != 0:
				data.append([i,j,seq[i][j]])
	return [len(seq), len(seq[0]), data] 
#2(a)(i)
def rows2(m):
    return m[0]

#2(a)(ii)
def cols2(m):
    return m[1]

#2(a)(iii)
def get2(m, x, y):
    data = m[-1]
    for i, j, val in data:
        if (x,y) == (i,j):
            return val
    return 0 #need this because if not inside, means it's zero.

#2(a)(iv)
def set2(mat, x, y, val):
    data = mat[-1]
    for i in range(len(data)):
        e_x, e_y = data[i][0], data[i][1]
        if (e_x, e_y) == (x, y):
            data[i][-1] = val
            break
    #if reach here and no match, means it was a zero val.
    data.append([x, y, val])
    data.sort(key = lambda element: (element[0], element[1]))

#2(a)(v)
def transpose2(m):
    data = m[-1]
    for i in range(len(data)):
        data[i][0], data[i][1] = data[i][1], data[i][0]
    data.sort(key = lambda element: (element[0], element[1]))
    m[0], m[1] = m[1], m[0]

#2(a)(vi)
def print_matrix2(mat):
    data = mat[-1]
    curr_row = data[0][0]
    to_print = "|"
    for element in data:
        row = element[0]
        if row == curr_row:
            to_print += " \t" + str(element[-1]) + " \t"
        else:
            to_print += "|"
            print(to_print)
            to_print = "|" + " \t" + str(element[-1]) + " \t"
            curr_row = element[0]
    to_print += "|"
    print(to_print)

#2(b)
"""
2nd is a better implementation. Although may be difficult to read at first, the data
structure allows for ease of manipulation. Ease of transposing and getting value (and even
setting value).
"""
