a = 5
try:
    raise NameError("HI kunal")    
except TypeError:
    print("Type error")

except:
    print("cant divide by zero")
    raise

else:
    print(b)
finally:
    print("It will always be exevuted")
