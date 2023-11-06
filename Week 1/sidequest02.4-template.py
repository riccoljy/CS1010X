#
# CS1010X --- Programming Methodology
#
# Mission 2 - Side Quest 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

##########
# Task 1 #
##########

# Simplifed Order notations:

# 4^n * n^2
# Ans: 4^n * n^2

# n * 3^n
# Ans: n * 3^n

# 1000000000n^2
# Ans: n^2

# 2^n/1000000000
# Ans: 2^n

# n^n + n^2 + 1
# Ans: n^n

# 4^n + 2^n
# Ans: 4^n

# 1^n
# Ans: 1

# n^2
# Ans: n^2

# Faster order of growth in each group:

# i. 4^n * n^2
# ii. 2^n/1000000000 (simplified to 2^n)
# iii. n^n + n^2 + 1 (simplified to n^n)
# iv. n^2


##########
# Task 2 #
##########

# Time complexity: O(n)
# Space complexity: O(n)


##########
# Task 3 #
##########

# Time complexity of bar: O(n)
# Time complexity of foo: O(n^2)

# Space complexity of bar: O(n)
# Space complexity of foo: O(2n) = O(n)

def improved_foo(n):
    ##bar(n) is just n + (n-1) + (n-2) + ... + 2 + 1 + 0
    ##foo(n) is bar(n) + foo(n-1), where foo(0) = 0
    
##    if n == 0:
##        return 0
##    else:
##ABOVE 3 REDUNDANT NOW THAT NOT USING RECCURSIVE
    
    bar_n = 0
    temp_val = 0
    for i in range(n+1):
        bar_n += i
        temp_val += bar_n
    return temp_val

# Improved time complexity: O(n)
# Improved space complexity: O(1)
