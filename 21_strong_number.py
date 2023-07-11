# STRONG NUMBER

num = int(input('Enter the number: '))
temp = num
sum = 0
while num > 0 :
    rem = num % 10
    print('reminder:',rem)
    fact = 1
    for i in range(1,rem+1):
        fact = fact * i
    print(fact)
    num = num // 10
    sum += fact
    
print('sum :',sum)
if sum == temp :
    print('it\'s strong number')
else:
    print('not a strong number')