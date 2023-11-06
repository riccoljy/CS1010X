#
# CS1010X --- Programming Methodology
#
# Mission 5 - Sidequest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph_connect_ends import *

##########
# Task 1 #
##########

def kochize(level):
    if level == 0:
        return unit_line
    else:
        LHS = (connect_ends(kochize(level-1), rotate(pi/3)(kochize(level-1))))
        RHS = (connect_ends(rotate(-pi/3)(kochize(level-1)), kochize(level-1)))
        return scale(1/3)(connect_ends(LHS, RHS))

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

#show_connected_koch(5, 4000)
#show_connected_koch(4, 4000)

##########
# Task 2 #
##########
def reflect_through_y_axis(curve):
    def reflected_curve(t):
        pt = curve(t)
        return make_point( -(x_of(pt)), y_of(pt))
    return reflected_curve

def snowflake():
    top = kochize(5)
    rhs = rotate(-2*pi/3)(top)
    lhs = rotate(2*pi/3)(top)
    return connect_ends(top, connect_ends(rhs, lhs))

def wrong_snowflake():
    top = kochize(5) #start top left, end top right
    rhs = rotate(pi/2)(reflect_through_y_axis(top)) #start top right, end bottom right
    bottom = rotate(pi)(top) #start bottom right, end bottom left
    lhs = rotate(-pi/2)(reflect_through_y_axis(top)) #start bottom left, end top right

    #since start and end points can now be connected,
    return connect_ends(top, connect_ends(rhs, connect_ends(bottom, lhs)))

draw_connected_scaled(2000, (snowflake()))

