str1=input("Enter the string: ")
str2=input("Enter the string: ")
common=""
for ch in str1:
    if ch in str2 and ch not in common:
        common=common+ch
print("common letters is: ",common)        
        