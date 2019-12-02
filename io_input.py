# 123456789
# 2345678
# 2468
a = '123456789'
print(a)
print(a[1:8:1])
print(a[1:8:2])
print(a[::-1])


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('Enter text:')
if is_palindrome(something):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')
