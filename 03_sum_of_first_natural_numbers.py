"""
if  n is 5 means

answer will be 0 + 1 + 2 + 3 + 4 + 5 = 15

"""
# find the sum of the first natural number 
sum = 0
num = int(input("Enter the Number: "))
if num<0:
  print("Enter a Positive Number.")
elif num==0:
  print("Your Number is 0")
if num>0:
    for i in range(num+1):
      sum=sum+i
    print("The Sum of the first %d natural numbers is %d" %(num,sum))
    
    

"""
num = 5 

5 > 0 :

5 + 1 :


0 , 1 , 2 , 3 , 4 , 5

sum = 0 

0 + 1 = 1 

1 + 2 = 3 

3 + 3 = 6 

6 + 4 = 10

10 + 5 = 15


"""
    
