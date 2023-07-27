# AUTOMORPHIC NUMBER

n = int(input('Enter the number: '))
sqrnum = n * n
k = len(str(n))
lastdigit = int(str(sqrnum)[-k:])
if lastdigit == n :
    print('It\'s an automorphic number')
else:
    print('not a automorphic number')