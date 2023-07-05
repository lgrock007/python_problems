# Palindrome 

value = input("Enter the value:")

rev_value = value[::-1]

if value == rev_value :
    print(rev_value,"is a palindromic value")
else :
    print('Not a Palindromic Value')