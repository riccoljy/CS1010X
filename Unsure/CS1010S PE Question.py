##CS1010X -- CS1010S PE Question, Ricco Lim, 27 Jan 2023


def num_cards(h):
    if h == 1:
        return 2
    else:
        return num_cards(h-1) + 2*h + (h-1) #2*h + h-1 = 3h-1
    
def num_triangles(h):
    def upright(h):
        if h == 1:
            return 0
        elif h == 2:
            return 1
        else:
            #add on for this is summation(h-1)
            return upright(h-1) + h-1 + summation(h-2) #h-1 + summation(h-2) = summation(h-1)
    def inverted(h):
        if h == 1:
            return 0
        elif h == 2:
            return 1
        else:
            add_on = 0
            for i in range(h-1, 0, -2):
                add_on += i
                #add on for this is h-1 + h-3 + h-5 + ... + 3 + 1
            return inverted(h-1) + add_on

    def summation(n):
        if n == 0:
            return n
        else:
            return summation(n-1) + n
    return upright(h) + inverted(h)

for i in range(1,10):
    print(num_triangles(i))
        
