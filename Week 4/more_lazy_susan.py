import secrets

# Maximum number of moves allowed per table.
MAX_MOVES = 4000

# The various numbers of coins used for the contest.
CONTEST_LEVELS = (10, 13, 15)

# Score modifiers used for each level.
SCORE_MODIFIERS = (1, 4, 7)

# The number of rounds to run the solver for, per level.
ROUNDS_PER_LEVEL = 1000


class Table(object):

    def __init__(self, size):
        assert size > 1
        self.turn = 0
        self.display = False
        self.size = size
        self.randomize()
        while self.is_solved(): # don't start with a solved state
            self.randomize()

    def randomize(self):
        self.state = [bool(secrets.randbits(1)) for i in range(self.size)]

    def rotate(self):
        for i in range(secrets.randbelow(self.size)):
            self.state.append(self.state.pop(0))

    def flip(self, move=None):
        self.turn += 1
        if move is None:
            for i in range(self.size):
                if secrets.randbits(1):
                    self.flip_at(i)
        else:
            for i in range(min(self.size, len(move))):
                if move[i]:
                    self.flip_at(i)

    def flip_at(self, position):
        self.state[position] = not self.state[position]

    def is_solved(self):
        return len(set(self.state)) == 1


# Run the solver on a new randomized table containing
# the specified number of coins.
def run_solver(coins, solver):
    table = Table(coins)
    while table.turn < MAX_MOVES:
        table.flip(solver(table.turn))
        if (table.is_solved()):
            return table.turn
        table.rotate()
    return -1


# Compute the score of the solver. If verbose is
# set to true, the score of each round will be printed.
def get_contest_score(create_solver, verbose=False):
    total_moves = 0
    total_score = 0
    for i in range(len(CONTEST_LEVELS)):
        size = CONTEST_LEVELS[i]
        if verbose:
            print(f'=== Level {i+1}: {size} coins ===')

        for r in range(ROUNDS_PER_LEVEL):
            moves = run_solver(size, create_solver(size))
            score = int((MAX_MOVES - moves) * SCORE_MODIFIERS[i]) \
                    if moves >= 0 else 0
            if verbose:
                print(f'  Round {r+1}: {moves} moves, {score} score')
            total_moves += moves if moves >= 0 else MAX_MOVES
            total_score += score

    if verbose:
        print(f'=== Total moves: {total_moves} ===')
        print(f'=== Total score: {total_score} ===')
    return total_score
