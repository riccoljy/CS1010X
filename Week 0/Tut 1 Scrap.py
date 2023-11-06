def is_leap_year(year):
    if year%4==0 and (year/4)%25!=0:
        return True
    elif year%4==0 and (year/4)%100==0:
        return True
    else: return False
