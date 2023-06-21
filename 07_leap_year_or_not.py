num = int(input("enter the number of year:")) 
if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0 ):
  print("It is Leap year")
else :
    print("Its Not Leap Year...")

