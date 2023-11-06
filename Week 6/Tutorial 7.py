##CS1010X      Tutorial 7       22 Feb 2023         Ricco Lim

##Question 1

def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))

def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else:
        return ([accumulate(op, init, [x[0] for x in sequences])]
                + accumulate_n(op, init, [x[1:] for x in sequences]))
    
s = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
##print(accumulate_n(lambda x,y:x+y, 0, s))
#ie:    T1 = [x[0] for x in sequences] or list(map(lambda x: x[0], sequences))
#       T2 = [x[1:] for x in sequences] or list(map(lambda x: x[1:], sequences))

##Question 2
#2(a)
def col_sum(matrix):
    return accumulate_n(lambda x, y: x+y, 0, matrix)

m = [[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]
##print(col_sum(m))

#2(b)
def row_sum(matrix):
    
    def transpose(matrix):
        num_of_row = len(matrix)
        num_of_col = len(matrix[0])
        for index in range(num_of_col):
            matrix.append([matrix[0][index]])
        matrix.pop(0)
        while num_of_row > 1:
            for index in range(num_of_col):
                matrix[num_of_row - 1 + index].append(matrix[0][index])
            matrix.pop(0)
            num_of_row -= 1
        return matrix

    return col_sum(transpose(matrix))

##print(row_sum(m))


##Question 3
#3(a)

def count_sentence(sentence):
    num_of_words = len(sentence)
    num_of_letters = num_of_words - 1 #num of spaces
    for word in sentence:
        for letter in word:
            num_of_letters += 1
    return [num_of_words, num_of_letters]

#Order of growth in time:   O(n)
#Order of growth in space:  O(n)

##print(count_sentence([[ 'C', 'S', '1', '0', '1', '0', 'S'] , ['R', 'o', 'c', 'k', 's']]))
##print(count_sentence([[ 'P', 'y', 't', 'h', 'o', 'n'] , ['i', 's'] , ['c', 'o', 'o', 'l']]))
##print(count_sentence([[ 'I'] , ['l', 'i', 'k', 'e'] , ['p', 'i', 'e']]))

#3(b)
def letter_count(sentence):
    counter = {}
    for word in sentence:
        for letter in word:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1

    result = []
    for key, val in counter.items():
        result.append([key, val])
    return result

#Order of growth in time:   O(2n) = O(n)
#Order of growth in space:  O(n)

##print(letter_count ([[ 's', 'h', 'e'] , ['l', 'i', 'k', 'e', 's'] , ['p', 'i', 'e', 's']]))

#3(c)
def most_frequent_letters(sentence):
    if sentence == []:
        return []
    else:
        lettercount = letter_count(sentence)
        highest_count = lettercount[0][1]
        result = [lettercount[0][0]]
        for letter_and_num in lettercount[1:]:
            letter = letter_and_num[0]
            count = letter_and_num[1]
            if count > highest_count:
                result = [letter]
                highest_count = count
            elif count == highest_count:
                result.append(letter)
            else:
                continue
        return result

#Order of growth in time:   O(3n) = O(n)
#Order of growth in space:  O(n)

##most_frequent_letters ([[ 's', 'h', 'e'] , ['l', 'i', 'k', 'e', 's'] , ['p', 'i', 'e', 's']])


##Question 4

def make_queue():
    return []

def enqueue(q, item):
    q.append(item)

def dequeue(q):
    return q.pop(0)

def size(q):
    return len(q)

q = make_queue()
enqueue(q, 1)
enqueue(q, 5)
##print(q)
##print(size(q))
##print(dequeue(q))

##Question 5

def who_wins(m, list_of_players):
    while len(list_of_players) > m:
        list_of_players.pop(m)
        list_of_players = list_of_players[m:] + list_of_players[:m]
    list_of_players.pop(0)
    return list_of_players


