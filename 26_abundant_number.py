# ABUNDANT Number

n = int(input('enter the number: '))
sum = 1
for i in range(2,n):
    if n % i == 0 :
        sum+= i
if sum > n :
    print("abundant number")
else:
    print('not abundant number')