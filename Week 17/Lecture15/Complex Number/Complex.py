from math import *

class Complex (object):
    def __init__(self):
        pass
    def realpart(self):
        pass
    def imagpart(self):
        pass
    def angle(self):
        pass
    def mag(self):
        pass
    def add(self, c):
        pass
    def minus(self, c):
        pass
    def times(self, c):
        pass
    def toString(self):
        if (self.imagpart() == 0):
            return str(self.realpart())
        elif (self.imagpart() < 0):
            return str(self.realpart())+str(self.imagpart())+"i"
        else:
            return str(self.realpart())+"+"+str(self.imagpart())+"i"


class ComplexCart(Complex):
    def __init__(self, r, i):
        self.real = r
        self.imag = i
    def realpart(self):
        return self.real
    def imagpart(self):
        return self.imag
    def magnitude(self):
        return sqrt(self.realpart()*self.realpart()+self.imag*self.imag)   
    def angle(self):
        if self.real!=0:
            if (self.real < 0):
                return pi + atan(self.imag/self.real)
            return atan(self.imag/self.real)
        elif self.imag == 0:
            return 0
        elif self.imag > 0:
            return pi/2
        else:
            return -pi/2     
    def add(self, c):
        self.real += c.realpart()
        self.imag += c.imagpart()
    def minus(self, c):
        self.real -= c.realpart()
        self.imag -= c.imagpart()
    def times(self, c):
        tempReal = self.real * c.realpart() - self.imag * c.imagpart()
        self.imag = self.real * c.imagpart() + self.imag * c.realpart()
        self.real = tempReal

class ComplexPolar(Complex):
    def __init__(self, m, a):
        self.mag = m
        self.ang = a
    def realpart(self):
        return self.mag * cos(self.ang)
    def imagpart(self):
        return self.mag * sin(self.ang)
    def magnitude(self):
        return self.mag
    def angle(self):
        return self.ang   
    def add(self, c):
        real = self.realpart() + c.realpart()
        imag = self.imagpart() + c.imagpart()
        self.mag = sqrt(real*real + imag*imag)
        if (real != 0):
            if (real < 0):
                self.ang = pi + atan(imag/real)
            else:
                self.ang = atan(imag/real)
        elif (imag == 0):
            self.ang = 0
        elif (imag > 0):
            self.ang = pi/2
        else:
            self.ang = -pi/2         
    def minus(self, c):
        real = self.realpart() - c.realpart()
        imag = self.imagpart() - c.imagpart()
        self.mag = sqrt(real*real + imag*imag)
        if (real != 0):
            if (real < 0):
                self.ang = pi + atan(imag/real)
            else:
                self.ang = atan(imag/real)
        elif (imag == 0):
            self.ang = 0
        elif (imag > 0):
            self.ang = pi/2
        else:
            self.ang = -pi/2         
    def times(self, c):
        self.mag *= c.magnitude()
        self.ang += c.angle()
        self.ang = self.ang % (2*pi)


# testing ComplexCart
a = ComplexCart(10.0, 12.0)
b = ComplexCart(1.0, 2.0)
a.add(b)
print("a=a+b is", a.toString())
a.minus(b)
print("a-b (which is the original a) is", a.toString())
print("Angle of a is", str(a.angle()))
a.times(b)
print("a x b is", a.toString())

# Testing ComplexPolar
c = ComplexPolar(10.0,pi/6.0)
d = ComplexPolar(10.0, pi/3.0)
print("c is",c.toString())
print("d is", d.toString())
c.add(d)
print("c=c+d is", c.toString())
c.minus(d)
print("c-d (which is the original c) is ", c.toString())
c.times(d)
print("c=c*d is", c.toString())

# Testing Combine
print("a is", a.toString())
print("d is", d.toString())
a.minus(d)
print("a=a-d is", a.toString()) 
a.times(d)
print("a=a*d is", a.toString())
d.add(a)
print("d=d+a is", d.toString())
d.times(a)
print("d=d*a is", d.toString()) 


