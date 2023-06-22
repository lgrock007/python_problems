# CHECK WHETHER THE GIVEN NUMBER IS PRIME NUMBER OR NOT .

num = int(input("Enter The Number: "))
count = 0
if num == 1 :
    print("Prime Number")
elif num > 1 :
    for i in range(2,num):
           if num % i == 0 :
               count += 1
        
    if count == 0 :
        print("Prime Number")
    else:
        print("Not a Prime Number")    
    
    
