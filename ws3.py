def diff17(n):
    return abs(n-17)*2 if n>17 else 17-n

def test_range(n):
    return 100<=n<=1000 or n==2000

def rev(s):
    return s[::-1]

def count_case(s):
    u=l=0
    for c in s:
        if c.isupper(): u+=1
        elif c.islower(): l+=1
    return {"upper":u,"lower":l}

def distinct(l):
    return list(set(l))

def even_list(l):
    return [x for x in l if x%2==0]

def robot():
    def move():
        print("moving")
    move()

def student(name,age,course):
    print(student.__code__.co_varnames[:3])

def move_robot(x,y,d):
    if d=="up": return (x,y+1)
    if d=="down": return (x,y-1)
    if d=="left": return (x-1,y)
    if d=="right": return (x+1,y)

def classify_temperature(t):
    if t<15: return "Cold"
    if t<=30: return "Moderate"
    return "Hot"

def is_goal_reached(path):
    x=y=0
    for p in path:
        if p=="up": y+=1
        elif p=="down": y-=1
        elif p=="left": x-=1
        elif p=="right": x+=1
    return (x,y)==(2,0)

class Student:
    def __init__(self,i,n,c=None):
        self.student_id=i
        self.student_name=n
        self.student_class=c
    def display(self):
        print(self.__dict__)

s1=Student(1,"A","CS")
s2=Student(2,"B","ME")
print(s1.__dict__,s2.__dict__)

class Circle:
    def __init__(self,r): self.r=r
    def area(self): return 3.14159*self.r*self.r
    def perimeter(self): return 2*3.14159*self.r

class StringClass:
    def get_String(self): self.s=input()
    def print_String(self): print(self.s.upper())

class Robot:
    def __init__(self,n,t): 
        self.name=n
        self.task=t
        self.battery=100
    def perform_task(self):
        print(self.name,"performing",self.task)
        self.battery-=10
    def recharge(self):
        self.battery=100
    def status(self):
        print(self.name,self.task,self.battery)
