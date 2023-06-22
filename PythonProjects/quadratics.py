
def validate(a,b,c):
    try:
        a, b, c = float(a),float(b),float(c)
        print(type(a))
    except:pass
    
    
    if type(a) is float and float(b) is float and type(c) is float:return True
    else:return False


a = input('Enter a: ')
b = input('Enter b: ')
c = input('Enter c: ')

k = (validate(a,b,c))

print(k)

if validate(a,b,c):
     pass
else:
    print('The values Provided is neither floatr nor int')
    