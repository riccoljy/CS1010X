from math import *

def taxi_fare(distance):
    base_fare = 3.00
    ten_km_price = base_fare + ceil(9000/400) * 0.22
    if distance<= 1000:
        return base_fare
    elif 1000<distance<=10_000:
        return base_fare + ceil((distance-1000)/400) * 0.22
    else:
        #can do recursive; return taxi_fare(1000) + 
        return ten_km_price +\
               ceil((distance-10_000)/350) * 0.22
    

    
def fibbon(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbon(n-1) + fibbon(n-2)


    
