#
# CS1010X --- Programming Methodology
#
# Mission 1 - Side Quest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

from math import *
##########
# Task 1 #
##########

def egyptian(pic, n):
    def beside_frac(frac, p1, p2):
        return quarter_turn_left(stack_frac(frac,
                                     quarter_turn_right(p1),
                                     quarter_turn_right(p2)))
    ##CREATING EDGES
    #horizontaledge=quarter_turn_left(stackn(n,
    #                                      quarter_turn_right(pic)))
    #verticaledge=stackn(n,pic)
    bottom=quarter_turn_left(stackn(n-2,
                                    quarter_turn_right(pic)))
    right=stackn(n-1, pic)
    top=quarter_turn_left(stackn(n-1,
                                 quarter_turn_right(pic)))
    left=stackn(n, pic)

    ##STACKING INDIVIDUALLY
    cnb=stack_frac((n-2)/(n-1), pic, bottom) #cnb = centre & bottom
    cnbnr=beside_frac((n-2)/(n-1),cnb,right) #cnbnr = centre & bottom & right
    cnbnrnt=stack_frac(1/n,top, cnbnr) #cnbnrnt = centre & bottom & right & top
    egyptimage=beside_frac(1/n,left,cnbnrnt)
    return egyptimage

    
    
# Test
show(egyptian(make_cross(sail_bb), 8))
