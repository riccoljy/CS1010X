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

# Entry 2 of 3
# ============

def plane():
    def besiden(n, painter): return quarter_turn_left(stackn(n, quarter_turn_right(painter)))
    clouds = besiden(3, scale_independent(0.8, 0.5, image_to_painter("Clouds.png")))

    #Building Plane pewwwwwww
    body = scale_independent(0.8, 0.1, circle_bb)
    wings = scale_independent(0.25, 0.4, flip_horiz(sail_bb))
    bodywings = overlay_frac(0, body,
                             overlay_frac(0, translate(-0.025, -0.1, rotate(-0.5, wings)),
                                          translate(-0.025, 0.1, rotate(0.5, flip_vert(wings)))))
    plane = overlay_frac(0, bodywings,
                         overlay_frac(0, translate(0.35, -0.06, scale(0.5, rotate(-0.5, wings))),
                                      translate(0.35, 0.06, scale(0.5, rotate(0.5, flip_vert(wings))))))

    return stack_frac(1/3, clouds, plane)
    

#stereogram(plane())
show(plane())
