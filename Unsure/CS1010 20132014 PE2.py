class Node:

     def __init__(self, name):
         self.name = name
         self.children = []

     def get_name(self):
         return self.name

     def set_children(self, c):
         self.children = c

     def add_children(self, c):
         self.children += c

     def get_children(self):
         return self.children

class Arc:

     def __init__(self, head, tail):
         self.head = head
         self.tail = tail

     def get_head(self):
         return self.head

     def get_tail(self):
         return self.tail

class Graph:

    def __init__(self, nodes, arcs):
        self.N = nodes
        self.A = arcs

        for i in self.N:
            i.set_children([])  # Reset children property
            for j in self.A:
                if j.get_head() == i:
                    tailnode = j.get_tail()
                    i.add_children([j.get_tail()])
                        
    def get_nodes(self):
        return self.N

    def get_arcs(self):
        return self.A

    def search(self, start_node_s, string_target_name):
        lst = []
        res = []
        lst_of_nodes = print_nodes(self.get_nodes())
        for node in lst_of_nodes:
            if node[1] == []: continue
            elif string_target_name in node[1]:
                lst = node
                break
        if lst == []:
            return ("Fruitless hunt!", lst)
        #else if lst not empte eg lst = ['S', ['A', 'D']]
        
        if start_node_s.get_name() == lst[0]: ##assuming len(lst) == 1 FOR NOW
            return ("Target found!", [start_node_s.get_name(), string_target_name])
        intermediate = self.search(start_node_s, lst[0])
        newlst = intermediate[1][:]
        newlst.append(string_target_name)
        return ("Target found!", newlst)
        

s = Node('S')
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
h = Node('Home')

ab = Arc(a, b)
ac = Arc(a, c)
ae = Arc(a, e)
bc = Arc(b, c)
bd = Arc(b, d)
bf = Arc(b, f)
cb = Arc(c, b)
cd = Arc(c, d)
cf = Arc(c, f)
da = Arc(d, a)
db = Arc(d, b)
dc = Arc(d, c)
de = Arc(d, e)
eb = Arc(e, b)
ec = Arc(e, c)
ed = Arc(e, d)
ef = Arc(e, f)
eh = Arc(e, h)
fa = Arc(f, a)
fb = Arc(f, b)
fd = Arc(f, d)
fh = Arc(f, h)
sa = Arc(s, a)
sc = Arc(s, c)
sd = Arc(s, d)

def print_nodes(lst):
    out = []
    for i in lst:
        out.append([i.get_name(), list(c.get_name() for c in i.get_children())])
    return out

def test_3a(n):
    N1 = [s, a, b, c, d, e, f, h]
    A1 = [ab, bc, cd, de, ef, fh, sa]
    N2 = [s, a, b, c, d, e, f, h]
    A2= [ab, ac, ae, bd, bf, cb, cf, da, ec, ef, eh, fa, fh, sa, sd]
    N3 = [s, b, c, e, f]
    A3 = [sc, bc, bf, cb, cf, fb]
    if n == 1:
        G1 = Graph(N1, A1)
        return print_nodes(G1.get_nodes())
    elif n == 2:
        G2 = Graph(N2, A2)
        return print_nodes(G2.get_nodes())
    elif n == 3:
        G3 = Graph(N3, A3)
        return print_nodes(G3.get_nodes())


N = [s, a, b, c, d, e, f, h]
A = [ab, bc, cd, de, ef, fh, sa]
G1 = Graph(N,A)
