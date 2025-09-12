# Worksheet 1 Solutions

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

first = input()
last = input()
print(last, first)

r = float(input())
print(3.14159*r*r)

color_list = ["Red","Green","White","Black"]
print(color_list[0], color_list[-1])

n = int(input())
print(n + int(str(n)*2) + int(str(n)*3))

data = input().split(",")
print(list(data), tuple(data))

c = float(input())
print((c*9/5)+32)

a,b = map(int,input().split())
a,b = b,a
print(a,b)

n = int(input())
print("Even" if n%2==0 else "Odd")

year = int(input())
print("Leap" if (year%4==0 and year%100!=0) or year%400==0 else "Not Leap")

import math
x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())
print(math.dist([x1,y1],[x2,y2]))

a,b,c = map(int,input().split())
print("Triangle" if a+b+c==180 else "Not Triangle")

p,t,r = map(float,input().split())
print(p*((1+r/100)**t -1))

n = int(input())
prime = True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        prime=False
        break
print("Prime" if prime and n>1 else "Not Prime")

N = int(input())
print(sum(i*i for i in range(1,N+1)))
