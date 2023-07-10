# FACTOR of a number

num = int(input('Enter the Number: '))
value = 1
print(f"the factor of {num} are:")
while value <= num :
    if num % value == 0 :
        print(value,end=' ')
    value += 1


# if we need count for it how many factors are there in given number .

num = int(input('Enter the Number: '))
value = 1
count = 0
print(f"the factor of {num} are:")
while value <= num :
    if num % value == 0 :
        print(value,end=' ')
        count += 1

    value += 1
print(f'count of the given factor {num} are :',count)
