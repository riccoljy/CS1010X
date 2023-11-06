#Recitation 8        Ricco Lim      28/04/2023


##Question 1
a = (("apple", 2), ("orange", 4), (5, 7))
b = dict(a)

c = [[1,2], [3,4], [5,7]]
d = dict(c)

print(b["orange"] == 4)
print(b[5] == 7)
#print(b[1] == KeyError) 

b["bad"] = "better"
b[1] = "good"

##for key in b.keys():
##    print(key)
# this will print the keys ie: "apple", "orange", 5, "bad", 1

##for val in b.values():
##    print(val)
#this will print the values ie: 2, 4, 7, "better", "good"

del b["bad"]
del b["apple"]

print(tuple(b.keys()) == ("orange", 5, 1))
print(list(b.values()) == [4, 7, "good"])

##Question 2
def make_stack():
    s = []
    def stack(string):
        if string == "is_empty":
            return s == []
        elif string == "clear":
            s.clear()
            return
        elif string == "peek":
            if s == []: return None
            return s[-1]
        elif string == "push":
##            def pusher(item):
##                s.append(item)
##            return pusher
            return lambda x: s.append(x)
        elif string == "pop":
            if s == []: return None
            return s.pop()
        elif string == "whole":
            return s
    return stack

##Question 3
def push_all(stack, seq):
    for element in seq:
        stack("push")(element)
    return stack("whole")

##Question 4
def pop_all(stack):
    output = []
    while not stack("is_empty"):
        output.append(stack("pop"))
    return output

##Question 5
def make_calculator():
    stack = make_stack()
    ops = {"+": lambda x, y: x + y, \
           '-': lambda x, y: x - y, \
           '*': lambda x, y: x * y, \
           '/': lambda x, y: x / y}
    def oplookup(msg, *args):
        if msg == "ANSWER":
            return stack("peek")
        elif msg == "CLEAR":
            stack("clear")
            return
        elif  msg == "NUMBER_INPUT":
            stack("push")(args[0])
            return
        elif msg == "OPERATION_INPUT":
            x = stack("pop")
            y = stack("pop")
            res = (ops[args[0]])(x, y)
            stack("push")(res)
        else:
            raise Exception("calculator doesn't" + msg)
    return oplookup
