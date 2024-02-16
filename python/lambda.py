
x = lambda x, y : x * y
#print(x(6, 5))


#The power of lambda is better shown when you use them as an 
#anonymous function inside another function.


#We can double the number or triple the number by using lambda
def fun(n):
    return lambda x : x * n
doubler = fun(2)

print(doubler)

#tripler = fun(3)
#print(tripler(33))