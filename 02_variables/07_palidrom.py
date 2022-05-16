palindrome = input('Insert a palindrome and check')
palindrome = str(palindrome)
reversed = palindrome[::-1]
print(f'This is reversed: {str(reversed)}')
print(f'Your word is a palindrome: {palindrome == reversed}')
