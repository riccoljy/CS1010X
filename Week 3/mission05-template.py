#
# CS1010X --- Programming Methodology
#
# Mission 5
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from hi_graph import *

##########
# Task 1 #
##########

def connect_ends(curve1, curve2):
    
    startpoint = lambda curve: curve(0)
    x_startpoint = lambda curve: x_of(startpoint(curve))
    y_startpoint = lambda curve: y_of(startpoint(curve))

    endpoint = lambda curve: curve(1)
    x_endpoint = lambda curve: x_of(endpoint(curve))
    y_endpoint = lambda curve: y_of(endpoint(curve))
    
    x_diff = x_endpoint(curve1) - x_startpoint(curve2)
    y_diff = y_endpoint(curve1) - y_startpoint(curve2)
    newcurve2 = translate(x_diff, y_diff)(curve2)
    return connect_rigidly(curve1, newcurve2)

#draw_connected_scaled(200, connect_ends(arc, unit_line))
draw_connected_scaled(200, connect_ends(translate(5,5)(arc), translate(1,1)(unit_line)))


##########
# Task 2 #
##########

def show_points_gosper(level, num_points, initial_curve):
    "your solution here!"
    pass

##########
# Task 3 #
##########

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends("your solution here"))
    return inner_gosperize

# testing
# draw_connected(200, your_gosper_curve_with_angle(10, lambda lvl: pi/(2+lvl)))
# draw_connected(200, your_gosper_curve_with_angle(5, lambda lvl: (pi/(2+lvl))/(pow(1.3, lvl))))
