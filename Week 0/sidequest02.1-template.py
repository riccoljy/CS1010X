#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
from math import sin, cos, pi

##########
# Task 1 #
##########

def tree(n, pic):
    ## Cannot do overlay twice such as :
    # overlay_frac((n-i-1)/n, blank_bb, overlay_frac(1/(i+1), scale((n-i)/n, pic), treepic))
    ## otherwise last layer keeps getting pushed back
    treepic=blank_bb
    for i in range(n):
        treepic = overlay_frac(1/(1+i),
                               scale((n-i)/n, pic),
                               treepic)
    return treepic

# Test
#show(tree(6, pentagram_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(pic, n):
    ## 2 'CONDITIONS'
    #Indiv runes scaled 2/n
    #Radius of circle 1/2 - 1/n
    
    #Eq of circle : x^2 + y^2 = (1/2 - 1/n)^2
    
    r = 1/2 - 1/n #radius r
    helixpic = blank_bb
    for i in range(n):
        x_coord, y_coord = sin((n-1-i)*2*pi/n)*r, cos((n-1-i)*2*pi/n)*r
        helixpic = overlay_frac(1/(1+i), #same 1/(2+i-1) as before.... not sure how it works.......
                                translate(x_coord, y_coord, scale(2/n, pic)),
                                helixpic)
    
    
    return helixpic

# Test
#show(helix(make_cross(rcross_bb), 9))
#show(helix(make_cross(rcross_bb),12))
show(helix(circle_bb,9))
