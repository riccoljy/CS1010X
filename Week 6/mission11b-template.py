#
# CS1010X --- Programming Methodology
#
# Mission 11b
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

# Collaborator: <your collaborator's matric> <your collaborator's name>

###############
# Mission 11b #
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
# 2 Generic-Ord instead, then add_ord will not be used since their tags are not (’ordinary’, ’ordinary’), and the appropriate function
# (indexed by 'add_com' and ('complex', 'complex')) will be used instead.

##########
# Task 3 #
##########

# There’s a right way and a wrong way to create a generic complex number. Here are two tries at
# producing 9+10i. Which is the right way?

# first_try = create_complex(9, 10)
# second_try = create_complex(create_ordinary(9), create_ordinary(10))

# What happens when you use the wrong way to produce 9+10i and 3+10i and then try to add
# them? Why does this happen?

# Right way: second_try = create_complex(create_ordinary(9), create_ordinary(10))
# What happens: Exception: ('Bad tagged datum -- type_tag ', 9) is raised.
# Why it happens:
# The real part and imaginary part of the complex number is ultimately made of Generic-Ord numbers, and the operators
# for the complex numbers are programmed to operate on those Generic-Ord numbers.
# This can be further seen in the code of add_com:

##def add_com(x, y):
##        return make_com( add(real(x), real(y)),
##                         add(imag(x), imag(y)) )

# add_com uses the (generic) add function will require thereal & imaginary parts to be tagged. Hende, when the wrong
# way is used, the real & imaginary parts do not have tags and add cannnot be performed on them. Only when they are
# of Generic-Ord type can the real & imaginary parts be worked on, just like in second_try.


##########
# Task 4 #
##########

# Produce expressions that define c2_plus_7i to be the generic complex number whose real part is 2
# and whose imaginary part is 7, and c3_plus_1i to be the generic complex number whose real part
# is 3 and whose imaginary part is 1. Assume that the expression
# >>> csq = square(sub(c2_plus_7i, c3_plus_1i))
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
# c2_plus_7i = create_complex(create_ordinary(2), create_ordinary(7))
# c3_plus_1i = create_complex(create_ordinary(3), create_ordinary(1))

# csq = square(sub(c2_plus_7i, c3_plus_1i))

## Sample ASCII box and pointer diagrams (with 2 components) for your convenience
##            +---+---+---+---+
##  csq -->   |       |       |  
##            +---+---+---+---+
##                |       |
##                v       |
##            "complex"   |
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
##       "ordinary"  -35     "ordinary"   -12

##########
# Task 5 #
##########

# Within the generic complex number package, the internal add_com function
# handled the addition operation. Why is it not
# possible to name this function "add"?

# Answer:
# The code for add_com is as seen:

##def add_com(x, y):
##        return make_com( add(real(x), real(y)),
##                         add(imag(x), imag(y)) )

# if named as add instead of add_com, the inner add function in line 2 will become a recursive call instead of a call to the generic add. This will
# result in a never-ending loop.


##########
# Task 6 #
##########

from generic_arith import *

# Modify install_complex_package, indicating clearly your modifications.
def install_complex_package():
    def make_com(x, y):
        return tag(repcom(x, y))
    def repcom(x, y):
        return (x, y)
    def real(x):
        return x[0]
    def imag(x):
        return x[1]
    def tag(x):
        return attach_tag("complex", x)

    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
    def add_com(x, y):
        return make_com( add(real(x), real(y)),
                         add(imag(x), imag(y)) )
    def sub_com(x, y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def mul_com(x, y):
        return make_com( sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def div_com(x, y):
        com_conj = content(complex_conjugate(y))
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
                         div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return make_com(real(x), negate(imag(x)))

    def negate_com(x): # (RepCom) -> Generic-Com
        return make_com( negate(real(x)), negate(imag(x)))
    def is_zero_com(x): # (RepCom) -> Py-Bool
        return is_zero(real(x)) and is_zero(imag(x))
    def is_eq_com(x, y): # (RepCom, RepCom) -> Py-Bool
        return x == y

    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)

    put("negate", ("complex",), negate_com)
    put("is_zero", ("complex",), is_zero_com)
    put("is_equal", ("complex", "complex"), is_eq_com)
    

install_complex_package()

def create_complex(x,y):
    return get("make", "complex")(x, y)

# Change the values for the test variables below
c_neg3_plus_10i = create_complex(create_ordinary(-3), create_ordinary(10))
c1_plus_2i = create_complex(create_ordinary(1), create_ordinary(2))
c1_plus_3i = create_complex(create_ordinary(1), create_ordinary(3))

#################
# Do not change #
#################
def gradeThis():
    if is_equal(sub(c_neg3_plus_10i, mul(c1_plus_2i, c1_plus_3i)),
        add(c1_plus_2i, c1_plus_3i)):
        print("Well done!")
    else:
        print("Please check your solution.")
gradeThis()
