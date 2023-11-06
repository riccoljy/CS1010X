#Recitation 10      Ricco Lim       11 May 2023

table = {}
def count_change(amount, kind_of_coins):
    coins = (1, 5, 10, 20, 50)
    if (amount, kind_of_coins) in table:
        return table[(amount, kind_of_coins)]
    elif amount == 0:
        table[(amount, kind_of_coins)] = 1
    elif amount < 0 or kind_of_coins <= 0:
        table[(amount, kind_of_coins)] = 0
    else:
        table[(amount, kind_of_coins)] = count_change(amount-coins[kind_of_coins-1], kind_of_coins) + count_change(amount, kind_of_coins-1)
    return table[(amount, kind_of_coins)]

def dp_count_change(amount, kind_of_coins):
    coins = (1, 5, 10, 20, 50)
    table = []
    
    #amount < 0 or kind_of_coins <= 0
    first_row = [0] * (kind_of_coins+1) #+1 because accounting for 0 coins.
    for i in range(amount+1):
        table.append(list(first_row)) #use list(first_row) or first_row.copy() so that list's inner lists all doesnt point to first_row

    for i in range(1, kind_of_coins+1):
        table[0][i] = 1
    for col in range(1, kind_of_coins+1):
        for row in range(1, amount+1):
            if (row - coins[col-1]) < 0: ans1 = 0
            else: ans1 = table[row-coins[col-1]][col]
            table[row][col] = ans1 + table[row][col-1]

    return table[amount][kind_of_coins]
        

prices = {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20, 9: 24, 10: 30}


##def cut_rod(n, prices):
##    def helper(n):
##        potential = []
##        for x in range(1, n):
##            y = n-x
##            #print(f"x = {x} and y = {y}")
##            price = prices[x] + prices[y]
##            potential.extend(helper(x))
##            potential.extend(helper(y))
##            potential.append(price)
##        potential.append(prices[n])
##        return potential
##    return max(helper(n))

def cut_rod(n, prices):
    if n <= 0:
        return 0
    max_price = 0
    for p in prices:
        if p <= n:
            max_price = max(max_price, prices[p] + cut_rod(n-p, prices))
    return max_price


memorod = {}
def memo_cut_rod(n, prices):
    if n in memorod:
        return memorod[n]
    if n <= 0:
        memorod[n] = 0
        
    max_price = 0
    for p in prices:
        if p <= n:
            max_price = max(max_price, prices[p] + memo_cut_rod(n-p, prices))
    memorod[n] = max_price
    return memorod[n]

def dp_cut_rod(n, prices):
    max_price = [0] * (n+1)
    for length in range(1, n+1):    
        for p in prices:
            if p <= length:
                max_price[length] = max(max_price[length], prices[p] + max_price[length-p])
    return max_price[n]

def dp2_cut_rod(n, prices):
    max_price = []
    row = [0] * (len(prices)+1)
    for i in range(n+1):
        max_price.append(row.copy())

    for length in range(1, n+1):    
        for p in range(1, len(prices)+1):
            if p <= length:
                max_price[length][p] = max(max_price[length][p-1], prices[p] + max_price[length-p][p])
            else:
                max_price[length][p] = max_price[length][p-1]
    #print(max_price)
    return max_price[n][len(prices)]

def are_anagrams(string1, string2):
    return sorted(string1) == sorted(string2)
def has_anagrams(lst_of_strings):
    for i in range(len(lst_of_strings)-1):
        for j in range(i+1, len(lst_of_strings)):
            if are_anagrams(lst_of_strings[i], lst_of_strings[j]):
                return True
    return False
    
def find_anagrams(lst):
    res = []
    if not has_anagrams(lst): return res
    
    for i in range(len(lst)-1):
        str1 = lst[i]
        sub = [str1]
        for j in range(i+1, len(lst)):
            str2 = lst[j]
            if are_anagrams(str1, str2):
                sub.append(str2)
        sub.sort()
        if len(sub) > 1 and sub not in res:
            res.append(sub)
    return res
