#
# CS1010X --- Programming Methodology
#
# Contest 7.2 Template

from more_lazy_susan import *
import random

def create_solver(coins):
    #move = [True] + [False] * (coins - 1)            
    def moveset(table_size):

        def movelist(n):
            if n == 2:
                moves = ([True, False],)
                return moves
            else:
                moves = ()
                flipall = []
                flipnone = []
                for i in range(n):
                    flipall += [True,]
                    flipnone += [False,]
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

    
    
    if coins == 10:
        moves = moveset(16)[:4000]
        new = []
        for move in moves:
            new.append(move[:10])
    elif coins == 13:
        moves = moveset(16)[:4000]
        new = []
        for move in moves:
            new.append(move[:13])
    else:
        moves = moveset(16)[:4000]
        new = []
        for move in moves:
            new.append(move[:15])
            
    def solver(move_id):
        return new[move_id]
    
    return solver
    


# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
get_contest_score(create_solver, True)
