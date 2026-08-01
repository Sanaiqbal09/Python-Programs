sentence=input("Enter the sentence: ")
words=sentence.split()
printed=[]
for word in words:
    if word not in printed:
        printed.append(word)
        print("count of",word,"=",words.count(word))
        