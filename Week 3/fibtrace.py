from diagnostic import *
from hi_graph_connect_ends import *

#EXAMPLE ON HOW TO USE trace

##def fib(n):
##    if n < 2:
##        return n
##    else:
##        return fib(n - 1) + fib(n - 2)
##
##trace(fib)
##fib(3)
##untrace(fib)
##fib(3)

for x in range(1, 6):
    print("for (original) rotate, where level = ", x)
    trace(x_of)
    gosper_curve(x)(0.5)
    untrace(x_of)

    print("for joe's rotate, where level = ", x)
    original_rotate = rotate
    replace_fn(rotate, joe_rotate)
    trace(x_of)
    gosper_curve(x)(0.5)
    untrace(x_of)
    replace_fn(rotate, original_rotate)

##ouput:

##for (original) rotate, where level =  1
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##for joe's rotate, where level =  1
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##for (original) rotate, where level =  2
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##for joe's rotate, where level =  2
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##for (original) rotate, where level =  3
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##for joe's rotate, where level =  3
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115340D0>)
##--> 0.0
##for (original) rotate, where level =  4
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537D90>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537AE8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537D90>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537AE8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537D90>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537AE8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537D90>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537AE8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537D90>)
##--> 0.0
##for joe's rotate, where level =  4
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115379D8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115377B8>)
##--> 0.0
##for (original) rotate, where level =  5
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537EA0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537EA0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537EA0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537EA0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537EA0>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE115376A8>)
##--> 0.0
##for joe's rotate, where level =  5
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537BF8>)
##--> 0.0
##x_of(<function make_point.<locals>.<lambda> at 0x000001CE11537840>)
##--> 0.0

