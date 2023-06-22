def is_odd(Number:int):
    if Number % 2 == 0:
        return False
    return True

def odd_list(start:int,end:int):
    ODDS = [i for i in range(start,end+1) if is_odd(i)]
    return ODDS
