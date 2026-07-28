#to count characters ina string
'''
word=input("enter the word: ")
count=0
for ch in word:
    count =count +1
print("no.of characters in a string: ",count)
'''

#to count vowels
'''
word=input("enter the word: ")
count=0
for ch in word:
    if ch in "aeiouAEIOU":
        count =count +1
print("no.of Vowels: ",count)
'''

#to count how many times a appeared in astring
'''
word=input("enter the word: ")
count=0
for ch in word:
    if ch in "a":
        count =count +1
print("no.of times a appeared is: ",count)
'''

#to count upper case letter in string
'''
word=input("Enter the string: ")
count=0
for ch in word:
    if ch in word.upper():
        count=count+1
print("count of uppercase letters: ",count)
'''

#Count words ending with vowels
sentence=input("Enter the sentence: ")
words=sentence.split()
count=0
for word in words:
    if word[-1].lower() in "aeiou":
        count=count+1
print("count of word ending in vowel = ",count)
