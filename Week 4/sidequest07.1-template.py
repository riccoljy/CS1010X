#
# CS1010X --- Programming Methodology
#
# Mission 7 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from lazy_susan import *

##########
# Task 1 #
##########

def solve_trivial_2(table):
    table_state = get_table_state(table)
    coins_to_flip = ()
    for coin in table_state:
        if coin == 1:
            coins_to_flip += 0,
        else:
            coins_to_flip += 1,
    flip_coins(table, coins_to_flip)

# test:
t2_1 = create_table(2)
solve_trivial_2(t2_1)
print(check_solved(t2_1))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t2_1_run = create_table(2)
##run(t2_1_run, solve_trivial_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t2_1_susan = create_table(2)
##Susan(t2_1_susan)

########################################################





##########
# Task 2 #
##########

def solve_trivial_4(table):
    table_state = get_table_state(table)
    coins_to_flip = ()
    for coin in table_state:
        if coin == 1:
            coins_to_flip += 0,
        else:
            coins_to_flip += 1,
    flip_coins(table, coins_to_flip)

# test:
t4_2 = create_table(4)
solve_trivial_4(t4_2)
print(check_solved(t4_2))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_2_run = create_table(4)
##run(t4_2_run, solve_trivial_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t4_2_susan = create_table(4)
##Susan(t4_2_susan)

########################################################





##########
# Task 3 #
##########

def solve_2(table):
    if check_solved(table) == True:
        return
    else:
        flip_coins(table, (0,1)) #(0,1) or (1,0); arbitrary since can just flip any
        return

# test:
t2_3 = create_table(2)
solve_2(t2_3)
print(check_solved(t2_3))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t2_3_run = create_table(2)
##run(t2_3_run, solve_2)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

##t2_3_susan = create_table(2)
##Susan(t2_3_susan)

########################################################





##########
# Task 4 #
##########

def solve_4(table):
    if check_solved(table) == True:
        return
    else:            
##        while check_solved(table) == False: #Actually not required, can just call function, because as per qns, "guaranteed within 7 moves"
##            n_equals_4_algo(table)
            
        n_equals_4_algo(table)
        return

def n_equals_4_algo(table):
    A = (1,0,1,0) 
    B = (1,1,0,0) 
    C = (1,0,0,0)
    flip_coins(table, A)
    if check_solved(table) == True:
        return
    flip_coins(table, B)
    if check_solved(table) == True:
        return
    flip_coins(table, A)
    if check_solved(table) == True:
        return
    flip_coins(table, C)
    if check_solved(table) == True:
        return
    flip_coins(table, A)
    if check_solved(table) == True:
        return
    flip_coins(table, B)
    if check_solved(table) == True:
        return
    flip_coins(table, A)
    return          
        
# test:
t4_4 = create_table(4)
solve_4(t4_4)
print(check_solved(t4_4))


########################################################
## VISUALIZATION ALTERNATIVE
## Run the following two lines below to see how the
## coins on the table are flipped and rotated.

##t4_4_run = create_table(4)
##run(t4_4_run, solve_4)

########################################################
## GUI ALTERNATIVE
## Run the following two lines below to use the
## interactive GUI to solve the table instead.

t4_4_susan = create_table(4)
Susan(t4_4_susan)

########################################################





##########
# Task 5 #
##########

def solve(table):
    if check_solved(table) == True:
        return
    else:
        table_size = get_table_size(table)
        moves = moveset(table_size)
        for i in range(2**(table_size -1) -1):
            flip_coins(table, moves[i])
            if check_solved(table):
                return            

def moveset(table_size):

    def movelist(n):
    
    #No need for n==1 bc n==1 is alr solved......
    ##    if n == 1:
    ##        moves = ((1,),)
    ##        return moves
        
        if n == 2:
            moves = ((1, 0),)
            return moves
        else:
            moves = ()
            flipall = ()
            flipnone = ()
            for i in range(n):
                flipall += (1,)
                flipnone += (0,)
            for move in movelist(n//2): #for first n//2-1 moves
                moves += (move * 2,)
            moves += (flipall[:n//2]+flipnone[n//2:],)
            for move in movelist(n//2): #for next n//2-1 moves,
                moves += (move+flipnone[n//2:],)
            return moves
        
    def num_of_distinct_moves(table_size):
        return table_size-1
    
    moves = movelist(table_size)
    
    if table_size == 2:
        return moves
    else: #pattern is 1213121
        asterisk = ()
        result = ()
        for move in moveset(table_size//2):
            asterisk += (move*2,)
        num = num_of_distinct_moves(table_size//2)

        while movelist(table_size)[-1] not in result: ##or while len(result) != 2**(table_size-1)-1
        
            result = asterisk
            result += (movelist(table_size)[num],)
            result += asterisk
            result += (movelist(table_size)[num+1],)
            result += asterisk
            result += (movelist(table_size)[num],)
            result += asterisk
            asterisk = result
            num += 2
        
        return result

    
# test:
t4_5 = create_table(4)
solve(t4_5)
print(check_solved(t4_5))

t8_5 = create_table(8)
solve(t8_5)
print(check_solved(t8_5))

t16_5 = create_table(16)
solve(t16_5)
print(check_solved(t16_5))

# Note: It is not advisable to execute run() if the table is large.
