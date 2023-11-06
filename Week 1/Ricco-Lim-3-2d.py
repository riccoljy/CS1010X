#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 3 of 3
# ============

def beside_frac(frac, p1, p2):
        return quarter_turn_left(stack_frac(frac,
                                     quarter_turn_right(p1),
                                     quarter_turn_right(p2)))

def besiden(n, painter):
    return quarter_turn_left(stackn(n, quarter_turn_right(painter)))

def HappyCNY():
    RHSLine = beside_frac(3/4, blank_bb, stackn(3, black_bb))
    H = beside_frac(1/3, RHSLine, beside(stack_frac(2/5, blank_bb, quarter_turn_left(RHSLine)), turn_upside_down(RHSLine)))

    MidVertLine = beside_frac(12/25, blank_bb, beside_frac(1/13, stackn(3, black_bb), blank_bb))
    A = beside(translate(0.5, 0, flip_horiz(sail_bb)),
               translate(-0.5, 0, sail_bb))
    P = (beside(RHSLine, translate(-0.25, 0, stack_frac(1/2, circle_bb, blank_bb))))

    Y = stack(turn_upside_down(A), scale(1.3, translate(0, -0.1, MidVertLine)))

    HAPPY = beside_frac(1/5, H,
                       beside_frac(1/4, A,
                                   beside_frac(1/3, P,
                                               beside_frac(1/2, P, Y))))
    C = scale(0.75, stack_frac(1/5, besiden(5, black_bb),
                   stack_frac(3/4, beside_frac(1/5, stackn(4, black_bb), blank_bb),
                              besiden(5, black_bb))))
    N = quarter_turn_right(C)

    CNY = beside_frac(1/3, C,
                      beside_frac(1/2, N, scale(0.75, Y)))
    return stack(HAPPY, beside_frac(3/4, CNY, scale(0.5, heart_bb)))

show(HappyCNY())



