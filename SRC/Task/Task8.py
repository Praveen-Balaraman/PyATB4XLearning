a=int(input("Enter the side a of the Triangle"))
b=int(input("Enter the side b of the Triangle"))
c=int(input("Enter the side c of the Triangle"))

if a==b==c:
    print("Triangle is a Equilateral")
elif a==b or a==c or b==c:
    print("Triangle is Isoceles")
else:
    print("Triangle is a scalene")