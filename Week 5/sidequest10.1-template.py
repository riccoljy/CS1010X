#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    nested_list = []
    for i in range(n):
        nested_list.append(0)
    main_game_matrix = []
    for i in range(n):
        main_game_matrix.append(nested_list[:]) #must use copy if not, all will change.
    return main_game_matrix

def has_zero(mat):
    return 0 in flatten(mat)

def add_two(mat):
    if not has_zero(mat):
        return mat
    else:
        n = len(mat)-1
        num_of_0s = flatten(mat).count(0)
        while flatten(mat).count(0) == num_of_0s:
            rand_col = randint(0, n)
            rand_row = randint(0, n)
            if mat[rand_col][rand_row] == 0:
                mat[rand_col][rand_row] = 2
                return mat


###########
# Task 2  #
###########

def check_any_adjacent_tiles(mat):
        high = len(mat)
        for row in mat:
            low = 0
            while high > low+1:
                if row[low] == row[low+1]:
                    return True
                else:
                    low += 1
        # if reach here, means no same ones horizontally.
        # now to check vertically
        for i in range(high):
            low = 0
            while high > low+1:
                if mat[low][i] == mat[low+1][i]:
                    return True
                else:
                    low += 1
        return False

def game_status(mat):    
    if 2048 in flatten(mat):
        return "win"
    elif not has_zero(mat) and not check_any_adjacent_tiles(mat):
        return "lose"
    else:
        return "not over"       

###########
# Task 3a #
###########

def transpose(matrix):
    new_matrix = matrix[:]
    num_of_row = len(new_matrix)
    num_of_col = len(new_matrix[0])
    for index in range(num_of_col):
        new_matrix.append([new_matrix[0][index]])
    new_matrix.pop(0)
    while num_of_row > 1:
        for index in range(num_of_col):
            new_matrix[num_of_row - 1 + index].append(new_matrix[0][index])
        new_matrix.pop(0)
        num_of_row -= 1
    return new_matrix




###########
# Task 3b #
###########

def reverse(mat):
    new_mat = []
    for row in mat:
        curr_row = []
        for num in row:
            curr_row.insert(0, num)
        new_mat.append(curr_row)
    return new_mat



############
# Task 3ci #
############

def merge_left(mat):

    def insert_in_row(x, row):
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = x
                return row
            else:
                continue
        return row

    def move_left_row(row):
        score = 0
        row_copy = row[:]
        new_row = [0] * len(row_copy)
        for index1 in range(len(row_copy)):
            if row_copy[index1] != 0:
                current_tile = index1
                i = 1
                next_tile = -1
                while current_tile + i < len(row_copy):
                    index2 = current_tile + i
                    if row[index2] != 0:
                        next_tile = index2
                        break
                    else:
                        i += 1
                        
                if next_tile == -1: #means no next_tile
                    insert_in_row(row_copy[current_tile], new_row)
                            
                elif row[current_tile] == row[next_tile]: #means they have same value,
                    insert_in_row(row_copy[current_tile]*2, new_row)
                    row_copy[next_tile] = 0 #since that value is "used" and combined alr (old matrix copy ruined)
                    score += row_copy[current_tile]*2
                    
                else:
                    insert_in_row(row_copy[current_tile], new_row)
        return new_row, score


    new_mat = list(map(lambda x: x[0], list(map(move_left_row, mat))))
    points = sum(tuple(map(lambda x: x[1], list(map(move_left_row, mat)))))
    return new_mat, not new_mat == mat, points

                    



#############
# Task 3cii #
#############

def merge_right(mat):
    reversed_mat = reverse(mat)
    merged_mat = reverse(merge_left(reversed_mat)[0])
    return merged_mat, not merged_mat == mat, merge_left(reversed_mat)[-1]

def merge_up(mat):
    transposed_mat = transpose(mat)
    merged_mat = transpose(merge_left(transposed_mat)[0])
    return merged_mat, not merged_mat == mat, merge_left(transposed_mat)[-1]

def merge_down(mat):
    transposed_mat = transpose(mat)
    merged_mat = transpose(merge_right(transposed_mat)[0])
    return merged_mat, not merged_mat == mat, merge_right(transposed_mat)[-1]


###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
##text_play()


