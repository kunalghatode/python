'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "k" in x]

print(newlist)


newlist1=[]
for i in fruits:
	if "k" in i:
    	 newlist1.append(i)
print(newlist1)
        
'''











square=[x**2 for x in range(9,18) if x%2!=0]
print(square)

name=['kunal','prince']
p=[x*2 for x in name]
print(p)



l=[1,5,8,3,2,0]
l.sort()
print(l)

l.sort(reverse=True)
print(l)




cube=[x**3 for x in range(1,5) if x > 1]
print(cube)