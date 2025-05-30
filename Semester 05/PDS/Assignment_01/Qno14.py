# str = 'madam'
# new_str = ""

# new_str = str[::-1]

# if(str == new_str):
#     print(' is Palindrome')
# else:
#     print(' is not Palindrome')

original  = 121
reverse = 0
digit = 0

while(original > 0):
    digit = original % 10
    reverse = reverse * 10 + digit
if(original == reverse):
     print('Number is palindrome')
else:
    print('Number is not palindrome')


number = 123
rev = 0
rev = str(number)
if(rev == number):
    print('Palindrome')
else:
    print('Not palindrome')