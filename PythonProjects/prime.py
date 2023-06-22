import odd
def is_prime(number:int):
    val = False
    if number == 2:
        val = True
    elif odd.is_odd(number):
        if number == 1:val= False
        for i in range(3,number):
            if odd.is_odd(i):
                if number % i == 0:
                    val = False 
                    break
                val = True
    return val

def prime_list(start:int,end:int):
    PRIME = [i for i in range(start,end+1) if is_prime(i)]        
    return PRIME

 
primes = prime_list(1,100)  

print(len(primes)) 