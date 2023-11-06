#
# CS1010X --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
import math


###########
# Task 1a #
###########

def fractal(pic, n):
    if n == 1:
        return pic
    else:
        return beside(pic,
                      stack(fractal(pic, n-1),fractal(pic, n-1)))

# Test
#show(fractal(make_cross(rcross_bb), 3))
#show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(pic, n):
    new_pic = pic
    while n > 1:
        new_pic = beside(pic,
                         stack(new_pic, new_pic))
        print(n)
        n = n-1
    return new_pic
        

# Test
#show(fractal_iter(make_cross(rcross_bb), 3))
#show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(pic1, pic2, n):
    if n == 1:
        return pic1
    else:
        return stack(pic1,
                      beside(dual_fractal(pic2, pic1, n-1),
                            dual_fractal(pic2, pic1, n-1)))

        
    

# Test
show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
#show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(pic1, pic2, n):
    i=1
    if n%2==1:
        newpic=pic1
        pic1,pic2=pic2,pic1
    else:
        newpic=pic2
    while i<n:
        newpic=beside(pic1,
                  stack(newpic, newpic))
        i=i+1
        pic1,pic2=pic2,pic1
    return newpic


# Test
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 5))
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
#show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(pic1, pic2, pic3, pic4):
    lhs=stack(pic4,
              overlay_frac(1/4, blank_bb, pic3))
    rhs=stack(overlay_frac(3/4, blank_bb, pic1),
              overlay_frac(1/2, blank_bb, pic2))
    newpic=beside(lhs, rhs)
    return newpic

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
