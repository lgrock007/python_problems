# HARSHAD NUMBER
n = int(input('Enter the number: '))
num = str(n)
sum = 0
for i in num :
    sum += int(i)
    
if n % sum == 0 :
    print("it's a Harshad Number")
else:
    print('not a harshad number')