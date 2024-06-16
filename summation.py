'''The function accepts two integers n, m as arguments Find the sum of all numbers in range from 1 to m(both inclusive)'
' that are not divisible by n.
Return difference between sum of integers not divisible by n with sum of numbers divisible by n.

Assumption:

n>0 and m>0
Sum lies between integral range
Example

Input
n:4
m:20
Output
90'''

def summation(n,m):
    sum=0
    sum1=0
    for i in range(1,m+1):
        if i%n==0:
            sum=sum+i
        else:
            sum1=sum1+i
    return sum-sum1
n=int(input())
m=int(input())
print(summation(n,m))
        

