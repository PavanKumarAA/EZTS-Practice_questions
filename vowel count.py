# happy fathers day
# extract the vowel which has max count
#Count of Maximum vowels
from collections import Counter
def countOfOvels(str):
    lis = Counter(str)
    lis2 = list()
    lis3 = ['a','e','i','o','u']
    for i,v in lis.items():
        if i in lis3:
            lis2.append(v)
    return max(lis2)
str = input()
print(countOfOvels(str))