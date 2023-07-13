# PERFECT SQUARE

num = int(input('Enter the number: '))
flag = 0

for i in range(1,num):
    if i * i == num :
        flag = 1
        break

if flag == 1 :
    print('it\'s a perfect square')
else:
    print('not a perfect square')
