#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

"""For unit_circle, the points are all equidistant while for alternative_unit_circle, the points are more clustered near t=0,
the start point. After examining the codes of both unit_circle and alternative_unit_circle, this clustering of points near t=0
can be attributed to performing sine and cosine to 2*pi* t**2 as compared to the unit_circle's sine and cosine of 2*pi*t.
When sine nand cosine are performed on 2*pi* t**2, the x and y coordinates of the points will be more clustered at t=0"""

##########
# Task 2 #
##########

# (a)
def spiral(t):
    return make_point(t*sin(2*pi*t), t*cos(2*pi*t))

#draw_connected_scaled(1000, spiral)

# (b)
def heart(t):
    return connect_rigidly(spiral, reflect_through_y_axis(spiral))(t)
                   

def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point( -(x_of(pt)), y_of(pt))
    return reflected_curve

draw_connected_scaled(1000, heart)
