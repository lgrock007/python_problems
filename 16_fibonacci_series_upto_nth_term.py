n = int(input('Enter the number: '))
first = 0 
second = 1
print('Fibonacci Series:')
for i in range(n):
    print(first,end=' ')
    temp = first
    first = second
    second += temp