##CS1010X       Recitation 4        21 Feb 2023         Ricco Lim

##Question 1

tup_a = (10, 12, 13, 14) # Creating tup_a
#print(tup_a) will print the tuple (10, 12, 13, 14)


tup_b = ("CS1010X", "CS1231") # Creating tup_b
#print(tup_b) will print the tuple ('CS1010X', 'CS1231')


tup_c = tup_a + tup_b # Creating tup_c
#print(tup_c) will print (10, 12, 13, 14, 'CS1010X', 'CS1231')

#len(tup_c) will return 6
#14 in tup_a will return True
#11 in tup_c will return False

tup_d = tup_b[0]*4
#tup_d will return 'CS1010XCS1010XCS1010XCS1010X'

#tup_d[0] will return 'C'
#tup_d[1:] will return 'S1010XCS1010XCS1010XCS1010X'

count = 0
for i in tup_a:
    count = count + i
#print(count) will return 49 since count += i, where i will iterate through tup_a = (10, 12, 13, 14)

#max(tup_a) will return 14, the greatest value in tup_a
    
#min(tup_a) will return 10, the smallest value in tup_a
#max(tup_c) & min(tup_c) will return a TypeError since int and str cannot be comapared

##Question 2
tup_1 = (1, 2, 3)

#(1, (2), 3) is not possible as a single element tuple requires a comma after the element to indicate that it is a tuple.
print( "(1, (2), 3)" )

tup_3 = (1, (2,), 3)

tup_4 = ((1, 2), (3, 4), (5, 6))


##Question 3
    
x = (7, 6, 5, 4, 3, 2, 1)
#x[3] and x[-4] will both return 4

x = (7, (6, 5, 4), (3, 2), 1)
#x[1][2], x[1][-1], x[-3][-1], and x[-3][2] will all return 4

x = (7, ((6, 5, (4,), 3), 2), 1)
#x[1][0][2][0] is one possibility.

##Question 4

#Given functions:

def make_module(course_code, units):
    return (course_code, units)

def make_units(lecture, tutorial, lab, homework, prep):
    return (lecture, tutorial, lab, homework, prep)

def get_module_code(course):
    return course[0]

def get_module_units(course):
    return course[1]

def get_module_total_units(units):
    return units[0] + units[1] + units[2] + units[3] + units[4]

#4(a)
def make_empty_schedule():
    return ()
#O(1) for both time & space

#4(b)
def add_class(course, schedule):
    schedule += course,
    return schedule
#O(1) for both time & space

#4(c)
def total_scheduled_units(schedule):
    result = 0
    for course in schedule:
        units = get_module_units(course)
        result += get_module_total_units(units)
    return result
#O(n) for both time & space

#4(d)
def drop_class(schedule, course):
    new_schedule = ()
    for mod in schedule:
        if mod != course:
            new_schedule += mod
    return new_schedule
#O(n) for both time & space

#4(e)
def credit_limit(schedule, max_credits):
    if total_scheduled_units(schedule) <= max_credits:
        return schedule
    else:
##        credits_to_drop = total_scheduled_units(schedule) - max_credits
##        highest_credit = 0
##        mod_to_remove = ()
##        for course in schedule:
##            units = get_module_units(course)
##            total_units = get_module_total_units(units)
##            if (total_units <= credits_to_drop) and \
##               (total_units > highest_credit):
##                highest_credits = total_units
##                mod_to_remove = course
##            else:
##                continue
##        if mod_to_remove != ():
##            drop_class(schedule, mod_to_remove)
##            return schedule
##        else: #if after iterating and all mods' MCs very high, so just need to remove one
##            drop_class(schedule, schedule[0]) #arbitrary; can take any out since all greater than

        while total_scheduled_units(schedule) > max_credits:
            drop_class(schedule, schedule[0])
        return schedule

#Best case: O(1) for both (if statement)
#Worst case: O(n) for time, O(1) for space

#4(f)


            
            
