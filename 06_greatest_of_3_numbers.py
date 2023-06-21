num_1 = int(input("Enter the Number 1 : "))   # 10 
num_2 = int(input("Enter the Number 2 : "))   # 20
num_3 = int(input("Enter the Number 3 : "))   # 30

if (num_1 >= num_2) and (num_1 >= num_3) :  
    print("no 1 :",num_1)
elif (num_2 >= num_1) and (num_2 >= num_3) :
    print("no 2 :",num_2)
else : 
    print("no 3 :",num_3)