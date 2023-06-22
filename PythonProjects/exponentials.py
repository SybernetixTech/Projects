def powers(number:int,power: float):
    if type(number) is str:result = 'The base should be a number'
    else:
        if power == 0:result = 1
        elif power < 0:result = f'1/{number ** abs(power)}'
        else:result = number ** power
    return result



    