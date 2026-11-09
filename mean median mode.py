a=[1,2,2,2,3,5,6,7,7,8]
n=7
s=0
for i in a :
    s+=i
    
mean=s/7
print("mean is",mean) 
median=print((n+1)/2)

from collections import Counter

def find_frequencies(a):

    return dict(Counter(a))

a = [1,2,2,2,3,5,6,7,7,8]
print(find_frequencies(a))


def highest_frequency(a):
    if not a:
        return None
    
    return Counter(a).most_common(1)[0][0]

a=  [1,2,2,2,3,5,6,7,7,8]
print( "mode of a is",highest_frequency(a))  


a=  [1,2,2,2,3,5,6,7,7,8]
v = 0
for i in range(len(a)):
    v= v + ((i-mean)**2)
print( " variance is ",v/len(a))   
    
import math   
std=0
for i in range(len(a)):
    std=std+((i-mean)**2)
    
sd=std/len(a)-1
print("standard deviation is ",math.sqrt(sd))        