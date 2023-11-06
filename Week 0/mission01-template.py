#
# CS1010X --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


##########
# Task 1 #
##########

def mosaic(pic1, pic2, pic3, pic4):
    return beside(stack(pic4, pic3),\
                  stack(pic1, pic2))


# Test
#show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))

##########
# Task 2 #
##########

def simple_fractal(pic):
    return beside(pic, \
                  stack(pic, pic))

# Test
#show(simple_fractal(make_cross(rcross_bb)))


