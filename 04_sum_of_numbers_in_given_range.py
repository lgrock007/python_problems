sum = 0
num1 = int(input("Enter the Number:"))
num2 = int(input("Enter the Number:"))
"""
if num1<0 and num2<0:
    print("Enter the Positive Number.")
elif num1==0 and num2==0:
    print("You have entered the number is zero.")
else:
"""
for i in range(num1,num2+1):
    sum = sum + i
print("The number is range between %d and %d are ,%d ."%(num1,num2,sum))