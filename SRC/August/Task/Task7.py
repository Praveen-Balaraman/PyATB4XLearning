year = int(input("Enter the Year"))

if (year % 4) != 0:
  print("The year is not leap")
elif year%4==0 and year%100!=0:
  print("The year is leap")
elif year%400==0 and year%100==0:
  print("The year is leap")
else:
  print("The year is not a leap")
