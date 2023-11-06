# CS1010S --- Programming Methodology
#
# Mission 7 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import datetime
import csv

###############
# Pre-defined #
###############

def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

###############
# Station ADT #
###############

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


############
## Task 1 ##
############

def make_train(train_code):
    ''' Do NOT modify this function'''
    return (train_code,)

test_train = make_train('TRAIN 0-0')

#############
# Task 1a   #
#############

def get_train_code(train):
    return train[0]

##UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
print("## Task 1a ##")
print(get_train_code(test_train))

# Expected Output #
# TRAIN 0-0

#############
# Task 1b   #
#############

def make_line(name, stations):
    return (name, stations)

def get_line_name(line):
    return line[0]

def get_line_stations(line):
    return line[1]

def get_station_by_name(line, station_name):
    for station in get_line_stations(line):
        if station_name in station:
            return station
        else:
            continue
    return None

def get_station_by_code(line, station_code):
    for station in get_line_stations(line):
        if station_code in station:
            return station
        else:
            continue
    return None

def get_station_position(line, station_code):
    if get_station_by_code(line, station_code) == None:
        return -1
    else:
        correct_station = get_station_by_code(line, station_code)
        return get_line_stations(line).index(correct_station)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
print("## Task 1b ##")
test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))
print(get_line_name(test_line))
print(get_line_stations(test_line))
print(get_station_by_name(test_line, 'Bras Basah'))
print(get_station_by_code(test_line, 'CC4'))

# Expected Output #
# Circle Line
# (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade'))
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')

#############
# Task 1c   #
#############

def make_train_position(is_moving, from_station, to_station):
    ''' Do NOT modify this function'''
    return (is_moving, from_station, to_station)

def get_is_moving(train_position):
    return train_position[0]

def get_direction(line, train_position):
    FromStationPosition = get_station_position(line, get_station_code(train_position[1]))
    ToStationPosition = get_station_position(line, get_station_code(train_position[2]))
    if ToStationPosition > FromStationPosition:
        return 0
    else:
        return 1
#Alternative get_direction using dictionary order (similar to using running integers,
#which is not recommended):
##def get_direction(line, train_position):
##    if train_position[2] > train_position[1]:
##        return 0
##    else:
##        return 1

def get_stopped_station(train_position):
    if get_is_moving(train_position) == True:  #if train is not stationary
        return None
    else: #if train is stationary
        return train_position[1]
        

def get_previous_station(train_position):
    if get_is_moving(train_position) == False: #if train is not moving
        return None
    else: #if train is moving
        return train_position[1]

def get_next_station(train_position):
    return train_position[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
print("## Task 1c ##")
test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)
print(get_is_moving(test_train_position2))
print(get_direction(test_line, test_train_position1))
print(get_stopped_station(test_train_position1))
print(get_previous_station(test_train_position2))
print(get_next_station(test_train_position2))

# Expected Output #
# True
# 0
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')
# ('CC3', 'Esplanade')

#############
# Task 1d   #
#############

def make_schedule_event(train, train_position, time):
    return (train, train_position, time)

def get_train(schedule_event):
    return schedule_event[0]

def get_train_position(schedule_event):
    return schedule_event[1]

def get_schedule_time(schedule_event):
    return schedule_event[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1D
print("## Task 1d ##")
test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))
print(get_train(test_bd_event1))
print(get_train_position(test_bd_event1))
print(get_schedule_time(test_bd_event1))

# Expected Output #
# ('TRAIN 0-0',)
# (True, ('CC4', 'Promenade'), ('CC3', 'Esplanade'))
# 2016-01-01 09:27:00


############
## Task 2 ##
############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