# How would you test that the winning condition works?
# Your answer: Playing until you get 2048. If status == "win", it works.
#


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    state = matrix, total_score
    return state

def get_matrix(state):
    return state[0]
    
def get_score(state):
    return state[1]
    
def make_new_game(n):
    mat = new_game_matrix(n)
    state = add_two(add_two(mat)), 0
    return state
    
def left(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_left(mat)[1]
    if valid:
        score += merge_left(mat)[-1]
        newstate = make_state(add_two(merge_left(mat)[0]), score)
        return newstate, valid
    else:
        return state, valid
    
def right(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_right(mat)[1]
    if valid:
        score += merge_right(mat)[-1]
        newstate = make_state(add_two(merge_right(mat)[0]), score)
        return newstate, valid
    else:
        return state, valid
    
def up(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_up(mat)[1]
    if valid:
        score += merge_up(mat)[-1]
        newstate = make_state(add_two(merge_up(mat)[0]), score)
        return newstate, valid
    else:
        return state, valid

def down(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_down(mat)[1]
    if valid:
        score += merge_down(mat)[2]
        newstate = make_state(add_two(merge_down(mat)[0]), score)
        return newstate, valid
    else:
        return state, valid


# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
##gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return mat, increment

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############

def make_new_records():
    return []

def push_record(new_record, stack_of_records):
    stack_of_records.append(new_record)
    stack_of_records = stack_of_records[-3:]
    return stack_of_records

def is_empty(stack_of_records):
    return not len(stack_of_records) #if length is 0 (ie: empty), will return not False

def pop_record(stack_of_records):
    if is_empty(stack_of_records):
        return None, None, stack_of_records
    else:
        last_rec = stack_of_records.pop()
        last_game_mat = get_record_matrix(last_rec)
        last_score_incr = get_record_increment(last_rec)
        return last_game_mat, last_score_incr, stack_of_records

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return matrix, total_score, records

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    mat = new_game_matrix(n)
    state = add_two(add_two(mat)), 0, make_new_records()
    return state

def left(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_left(mat)[1]
    stack = get_records(state)
    if valid:
        increment = merge_left(mat)[-1]
        score += increment
        new_mat = add_two(merge_left(mat)[0])
        curr_rec = make_new_record(mat, increment)
        push_record(curr_rec, stack)
        newstate = make_state(new_mat, score, stack)        
        return newstate, valid
    else:
        return state, valid

def right(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_right(mat)[1]
    stack = get_records(state)
    if valid:
        increment = merge_right(mat)[-1]
        score += increment
        new_mat = add_two(merge_right(mat)[0])
        curr_rec = make_new_record(mat, increment)
        push_record(curr_rec, stack)
        newstate = make_state(new_mat, score, stack)        
        return newstate, valid
    else:
        return state, valid

def up(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_up(mat)[1]
    stack = get_records(state)
    if valid:
        increment = merge_up(mat)[-1]
        score += increment
        new_mat = add_two(merge_up(mat)[0])
        curr_rec = make_new_record(mat, increment)
        push_record(curr_rec, stack)
        newstate = make_state(new_mat, score, stack)        
        return newstate, valid
    else:
        return state, valid

def down(state):
    mat = get_matrix(state)
    score = get_score(state)
    valid = merge_down(mat)[1]
    stack = get_records(state)
    if valid:
        increment = merge_down(mat)[-1]
        score += increment
        new_mat = add_two(merge_down(mat)[0])
        curr_rec = make_new_record(mat, increment)
        push_record(curr_rec, stack)
        newstate = make_state(new_mat, score, stack)        
        return newstate, valid
    else:
        return state, valid

# NEW FUNCTIONS TO DEFINE
def get_records(state):
    return state[-1]

def undo(state):
    #is also a move, just undo
    #since a stack only has latest 3 moves, will automatically be invalid after undo-ing 3 times
    
    rec = get_records(state)[-4:] #so that can undo only 3 times
    score = get_score(state)
    prev_mat, prev_incr, prev_stack = pop_record(rec)
    
    if is_empty(prev_stack):
        return state, False
    else:
        undone_state = make_state(prev_mat, score - prev_incr, prev_stack)
        return undone_state, True



# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': undo
}
gamegrid = GameGrid(game_logic)
