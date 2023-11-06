
##Recursive
def f(n):
    if n < 3:
        return n
    else:
        return f(n-1) + 2 * f(n-2) + 3 * f(n-3)

##Iterative; using counter?
def f(n):
    if n < 3:
        return n
    else:
        f0, f1, f2 = 0, 1, 2
        x, y, z = 0, 0, 0 #x, y, z = number of f0s, f1s, and f2s
        #f(3) = f(2) + 2f(1) + 3f(0) => x, y, z = 1, 2, 3
        #f(4) = f(3) +                  2f(2) + 3f(1)
        #     = f(2) + 2f(1) + 3f(0) +  2f(2) + 3f(1)
        #     = 3f(2) + 5f(1) + 3f(0) => x, y, z = 3, 5, 3
        #f(5) = f(4) + 2f(3) + 3f(2)
        
        while n >= 3:
            
            n -= 1
        sum = x*f0 + y*f1 + z*f2
        return sum


##def legendre(n):
##    #test 1^2, (1+1)^2 for prime, then
##    #test 2^2, (2+1)^2 for prime, then repeat until n^2, (n+1)^2
##    for i in range(1, n+1):
##        for value in range(i**2, (i+1)**2+1):
##            #print ("i=",i," value=", value)
##            if check_prime(value) == False: continue
##            elif value == (i+1)**2: return False #if reach the end of range and no prime, return False
##            else: 
##                break #continue to next range 2^2 3^2, etc.
##    return True #executed only if all ranges has at least one prime
##            
##            
##def check_prime(n):
##    if n < 2: return False
##    elif n == 2: return True
##    else:
##        i = 2
##        while i < n:
##            if n % i == 0:
##                return False
##            else:
##                i += 1
##        return True

def legendre_n(n):
    """Returns the number of primes between n**2 and (n+1)**2"""
    number_of_primes = 0
    for value in range(n**2, (n+1)**2+1):
        if check_prime(value) == True: number_of_primes += 1
        else: pass
    return number_of_primes


def check_prime(n):
    if n < 2: return False
    elif n == 2: return True
    else:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            else:
                i += 1
        return True


legendre_n(1)
legendre_n(2)
legendre_n(3)
legendre_n(12)
