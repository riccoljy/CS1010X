#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 1 of 3
# ============


def SpongebobPatrick(pic, n):
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
    cnb=stack_frac((n-2)/(n-1), circle_bb, bottom) #cnb = centre & bottom
    cnbnr=beside_frac((n-2)/(n-1),cnb,right) #cnbnr = centre & bottom & right
    cnbnrnt=stack_frac(1/n,top, cnbnr) #cnbnrnt = centre & bottom & right & top
    background=beside_frac(1/n,left,cnbnrnt)


    #spongebob
    SBBody = scale_independent(0.3, 0.35, black_bb)
    SBArm = overlay_frac(0, translate(0.025, 0, scale_independent(0.1, 0.05, circle_bb)),
                         scale_independent(0.15, 0.01, black_bb))
    SBBodyArm = overlay_frac(0, SBBody,
                             overlay_frac(0, eighth_turn_left(translate(-0.15, -0.1, SBArm)),
                                          translate(0.17, 0.026, rotate(3*pi/4, SBArm))))

    SBLeg = overlay_frac(0, translate(-0.045, 0.075, scale_independent(0.1, 0.05, circle_bb)) ,
                         scale_independent(0.01, 0.15, black_bb))
    SB = overlay_frac(0, SBBodyArm,
                      overlay_frac(0, translate(-0.07, 0.2, SBLeg),
                                   translate(0.1, 0.2, SBLeg)))

    
    SBPatrick = overlay_frac(1/3, overlay_frac(0, scale(0.75, translate(-0.22, 0, SB)),
                                          translate(0.15, 0, scale(0.4, pentagram_bb))),
                                          overlay(scale(0.7, circle_bb), background))

    
    return SBPatrick


hollusion(SpongebobPatrick(heart_bb, 9))

# Use one of the following methods to display your rune:
# stereogram(<your rune>)
# anaglyph(<your rune>)
# hollusion(<your rune>)
