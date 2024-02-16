

#We have to use single star(*) to unpack the elements in list
def fun(a, b, c):
    print(a, b, c)
l = [1, 2, 3]
fun(*l)    


#We have to use double star(**) to unpack the elements in dictionary
d = {"b" : "kunal", "a" : 1, 'c' : True}
fun(**d)