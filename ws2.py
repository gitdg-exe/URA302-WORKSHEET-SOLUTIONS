L = [11,12,13,14]
L += [50,60]
print(L)
L.remove(11); L.remove(13)
print(L)
print(sorted(L))
print(sorted(L, reverse=True))
print(13 in L)
print(len(L))
print(sum(L))
print(sum(x for x in L if x%2))
print(sum(x for x in L if x%2==0))
def prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
print(sum(x for x in L if prime(x)))
L.clear()
print(L)
del L

lst=[1,2,3]
s=0
for i in lst: s+=i
print(s)

p=1
for i in [1,2,3]: p*=i
print(p)

a=[[[ '*' for k in range(6)] for j in range(4)] for i in range(3)]
print(a)

D={1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}
D[8]=8.8
D.pop(2)
print(6 in D)
print(len(D))
print(sum(D.values()))
D[3]=7.1
D.clear()

S1={10,20,30,40,50,60}
S2={40,50,60,70,80,90}
S1|={55,66}
S1-={10,30}
print(40 in S1)
print(S1|S2)
print(S1&S2)
print(S1-S2)

import random,string
for i in range(100):
    l=random.randint(6,8)
    print(''.join(random.choice(string.ascii_letters) for _ in range(l)))

for i in range(600,801):
    if prime(i): print(i)

for i in range(100,1001):
    if i%63==0: print(i)

d=(11,12,2025)
print(f"The examination will start from: {d[0]} / {d[1]} / {d[2]}")

nums=[10,15,20,25,30]
for n in nums:
    if n%5==0: print(n)

n=int(input())
print(n%2==0)

s="Emma is good. Emma likes python. Emma"
print(s.count("Emma"))

l1=[1,2,3,4,5]
l2=[6,7,8,9]
print([x for x in l1 if x%2]+[y for y in l2 if y%2==0])

pos=[(2,3),(4,5),(6,7),(7,8)]
print([p for p in pos if p[0]%2==0])

sensor={1:2.3,2:4.5,3:1.8,4:3.6}
print([k for k,v in sensor.items() if v>3])

rec={"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
exe={"MOVE","TURN_LEFT","STOP"}
print(rec-exe)
