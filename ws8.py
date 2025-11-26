import math
import numpy as np

class Point:
    def __init__(self,x,y):
        self.x=x; self.y=y
    def dist(self,other):
        return math.hypot(self.x-other.x,self.y-other.y)
    def mid(self,other):
        return Point((self.x+other.x)/2,(self.y+other.y)/2)
    def line_eq(self,other):
        if other.x==self.x:
            return None,None
        m=(other.y-self.y)/(other.x-self.x)
        c=self.y-m*self.x
        return m,c
    def reflect_over_line(self,a,b):
        m,c = a.line_eq(b)
        if m is None:
            rx=2*a.x - self.x
            return Point(rx,self.y)
        A=m; B=-1; C=c
        x0,y0=self.x,self.y
        d=(A*x0+B*y0+C)/(A*A+B*B)
        xr=x0-2*A*d; yr=y0-2*B*d
        return Point(xr,yr)
    def __repr__(self):
        return f"({self.x:.3f},{self.y:.3f})"

p1=Point(*map(float,input('A x y: ').split()))
p2=Point(*map(float,input('B x y: ').split()))
print('distance',p1.dist(p2))
print('midpoint',p1.mid(p2))
m,c=p1.line_eq(p2)
if m is None:
    print('line x =',p1.x)
else:
    print(f'y={m}x+{c}')

p3=Point(*map(float,input('C x y: ').split()))
print('reflection',p3.reflect_over_line(p1,p2))

a_vec = np.array(list(map(float,input('A vec x y: ').split())))
b_vec = np.array(list(map(float,input('B vec x y: ').split())))
c_vec = np.array(list(map(float,input('C vec x y: ').split())))
R = a_vec + b_vec + c_vec
print('R',R)
print('magnitudes',np.linalg.norm(a_vec),np.linalg.norm(b_vec),np.linalg.norm(c_vec))
print('dots',a_vec.dot(b_vec),a_vec.dot(c_vec),b_vec.dot(c_vec))
def angle(u,v):
    return math.degrees(math.acos(max(-1,min(1,u.dot(v)/(np.linalg.norm(u)*np.linalg.norm(v))))))
print('angles',angle(a_vec,b_vec),angle(a_vec,c_vec),angle(b_vec,c_vec))
proj = (a_vec.dot(b_vec)/np.dot(b_vec,b_vec))*b_vec
print('proj A on B',proj)

sx,sy = map(float(input('S x y: ').split()))
ex,ey = map(float(input('E x y: ').split()))
px,py = map(float(input('P x y: ').split()))
S=np.array([sx,sy]); E=np.array([ex,ey]); P=np.array([px,py])
seg_len = np.linalg.norm(E-S)
print('segment length',seg_len)
t = np.dot(P-S,E-S)/np.dot(E-S,E-S)
t_clamped = max(0,min(1,t))
closest = S + t_clamped*(E-S)
print('closest',tuple(closest))
print('distance to segment',np.linalg.norm(P-closest))

a1,b1,c1 = map(float(input('a1 b1 c1: ').split()))
a2,b2,c2 = map(float(input('a2 b2 c2: ').split()))
D = a1*b2 - a2*b1
if abs(D)<1e-9:
    print('Lines are parallel or coincident.')
else:
    x = (c1*b2 - b1*c2)/D
    y = (a1*c2 - c1*a2)/D
    print('intersection', (x,y))
