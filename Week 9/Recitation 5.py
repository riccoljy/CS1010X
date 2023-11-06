## CS1010X Recitation 5         10 Mar 2023         Ricco Lim

##Question 1

print(1 == 1 == True)

print(1 is 1 == True)

print(("foo" == 'foo') == True)

print((0 == "0") == False)

print((0 is "0") == False)

print((False == False) == True)

print((False == 0) == True)

print(((1, 2) == (1, "2")) == False)

print(((1, 2) is (1, 2)) == True)

print(((1, 2, 3, 4, 5) == (1, 2, 3, 4, 5)) == True)

print(((1, 2, 3, 4, 5) == (1, 2, 3, 5, 4)) == False)

print((((1, 2), (2, 3)) == ((1, 2 ), (3, 2 ))) == False)

#Assignments/Initialising
x = (1, 2)
y = (1, 2)
z = x

print((x is y) == True) #Not sure why

print((x == y) == True)

print((x is z) == True)

print((3 in (1, 2, 3, 4, 5)) == True)

print(((1, 2) in (1, 2, 3, 4, 5)) == False)

print(((2) in (1, 2, 3, 4, 5)) == True)

print((() == ()) == True)

print(((1) == 1) == True)

print(((1,) == 1) == False)

#Assignments/Initialising
a = ((1, 2), (3, 4))
b = (x, (3, 4))

print((x in a) == True)

print((x in b) == True)


##Question 2

def contains(obj, seq):
    if obj in seq:
        position = seq.index(obj)
        return obj is seq[position]
    return False

print(contains(x, a) == False)
print(contains(x, b) == True)

def deep_contains(obj, tup):
    if obj is tup:
        return True
    elif type(tup) == tuple:
        for nest in tup:
            if type(nest) == tuple:
                if deep_contains(obj, nest):
                    return True
            elif type(nest) == int:
                if nest == tup[-1]:
                    return False
    return False
        
x = (1, 2)
a = ((1, 2), ((3, 4), x), (5, 6))

print(deep_contains(x, a) == True)

##Question 3
#3(a)
def fold_right(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], fold_right(fn, initial, seq[1:]))

def fold_left(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(fold_left(fn, initial, seq[:-1]), seq[-1])

def pair(a, b):
    return (a,b)

def divide(a, b):
    return a/b

print(fold_right(divide, 1, (1, 2, 3)) == 1/(2/(3/1)) == 3/2)
print(fold_left(divide, 1, (1, 2, 3)) == (((1/1)/2)/3) == 1/6)
print(fold_right(pair, (), (1, 2, 3)) == (1, (2, (3, ()))))
print(fold_left(pair, (), (1, 2, 3)) == ((((), 1), 2), 3))

#3(b)
#To produce the same values for any sequence, fn should be commutative

##Question 4
#4(a)
#queue will be using a tuple. to enqueue/insert, we will += (num,), and to dequeue, we will .pop(0).

#4(b)
def empty_queue():
    return ()

#Order of growth wrt time & space: O(1)

#4(c)
def enqueue(x, q):
    return q + (x,)

#Order of growth wrt time : O(n)
#Order of growth wrt space: O(n)

#4(d)
def dequeue(q):
    q.pop(0)
    return q

#Order of growth wrt time & space: O(1)

#4(e)
def qhead(q):
    return q[0]

#Order of growth wrt time & space: O(1)

##Question 5
x = (1, 2, 3, 4, 5, 6, 7)

#5(a)
parta = tuple(map(lambda n: n**2, x))
print(parta)

#5(b)
partb = tuple(filter(lambda n: n%2==1, x))
print(partb)
partb2 = tuple(filter(lambda n: x.index(n)%2==0, x))
print(partb2)

#5(c)
partc = tuple(map(lambda n: (n, n), x))
print(partc)

#5(d)
partd = fold_left(pair, 2, tuple(filter(lambda n: x.index(n)>2 and x.index(n)%2==1, x)))
print(partd)

#5(e)
parte = fold_left(pair, (2,), tuple(filter(lambda n: x.index(n)>2 and x.index(n)%2==1, x)))
print(parte)

#5(f)
##partf = "The maximum element of x: " + str(max(x))
##print(partf)
##
##5(g)
##partg = "The minimum element of x: " + str(min(x))
##print(partg)
##
##5(h)
##parth = "The maximum squared even element of x: " + str(max(filter(lambda n: n%2==0, parta)))
##print(parth)
##
##5(i)
##parti = "The sum of the square of each value in x: " + str(sum(parta))
##print(parti)
