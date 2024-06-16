from collections import Counter
str = input()
str = list(str)
for i in str:
    if i in "aeiou":
        s = i
        break
str.remove(s)
s1 = str.index(s)
print(s1+1)