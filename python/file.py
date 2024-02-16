f = open("test.txt", "w")
f.write("This is a text file.\n")
f.write("Used for file Handling")
f.close()

# f = open("test.txt", "rt")
# print(f.readline())
# f.close()


f = open("test.txt", 'w')
f.write(" File has more content")
f.close()


f = open("test.txt", 'a')
f.write(" File has more content")
f.close()

f = open("test.txt", "rt")
print(f.read())
f.close()



#if you want to delete the file, you might need to check if the file
# exists before you try to delete 

import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("File does not exist")