#############
# Task 2a   #
#############

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            current_station = make_station(code, station_name)
            curr_line_stations += current_station,
        else: #if line_name != curr_line_name (ie: next line already)
            prev_line = make_line(curr_line_name, curr_line_stations) #collate prev line
            lines += prev_line, #add prev line to lines (output)
            curr_line_name = row[2] #new line new name!
            #same as before,
            current_station = make_station(code, station_name)
            curr_line_stations = current_station, #= instead of += since new line
    last_line = make_line(curr_line_name, curr_line_stations)
    lines += last_line,
    return lines

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A. THIS IS NOT OPTIONAL TESTING!
LINES = parse_lines('station_info.csv')
CCL = filter(lambda line: get_line_name(line) == 'Circle Line', LINES)[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
print("## Task 2a ##")
print(get_line_stations(CCL)[5:8])

# Expected Output #
# (('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota'))

#############
# Task 2b   #
#############

def parse_events_in_line(data_file, line):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        train = make_train(row[0])
        trainposition = make_train_position(True if row[1]=="True" else False,
                                            get_station_by_code(line, row[2]),
                                            get_station_by_code(line, row[3]))

        ##Date in csv file given in format "DD/MM/YYYY"
        stringdate = row[4]
        year = int(stringdate[-4:])
        day = int(stringdate[:2])
        month = int(stringdate[3:5])

        ##Time in csv file given in format "HH:MM"
        stringtime = row[5]
        hour = int(stringtime[:2])
        minute = int(stringtime[-2:])
        
        time = datetime.datetime(year, month, day, hour, minute)

        events += make_schedule_event(train, trainposition, time),
    return events

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2B. THIS IS NOT OPTIONAL TESTING!
BD_EVENTS = parse_events_in_line('breakdown_events.csv', CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
print("## Task 2b ##")
print(BD_EVENTS[9])

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 3 ##
############

#############
# Task 3a   #
#############

def is_valid_event_in_line(bd_event, line):
    trainposition = get_train_position(bd_event)
    up0down1 = get_direction(line, trainposition) #if returns 0, gg up. if returns 1 gg down
    fromstation = get_stopped_station(trainposition) if get_is_moving(trainposition) == False else get_previous_station(trainposition)
    #alternative simpler but without getter:
    # fromstation = trainposition[1]
    tostation = get_next_station(trainposition)

    FROMposition = get_station_position(line, fromstation[0])
    TOposition = get_station_position(line, tostation[0]) #index 0 bc just want code, not name
    distance = abs(FROMposition - TOposition)

    time = get_schedule_time(bd_event)
    hour = time.hour
    minute = time.minute


    if distance == 1 and (7 <= hour <= 22 or (hour == 23 and minute == 0)):
        return True
    else:
        return False

def get_valid_events_in_line(bd_events, line):
    ''' Do NOT modify this function'''
    return filter(lambda ev: is_valid_event_in_line(ev, line), bd_events)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 3A. THIS IS NOT OPTIONAL TESTING!
VALID_BD_EVENTS = get_valid_events_in_line(BD_EVENTS, CCL)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
print("## Task 3a ##")
print(is_valid_event_in_line(test_bd_event1, CCL))
print(is_valid_event_in_line(test_bd_event2, CCL))

# Expected Output #
# True
# False

#############
# Task 3b   #
#############

def get_location_id_in_line(bd_event, line):
    trainposition = get_train_position(bd_event)
    if get_is_moving(trainposition) == True:
        fromstationposition = get_station_position(line, get_previous_station(trainposition)[0]) #index [0] because just want stn code
        tostationposition = get_station_position(line, get_next_station(trainposition)[0])
        return min((fromstationposition, tostationposition)) + 0.5
    else: #if not moving
        return get_station_position(line, get_stopped_station(trainposition)[0]) 

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
print("## Task 3b ##")
test_loc_id1 = get_location_id_in_line(test_bd_event1, CCL)
test_loc_id2 = get_location_id_in_line(test_bd_event2, CCL)
print(test_loc_id1)
print(test_loc_id2)

# Expected Output #
# 2.5
# 1

############
## Task 4 ##
############

# UNCOMMENT the following to read the entire train schedule
FULL_SCHEDULE = parse_events_in_line('train_schedule.csv', CCL)    # this will take some time to run

#############
# Task 4a   #
#############

def get_schedules_at_time(train_schedule, time):
    output = ()
    for event in train_schedule:
        if get_schedule_time(event) == time:
            output += event,
        else: #may be wrong format, like in csv file
            ##Date in csv file given in "MM/DD/YYYY" format
            ##Will need to find way to adopt to any date format
            timewrongformat = str(get_schedule_time(event))
            year = int(timewrongformat[:4])
            day = int(timewrongformat[5:7])
            month = int(timewrongformat[8:10])
            hour = int(timewrongformat[11:13])
            minute = int(timewrongformat[14:16])
            seconds = int(timewrongformat[-2:])
            
            timerightformat = datetime.datetime(year, month, day, hour, minute, seconds)
            if timerightformat == time:
                output += event,
            else:
                continue
    return output

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
print("## Task 4a ##")
test_datetime = datetime.datetime(2017, 1, 6, 6, 0)
test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)
print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))

#############
# Task 4b   #
#############

