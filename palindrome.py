word=input("Enter a word: ")
if word == word[::-1]:
    print(word,"palindrome")
else:
    print(word,"not palindrome")