def time_difference(time1, time2):
    seconds1 = time_to_seconds(time1)
    seconds2 = time_to_seconds(time2)
    diffsec = seconds2 - seconds1
    sec = diffsec%60
    diffmin = int(diffsec/60)
    minute = diffmin%60
    diffhour = int(diffmin/60)
    hour = diffhour%60
    return make_time_string(hour,minute,sec)
    
    
# Predefined helper functions. Do not edit them.
def time_to_seconds(time):
    x = list(map(int, time.split(":")))
    return x[0] * 3600 + x[1]*60 + x[2]

def make_time_string(hours, mins, seconds):
    return "{:02d}:{:02d}:{:02d}".format(hours, mins, seconds)
