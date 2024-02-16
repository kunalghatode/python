class kunnudon:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def printName(self):
  print(f"{self.name} {self.age}")

class johnthedon(kunnudon):
 def bark(self):
  print("John banega don")

j = johnthedon("john", 8)
k = kunnudon("kunal", 21)
j.bark()
j.printName()
k.printName()