def get_schedules_near_loc_id_in_line(train_schedule, line, loc_id):
    output = ()
    for schedule in train_schedule:
        ##since function should return a tuple of ScheduleEvents whose positions are a maximum of 0.5 away from the given position,
        if (loc_id - 0.5) <= get_location_id_in_line(schedule, line) <= (loc_id + 0.5):
            output += schedule,
    return output

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4B
print("## Task 4b ##")
test_schedules_near_loc_id = get_schedules_near_loc_id_in_line(FULL_SCHEDULE[:10], CCL, test_loc_id1)
print(test_schedules_near_loc_id[1])

# Expected Output #
# (('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))

#############
# Task 4c   #
#############

def get_rogue_schedules_in_line(train_schedule, line, time, loc_id):
    schedule_events_at__right_time = get_schedules_at_time(train_schedule, time)
    schedule_events_at_time_and_position = get_schedules_near_loc_id_in_line(schedule_events_at__right_time, line, loc_id)
    return schedule_events_at_time_and_position

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4C
print("## Task 4c ##")
test_bd_event3 = VALID_BD_EVENTS[0]
test_loc_id3 = get_location_id_in_line(test_bd_event3, CCL)
test_datetime3 = get_schedule_time(test_bd_event3)
test_rogue_schedules = get_rogue_schedules_in_line(FULL_SCHEDULE[1000:1100], CCL, test_datetime3, test_loc_id3)
print(test_rogue_schedules[2])

# Expected Output #
# (('TRAIN 1-11',), (True, ('CC24', 'Kent Ridge'), ('CC23', 'one-north')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 5 ##
############

###############
# Scorer ADT  #
###############

def make_scorer():
    return {}

def blame_train(scorer, train_code):
    scorer[train_code] = scorer.get(train_code, 0) + 1
    return scorer

def get_blame_scores(scorer):
    return tuple(scorer.items())

# Use this to keep track of each train's blame score.
SCORER = make_scorer()

#############
# Task 5a   #
#############

def calculate_blame_in_line(full_schedule, valid_bd_events, line, scorer):
    for bd_event in valid_bd_events:
        curr_bd_event_locationID = get_location_id_in_line(bd_event, line)
        curr_bd_event_time = get_schedule_time(bd_event)
        schedules_to_blame = get_rogue_schedules_in_line(full_schedule, line, curr_bd_event_time, curr_bd_event_locationID)
        trains_to_blame = ()
        for each_schedule in schedules_to_blame:
            curr_train = get_train(each_schedule)[0]
            if curr_train not in trains_to_blame:
                trains_to_blame += curr_train,
            else: #train already going to be blamed for that event
                continue
        for train in trains_to_blame:
            blame_train(scorer, train)
    return scorer

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 5A. THIS IS NOT OPTIONAL TESTING!
calculate_blame_in_line(FULL_SCHEDULE, VALID_BD_EVENTS, CCL, SCORER)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5A
print("## Task 5a ##")
print(sorted(get_blame_scores(SCORER))[7])

# Expected Answer
# ('TRAIN 0-5', 2)

#############
# Task 5b   #
#############

def find_max_score(scorer):
    tuple_of_scores = map(lambda x: x[1], get_blame_scores(scorer))
    return max(tuple_of_scores)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5B
print("## Task 5b ##")
test_max_score = find_max_score(SCORER)
print(test_max_score)

# Expected answer
# 180

#############
# Task 5c   #
#############

# UNCOMMENT THE CODE BELOW TO VIEW ALL BLAME SCORES. THIS IS NOT OPTIONAL TESTING!
print("## Task 5c ##")
train_scores = get_blame_scores(SCORER)
print("############### Candidate rogue trains ###############")
for score in train_scores:
 print("%s: %d" % (score[0], score[1]))
print("######################################################")

''' Please type your answer into the Task 5c textbox on Coursemology '''

"""
Yes, I believe that hypothesis still holds because of the outlier TRAIN 0-4 which has a
blame_score of 180, as compared to the much lower blame_score the other trains have which
are all below 20. This one train has been blamed so many times in so many valid breakdown
events that it has reached a blame_score more than 9 times that of the highest blame_score
in the other trains.

"""

#############
# Task 5d   #
#############

def find_rogue_train(scorer, max_score):
    for train_and_score in get_blame_scores(scorer):
        if max_score in train_and_score:
            return train_and_score[0]
        else:
            continue

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5D
print("## Task 5d ##")
print("Rogue Train is '%s'" % find_rogue_train(SCORER, test_max_score))

# Expected Answer
# Rogue Train is 'TRAIN 0-4'
