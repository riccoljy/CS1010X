##CS1010X Recitation 3,         18/1/2023,      Ricco Lim
def sum(term, a, next, b):
    if a>b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)
    
def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))


##Question 1(a)
#Given below,
x=2
def f():
    x = 5
    y = x + 5
    return x + y
#f() + x will return 17 since f() reassigned 5 to x and f() will return 15, then adding x=2 gives 17.

##Question 1(b)
x = 2
y = 3
def g(x):
    y = x+5
    x=7
    return x+y
#g(y) + y will return 18 since g(y) = g(3) = 7+8 = 15. Then +y = +3 = 18

##Question 1(c)
x= 5
def bar(x, y):
    return y(x)
#bar(4, lambda x: x**2) will return 16 since the function will return (lambda x: x**2)(4) which gives 16.
# x = 5 is a redundant statement in this situation since when calling bar, that x is not used.

##Question 2
def my_sum_iter(n):
    result = 0
    for i in range(1, n+1):
        result += i*(i+1)
    return result

##Question 3
#Iterative.
#Order of growth wrt time: O(n)
#Order of growth wrt space: O(1)

##Question 4
def my_sum_rec(n):
    if n == 1:
        return 1*2
    else:
        return my_sum_rec(n-1) + n*(n+1)

#Order of growth wrt time: O(n)
#Order of growth wrt space: O(n)

##Question 5
def my_sum_higher_order_sum(n):
    return sum(lambda x: x*(x+1), 1, lambda x: x+1, n)
#ie:
#T1: lambda x: x*(x+1)
#T2: 1
#T3: lambda x: x+1
#T4: n

##Question 6
def my_sum_higher_order_fold(n):
    return fold(lambda x, y: x+y, lambda x: x*(x+1), n)

##Question 7
def sum_iter(term, a, next, b):
    result = 0
    while a <= b:
        result += term(a)
        a = next(a)
    return result

##Question 8
def fold_iter(op, f, n):
    result = f(n)
    n -= 1
    while n > 0:
        result = op(f(n), result)
        n -= 1
    return result
