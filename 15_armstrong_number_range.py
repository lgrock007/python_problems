# ARMSTRONG Number Given in a range 

lower = int(input('Enter the number A :'))
upper = int(input('Enter the Number B :'))

for i in range(lower,upper+1):
    order = len(str(i))
    sum = 0 
    temp = i 
    while temp > 0 :
        value = temp % 10 
        sum = sum + ( value ** order )
        temp = temp // 10
    if i == sum :
        print(i)
    