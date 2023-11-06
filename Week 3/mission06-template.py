#
# CS1010X --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from diagnostic import *
from hi_graph_connect_ends import *

# Mission 6 requires certain functions from Mission 5 to work.
# Do copy any relevant functions that you require in the space below:

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        return put_in_standard_position(connect_ends(rotate(theta)(curve_fn), rotate(-theta)(curve_fn)))
    return inner_gosperize

# Do not copy any other functions beyond this line #
##########
# Task 1 #
##########

# Example from the mission description on the usage of time function:
# profile_fn(lambda: gosper_curve(1000)(0.1), 500)

# Choose a significant level for testing for all three sets of functions.

# -------------
# gosper_curve:
# -------------
# write down and invoke the function that you are using for this testing
# in the space below

readings = []
for i in range(5):
	readings.append(profile_fn(lambda: gosper_curve(50)(0.2), 100))
print(readings, sum(readings)/5)


# Time measurements


##43.6704
##27.953700000000026
##30.123300000000018
##24.208699999999972
##30.061400000000017

##average time = 31.20350000000001

# ------------------------
# gosper_curve_with_angle:
# ------------------------
# write down and invoke the function that you are using for this testing
# in the space below

readings = []
for i in range(5):
	readings.append(profile_fn(lambda: gosper_curve_with_angle(50, lambda lvl: pi/4)
(0.2), 100))
print(readings, sum(readings)/5)


# Time measurements

##22.843100000000007
##31.19830000000001
##23.249499999999923
##23.579900000000098
##22.371200000000037

##average time = 24.648400000000017


# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
# write down and invoke the function that you are using for this testing
# in the space below

readings = []
for i in range(5):
	readings.append(profile_fn(lambda: your_gosper_curve_with_angle(50, lambda lvl: pi/4)
(0.2), 100))
print(readings, sum(readings)/5)

# Time measurements

##2234.7292999999995
##2374.3947999999996
##2536.4942
##2510.3005000000003
##2555.5594999999994

##average time = 2442.2956599999998


# Conclusion:
# gosper_curve_with_angle < gosper_curve < your_gosper_curve_with_angle in terms of
# their timings. gosper_curve_with_angle has the biggest advantage in speed while
# your_gosper_curve_with_angle has the worst.

# This implies that although all produce the same curve when angle = pi/4 ,
# gosper_curve_with_angle, which is more customisable than gosper_curve
# (being able to alter the angle) has an advantage in speed over gosper_curve.

# Meanwhile, although your_gosper_curve_with_angle can also alter the angle,
# the need to undergo put_in_standard_position and connect_ends unlike less demanding
# functions like the scale, translate, and connect_rigidly functions
# in gosper_curve_with_angle makes your_gosper_curve_with_angle have least advantage

##########
# Task 2 #
##########

#  1) Yes, both work and achieve the same purpose.


#  2) Using joe_rotate as a function means that for every t value, curve(t) has to be
#       computed twice in x, y = x_of(curve(t)), y_of(curve(t)), as compared to the once
#       in rotate. Hence, joe_rotate will have time which is exponential in the level.

##########
# Task 3 #
##########

#
# Fill in this table:
#
#                    level      rotate       joe_rotate
#                      1          <3>           <4>
#                      2          <5>           <10>
#                      3          <7>           <22>
#                      4          <9>           <46>
#                      5          <11>          <94>
#
#  Evidence of exponential growth in joe_rotate.
