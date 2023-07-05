 # ARMSTRONG NUMBER
 
num = int(input('Enter the number:'))
sum = 0 
order = len(str(num))
temp = num 
while temp > 0 :
    value = temp % 10
    sum = sum + ( value ** order )
    temp = temp // 10

if sum == num :
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")    
