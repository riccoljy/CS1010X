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

# Entry 1 of 3
# ============
def beside_frac(frac, p1, p2):
        return quarter_turn_left(stack_frac(frac,
                                     quarter_turn_right(p1),
                                     quarter_turn_right(p2)))   

def shock(pic, shockness_level):
    #shockness_level will be how shocked he is, integer between 0-10; size of mouth
    eyes = beside(scale(0.25, pic), scale(0.25, pic)) #to be stacked on top of mouth
    shockpic = mouth = blank_bb
    if shockness_level==0:
        mouth = beside_frac(2/10,
                            blank_bb,
                            beside_frac(6/8, #6/8 bc 10-2 left 8, rhs blank also 2, so 6
                                        stack_frac(1/3, blank_bb, stack(black_bb, blank_bb)),
                                        blank_bb))
    else:
        mouth = beside_frac(1/10,
                            blank_bb,
                            beside_frac(8/9, #same, 8/9 = (10-1-1)/(10-1)
                                        scale(shockness_level/10, circle_bb),
                                        blank_bb))
    shockpic = stack(eyes, mouth)
    return shockpic


#if allowed to use overlay, uncomment below for head hahaha
show(overlay(blank_bb,circle_bb))

#show(shock(ribbon_bb, 2))
#show(shock(circle_bb, 0))
show(shock(heart_bb, 9))


