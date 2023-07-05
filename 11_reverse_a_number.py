num = int(input("Enter the number u wants to be reversed: "))
rem = 0 

while num > 0 :
    digit = num % 10
    rem = ( rem * 10 ) + digit 
    num = num // 10
    
print('reversed number:',rem)
    