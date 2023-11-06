#
# CS1010X --- Programming Methodology
#
# Mission 2 - 3D Contest
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *

########
# Task #
########

# You may submit up to three entries. Please update your entry number below.

# Entry 3 of 3
# ============
def besiden(n, pic):
    return quarter_turn_right(stackn(n, quarter_turn_left(pic)))

def nxn(n, pic):
    return besiden(n, stackn(n, pic))

def snail():
    background = nxn(10, ribbon_bb)

    ##Snail
    shell = overlay_frac(1/2, scale_independent(0.5, 0.25, ribbon_bb), scale_independent(0.6, 0.3, circle_bb))
    body = scale_independent(0.6, 0.05, circle_bb)
    head = rotate(0.15, scale_independent(0.05, 0.2, circle_bb))


    shadow = scale_independent(1, 0.05, circle_bb)

    snail = overlay_frac(3/4, overlay_frac(1/2, shell,
                         overlay_frac(0, translate(-0.42, 0.041, head),
                                      translate(-0.15, 0.13, body))),
                         translate(0, 0.17, shadow))

    final = overlay_frac(1/6, blank_bb, overlay(snail, background))
    
    return final

hollusion(snail())
