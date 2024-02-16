class kunnudon:
 def __init__(self, name, age):
  self.name = name
  self.age = age

 def __str__(self):
  return f"{self.name}, {self.age}"
 
 def kunal(self):
  pass

k = kunnudon("kunal", 21)
p = kunnudon("prince", 29)
p.age = 10
del p
# print(k)
k.kunal()
# print(p)
# print(k.name)
# print(k.age)
# print(p.name)
# print(p.age)


