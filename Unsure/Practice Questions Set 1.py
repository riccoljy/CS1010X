##CS1010X 2017/2018 Prac Qns Set 1

##Question 1

#1a
def shift_one_left(num):
    return shift_left(num, 1)

#1b & c
#Neither recursive nor iterative
def shift_left(num, n):
    if n == 0:
        return num
    else:
        strnum = str(num)
        smallest_n = n%len(strnum)
        strnum = strnum[smallest_n:] + strnum[:smallest_n]
        return int(strnum)

#Iterative
def shift_left_iter(num, n):
    strnum = str(num)
    length = len(strnum)
    for i in range(n):
        strnum = strnum[1:] + strnum[0]
    return int(strnum)

#Recursive
def shift_left_rec(num, n):
    if n == 0:
        return num
    else:
        return shift_left_rec(int(str(num)[1:] + str(num)[0]), n-1)

##1d

#Neither recurisve nor iterative
def shift_right(num, n):
    return shift_left(num, -n)

#Iterative
def shift_right_iter(num, n):
    strnum = str(num)
    length = len(strnum)
    for i in range(n):
        strnum = strnum[-1] + strnum[:-1]
    return int(strnum)

#Recursive
def shift_right_rec(num, n):
    if n == 0:
        return num
    else:
        return shift_right_rec(int(str(num)[-1] + str(num)[:-1]), n-1)

##Question 2

def nth_digit(n, number):
    if n <= len(str(number)):
        return int(str(number)[-n])
    else:
        return None
def mth_digit(m, number):
    if m <= len(str(number)):
        return int(str(number)[m-1])
    else:
        return None

##Question 3

def divisible_by_11(num):
    sum_odd = sum_even = 0
    for i in range(len(str(num))):
        if i%2 == 0: #Looks like other way round but it's because str(num)[0] is 1st digit
            sum_odd += int(str(num)[i])
        else: #Likewise, str(num)[1] is 2nd digit
            sum_even += int(str(num)[i])
    diff = sum_odd - sum_even
    if diff%11 == 0:
        return True
    else:
        return False

    
##Odd and even position in number, NOT PARITY OF NUMBER
##def sum_of_odd_and_even(num):
##    odd = even = 0
##    strnum = str(num)
##    for digit in strnum:
##        if int(digit)%2==0:
##            even += int(digit)
##        else:
##            odd += int(digit)
##    return (odd, even)

##Question 4
def count_instance(num, seq):
    counter = 0
    for element in seq:
        if type(element) != tuple:
            if num == element:
                counter += 1
            else:
                continue
        else:
            counter += count_instance(num, element)
    return counter

##Question 5
def concat(n, m):
    return int(str(n)+str(m))

##Question 6
def replace_digit(n, d, r):
    strnum = str(n)
    for index in range(len(strnum)):
        if strnum[index] == str(d):
            strnum = strnum[:index] + str(r) + strnum[index+1:]
        else:
            continue
    return strnum

##Question 7

#Q2 Rec
def nth_digit_rec(n, num):
    
            
