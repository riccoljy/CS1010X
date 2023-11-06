##CS1010X Tutorial 3, 18/1/2023, Ricco Lim


##Question 1
#Pre-given functions:

def biggie_size(small_size):
    if 1 <= small_size <= 4:
        return small_size + 4
    else: return "not valid"

def unbiggie_size(big_size):
    if 5 <= big_size <= 8:
        return big_size - 4
    else: return "not valid"

def is_biggie_size(combo_option):
    if 5 <= combo_option <= 8:
        return True
    else: return False

def combo_price(combo_option):
    patty_price = 1.17
    biggie_size_charge = 0.5
    if combo_option < 1 or combo_option > 8:
        return "not valid"
    elif is_biggie_size(combo_option) == False:
        num_of_patty = combo_option
        return num_of_patty * patty_price
    else:
        num_of_patty = unbiggie_size(combo_option)
        return num_of_patty * patty_price + biggie_size_charge

def empty_order():
    return 0

def add_to_order(order, combo):
    return order*10 + combo

##Question 1(a)

##WRONG! NOT RECURSIVVE!
def order_size(order):
    return len(str(order))

def order_size(order):
    if order == empty_order():
        return 0
    else:
        return 1 + order_size(order//10)

##Question 1(b)
def order_size(order):
    count = 0
    for i in range(len(str(order))):
           count += 1
    return count

##Question 1(c)
def order_cost(order):
    
    if order <= 0:
        return "not valid"
    elif order_size(order) == 1:
        return combo_price(order)
    else:
        last_digit = int(str(order)[-1]) ##FIND LAST DIGIT IN ORDER
        new_order = int((order - int(str(order)[-1]))/10) ##Minus out the last digit behind
        cost = combo_price(last_digit) + order_cost(new_order) ##COST = Price of last digit/order + Price of remaining new_order
        return cost

##Question 1(d)
def order_cost(order):
    if order <= 0:
        return "not valid"
    else:
        cost = 0
        for i in str(order):
            cost += combo_price(int(i))
        return cost
        
##Question 1(e)
def add_orders(order1, order2):
    return order1 * 10**(order_size(order2)) + order2

##Question 2
##(a) O(n^2)

# Working:
# 5n^2 + n < 5n^2 + n^2 for n>1
#           = 6n^2 for n>1
#           = O(n^2) for k=6, n_0 = n naught > 1


##(b)
#WRONG
#O(sqrt(n)) = O(n^0.5)

# sqrt(n) + n < n + n for n>1
#               = 2n for n>1
#               = O(n) for k=2, n_0 > 1


##(c) O(3^n*n^2)

##Question 3
#WRONG
##Time: O(n)
#Time actually O(1)

##Space: O(n)

##Question 4
def fact(n):
    if n == 0: return 1
    else:
        count = 1
        for i in range(1, n+1):
            count = count*i
        return count


#Not in qns but
#Time: O(n)
#Space actually O(2) = O(1) for iterative bc no deferred operations/no creating of "new variables"

##Question 5
#WRONG
##Time: O(n)
#Time actually O(n^2)

    
##Space: O(n) with iterative fact function


##Question 6

def is_divisible(n, x):
    if n%x == 0: return True
    else: return False
##Assuming given the function above, BUT Time: O(n), Space: O(1) instead
   
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if is_divisible(n, i) == True:
                return False
            else: continue
        return True

##Time: O(n) * O(n) = O(n^2)
##Space: O(1)

##Question 7
def find_e(n):
    e = 1
    for i in range(1, n+1):
        e += 1/fact(i)
    return e
