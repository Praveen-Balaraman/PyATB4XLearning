
f=open("demo.txt","r")
print(f.read())
f.close()
f=open("demo.txt","a")
f.write("\n Im fine")

f.close()
f=open("demo.txt","r")
print(f.read())