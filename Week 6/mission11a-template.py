#
# CS1010X --- Programming Methodology
#
# Mission 11a
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> <your collaborator's name>

###############
# Mission 11a #
###############

##########
# Task 1 #
##########

# With these operations, compound generic operations can be defined, such as
# def square(x):
#   return mul(x, x)

# (a) What are the types of the input and output of the generic square operation?
# Answer: Generic-Num -> Generic-Num

# (b) Why would we prefer to define square in the above way, rather than:
# def square(x):
#    return apply_generic("square", x)
# Answer: This eases the work on the programmer in maintaning the table. If there is a new
#           type tag (ie: a new form of representation), the table would have to be updated
#           just to find the square of this new type. However, using mul (which would have
#           been modified to accept this new type already) would save that one extra step.

#           For example, if there were new types of Generic-Num, say Generic-ABC, Generic-DEF,
#           Generic-GHI, etc, then operations like add, sub, mul, and div would have to
#           be coded to suit those types as well.
#           Then, if def square(x): return mul(x, x) is used instead, it can be used right away.
#           However, if def square(x): return apply_generic("square", x) is used instead,
#           then this square function would have to be put on the _operation_table for EACH of the new
#           types of Generic-ABC, Generic-DEF, etc., and that would be much more tedious.
#           

##########
# Task 2 #
##########
# In the ordinary number package, a generic number operator is indexed by the
# name of the operator and a tuple of strings. For example, the add operator is
# indexed by ’add_ord’ and (’ordinary’, ’ordinary’); negation is indexed by
# ’negate_ord’ and (’ordinary’, ).
# In contrast, the constructor that creates an ordinary number is indexed by
# ’make_ord’ and just a string ’ordinary’. Explain why we have such a difference.

# Hint: Consider the differences in the process of the creation of a Generic-Num,
# such as create_ordinary, and the operations we can apply on Generic-Num, such
# as add. How is make_ord invoked, and how is add_ord invoked?

# Answer:
# make_ord is invoked when calling the function create_ordinary with argument x, and it returns get("make", "ordinary")(x). In other words,
# the number/argument x will be tagged with the "ordinary" tag and become a Generic-Ord

# On the other hand, add_ord is invoked when we use the add function on 2 Generic-Ord inputs. The 2 inputs will be
# stripped of their tags and the 2 Rep_Ord will be added, before giving an output and tagging it again, becoming a Generic-Ord

# When creating an ordinary number (Generic-Ord), the string/tag "ordinary" is simply tagged onto the number, whereas for
# the operators, the tuple is used to check whether that operator is used for that type of Generic-Num. If add is used on
# 2 Generic-Rat instead, then add_ord will not be used since their tags are not (’ordinary’, ’ordinary’), and the appropriate function
# (indexed by 'add_rat' and ('rational', 'rational')) will be used instead.



##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic rational number. Here are two tries at
# producing 9/10. Which is the right way?

# first_try = create_rational(9, 10)
# second_try = create_rational(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9/10 and 3/10 and then try to add
# them? Why does this happen?

# Right way: second_try = create_rational(create_ordinary(9), create_ordinary(10))
# What happens: Exception: ('Bad tagged datum -- type_tag ', 9) is raised.
# Why it happens:
# The numerator and denominator of the rational number is ultimately made of Generic-Ord numbers, and the operators
# for the rational numbers are programmed to operate on those Generic-Ord numbers.
# This can be further seen in the code of add_rat:

##def add_rat(x, y):
##        return make_rat( add(mul(numer(x), denom(y)),
##                             mul(denom(x), numer(y))),
##                         mul(denom(x), denom(y)) )

# add_rat uses functions like add and mul whichwill require the numerators and denominators to be tagged. Hende, when the wrong
# way is used, the numerator and denomiator do not have tags and add and mul cannnot be performed on them. Only when they are
# of Generic-Ord type can the numerator and denominator be worked on, just like in second_try.



##########
# Task 4 #
##########

# Produce expressions that define r2_7 to be the generic rational number whose numerator part is
# 2 and whose denominator part is 7, and r3_1 to be the generic rational number whose numerator
# is 3 and whose denominator is 1. Assume that the expression
# >>> csq = square(sub(r2_7, r3_1))
# is evaluated. Draw a box and pointer diagram that represents csq.

# As an example, the following is a box and pointer diagram that represents x, a Generic-
# Ord number:
# x = create_ordinary(5)
#
#         +---+---+---+---+
# x  -->  |       |       |
#         +---+---+---+---+
#             |       |
#             v       v
#         "ordinary"  5

# FILL IN YOUR ANSWERS HERE:
# r2_7 = create_rational(create_ordinary(2), create_ordinary(7))
# r3_1 = create_rational(create_ordinary(3), create_ordinary(1))

# csq = square(sub(r2_7, r3_1))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##  csq -->   |       |       |  
##            +---+---+---+---+
##                |       |
##                v       |
##           "rational"   |
##                        v
##                    +---+---+---+---+
##                    |       |       |
##                    +---+---+---+---+
##                        |       |
##            -------------       |
##            |                   |
##            v                   v
##        +---+---+---+---+   +---+---+---+---+
##        |       |       |   |       |       |
##        +---+---+---+---+   +---+---+---+---+
##            |       |           |       |
##            v       v           v       v
##       "ordinary"  361     "ordinary"   49

##########
# Task 5 #
##########

# Within the generic rational number package, the internal add_rat function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer:
# The code for add_rat is as seen:

##def add_rat(x, y):
##        return make_rat( add(mul(numer(x), denom(y)),
##                             mul(denom(x), numer(y))),
##                         mul(denom(x), denom(y)) )

# if named as add instead of add_rat, the inner add function in line 2 will become a recursive call instead of a call to the generic add. This will
# result in a never-ending loop.



##########
# Task 6 #
##########

from generic_arith import *

# Modify install_rational_package, indicating clearly your modifications.
def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )

    def negate_rat(x): # (RepRat) -> Generic-Rat
        return make_rat( negate(numer(x)), denom(x))
    def is_zero_rat(x): # (RepRat) -> Py-Bool
        return is_zero(numer(x))
    def is_eq_rat(x, y): # (RepRat, RepRat) -> Py-Bool
        simplestx = div(numer(x), denom(x))
        simplesty = div(numer(y), denom(y))
        return simplestx == simplesty        
    
    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)

    put("negate", ("rational",), negate_rat)
    put("is_zero", ("rational",), is_zero_rat)
    put("is_equal", ("rational", "rational"), is_eq_rat)
    
install_rational_package()

def create_rational(x, y):
    return get("make", "rational")(x, y)

# Change the values for the test variables below
r1_2 = create_rational(create_ordinary(1), create_ordinary(2))
r2_4 = create_rational(create_ordinary(2), create_ordinary(4))
r1_8 = create_rational(create_ordinary(1), create_ordinary(8))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(r1_2, mul(r2_4, r1_2)), add(r1_8, r1_8)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
