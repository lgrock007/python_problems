# PERFECT NUMBER

num = int(input('enter the number:'))
sum = 0
for i in range(1,num):
    if num % i == 0 :
        sum += i

if sum == num :
    print(f'{num} is a perfect number')
else:
    print('it\'s not a perfect number')