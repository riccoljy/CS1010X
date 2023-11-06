#
# CS1010X --- Programming Methodology
#
# Mission 2 - 2D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to 3 entries. Please update your entry number below.

# Entry 2 of 3
# ============
def beside_frac(frac, p1, p2):
        return quarter_turn_left(stack_frac(frac,
                                     quarter_turn_right(p1),
                                     quarter_turn_right(p2)))   

rectangle=beside_frac(2/5, blank_bb, beside_frac(1/3, black_bb, blank_bb))


def loss(pic):

    #making 2x2 grid
    show(beside_frac(49/100, blank_bb, beside_frac(1/51, black_bb, blank_bb)))
    show(quarter_turn_right(beside_frac(49/100, blank_bb, beside_frac(1/51, black_bb, blank_bb))))

    rectangle=beside_frac(2/5, blank_bb, beside_frac(1/3, pic, blank_bb))
    
    topleft = beside(rectangle, blank_bb)
    topright = beside(rectangle, stack_frac(1/3, blank_bb, rectangle))
    bottomleft = beside(rectangle, rectangle)
    bottomright = beside(rectangle, stack_frac(1/3, blank_bb, quarter_turn_right(rectangle)))
    combined = stack(beside(topleft, topright),
                     beside(bottomleft, bottomright))
    return combined
    

show(loss(make_cross(black_bb)))
# show(<your rune>)



