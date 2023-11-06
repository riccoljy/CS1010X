#Final review

#1(a)

def deep_reverse(lst):
    if lst == []:
        return lst
    elif isinstance(lst[0], list):
        return deep_reverse(lst[1:]) + [deep_reverse(lst[0])]
    return deep_reverse(lst[1:]) + [lst[0]]
#1(b)
def deep_sum(lst):
    if lst == []:
        return 0
    elif isinstance(lst[0], list):
        return deep_sum(lst[0]) + deep_sum(lst[1:])
    return lst[0] + deep_sum(lst[1:])


#2(a)

def make_stack():
    stack = []
    def helper(action, *num):
        if action == "push":
            stack.extend(num)
        elif action == "peek":
            return stack[-1]
        elif action == "pop":
            if len(stack) < 1: return None
            return stack.pop()
        elif action == "size":
            return len(stack)
    return helper

#2(b)

def prefix_infix(lst):
    stk = make_stack()
    for i in range(len(lst)):
        curr = lst[i]
        if isinstance(curr, str):
            print(curr)
