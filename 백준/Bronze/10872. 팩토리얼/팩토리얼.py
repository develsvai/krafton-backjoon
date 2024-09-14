def factorial(n : int ) :
    if n ==  0 :
        return 1
    if(n == 1) : 
        return 1
    
    return n * factorial(n-1)



N = int(input())

print(factorial(N))
