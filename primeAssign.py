import math

x = input()

int_no=int(x)


is_prime =True
def check_if_prime(num):
    
    int_m = math.ceil(math.sqrt(num))
    
    if(num==2):
        return True
    
    elif(num == 1 | num==0):
        return False
    else:
        print("I'm inside else "+ str(int_m))
        for i in range(2,int_m):
            print("I'm here inside loop" +str(num%i))
            if(num % i ==0):
                is_prime=False
                print(str(num%i))
                print(str(is_prime))
                return False
            
                
    return True
            
                
        


prime_check =(bool(check_if_prime(int_no)))
print("After the function call "+str(is_prime) +str(prime_check))
if(is_prime & bool(prime_check)):
    print(str(x)+" is prime")
else:
    print(str(x)+ " is not prime")