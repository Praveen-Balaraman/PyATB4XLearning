
i=1
while 0< i <=100:
    if i%3==0 and i%5!=0:
     print("Fizz")
    elif i%5==0 and i%3!=0:
     print("Buzz")
    elif i%5==0 and i%3==0:
     print("FizzBuzz")
    else:
      print(i)
    i += 1
