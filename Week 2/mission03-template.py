#
# CS1010X --- Programming Methodology
#
# Mission 3
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

###########
# Task 1a #
###########

def compose(f, g):
    return lambda x:f(g(x))

def thrice(f):
    return compose(f, compose(f, f))

def repeated(f, n):
    if n == 0:
        return identity
    else:
        return compose(f, repeated(f, n - 1))

# Your answer here:
# n = 9

###########
# Task 1b #
###########

identity = lambda x: x
add1 = lambda x: x + 1
sq = lambda x: x**2

# (i) print(thrice(thrice)(add1)(6))
# Explanation: thrice(thrice) returns a function that composes add1 3**3 = 27 times.
#               Hence, 6 + add1 27 times => 6+27 = 33

# (ii) print(thrice(thrice)(identity)(compose))
# Explanation: Prints function memory address since thrice(thrice)(identity)
#               will return the function identity, and identity(compose) will return
#               compose. Calling compose without any arguments returns its memory address.

# (iii) print(thrice(thrice)(sq)(1))
# Explanation: thrice(thrice)(sq) => sq(sq(sq(sq(......sq)...) so that there are 27 sq functions.
#               However, since square of 1 = 1, performing sq on 1 repeatedly will yield 1.

# (iv) print(thrice(thrice)(sq)(2))
# Explanation: Similar to (iii), the result should be 2**2**2**...**2 such that 2 is squared
#               # 27 times ultimately. (ie: Tetration/Power tower of 2, 27 times in this case)


###########
# Task 2a #
###########

def combine(f, op ,n):
    result = f(0)
    for i in range(n):
        result = op(result, f(i))
    return result

def smiley_sum(t):
    def f(x):
        return x * x
    def op(x, y):
        if x == 0 and y == 1:
            return x+y
        else:
            return x + 2*y
    n = t+1
    # Do not modify this return statement
    return combine(f, op, n)

###########
# Task 2b #
###########

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def new_fib(n):
    def f(x):
        if x == 0 or x == 1:
            return x
        else:
            fib_n = 0
            fib_n_plus_1 = 1
            for i in range(x-2):
                fib_n, fib_n_plus_1 = fib_n_plus_1, fib_n + fib_n_plus_1
            return fib_n
    def op(x, y):
        return x+y
    return combine(f, op, n+1)


# Your answer here:

## Although my new_fib function works &  utilises combine, it does not
## REALLY make use of combine since my function f already is the
## fibonacci function (although iteratively).
##
## I suspect that using combine is not required because the fibonacci sequence utilises
## the prevous 2 terms which can already be computed in function f, given the first 2 terms.
## Compared to smiley_sum function where it is all computed from argument t without
## the need for pre-given first few terms.
