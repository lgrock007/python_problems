
num_1 = int(input('Enter the Number:'))
num_2 = int(input('Enter the Number:'))

sum_1 = 0
sum_2 = 0
for i in range(1,num_1):
    if num_1 % i == 0 :
        sum_1 += i

for i in range(1,num_2):
    if num_2 % i == 0 :
        sum_2 += i
        
if (sum_1 / num_1) and (sum_2 == num_2) :
    print('Friendly Pair')
else:
    print('Non Friendly Pair')
    
