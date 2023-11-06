import math

def taxi_fare(distance):
    diff1 = math.ceil((distance-1000)/400)
    diff2 = math.ceil((distance-10000)/350)
    if distance<=1000: print("$3.00")
    elif 1000<distance<=10000:
        fare = float(3.00 + diff1*0.22)
        print("$"+str(fare))
    else:
        fare = float(3.00 + math.ceil(9000/400)*0.22 + diff2*0.22)
        print("$"+str(fare))

taxi_fare(900)   
