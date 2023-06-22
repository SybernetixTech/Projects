def is_even(number:int):
    if number % 2 == 0:
        return True
    return False

def even_list(start:int,end:int):
    EVEN = [i for i in range(start,end+1) if is_even(i)]
    return EVEN
