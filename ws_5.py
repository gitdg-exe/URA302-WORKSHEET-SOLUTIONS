import numpy as np
from scipy import stats, fftpack, linalg, interpolate, signal, optimize
import matplotlib.pyplot as plt
import time
import random
import string

a = np.random.rand(20)
print(np.mean(a), np.median(a), np.var(a))

b = np.random.rand(4,4)
print(fftpack.fft2(b))

c = np.array([[2,1],[1,3]])
print(linalg.det(c))
print(linalg.inv(c))
print(linalg.eigvals(c))

x = np.linspace(0,10,10)
y = np.sin(x)
f = interpolate.interp1d(x,y,kind='cubic')
x_new = np.linspace(0,10,100)
plt.plot(x,y,'o',x_new,f(x_new))
plt.show()

t = np.linspace(0,1,500)
sig = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
filtered = signal.medfilt(sig,5)
plt.plot(t,sig,t,filtered)
plt.show()

sales = np.random.randint(50,200,(12,4))
print(np.sum(sales,axis=0))
print(np.mean(sales,axis=0))
print(np.max(sales,axis=0))
print(np.argmax(np.sum(sales,axis=1)))
print(np.argmin(np.sum(sales,axis=1)))

names = ["Arin","Aditya","Chirag","Gurleen","Kunal"]
marks = np.array([[85,78,92,88],[79,82,74,90],[90,85,89,92],[66,75,80,78],[70,68,75,85]])
total = np.sum(marks,axis=1)
avg = np.mean(marks,axis=1)
print(total)
print(avg)
print(names[np.argmax(total)])
print(names[np.argmin(total)])
print(np.mean(total>=200)*100)

t = np.array([0,1,2,3,4,5])
v = np.array([2,3.1,7.9,18.2,34.3,56.2])
def model(t,a,b,c):
    return a*t*t + b*t + c
p,_ = optimize.curve_fit(model,t,v)
print(p)

plt.plot(t,v,'o',t,model(t,*p))
plt.show()

years = np.array([2000,2005,2010,2015,2020])
pop = np.array([50,55,70,80,90])
print(stats.pearsonr(years,pop)[0])
f = interpolate.interp1d(years,pop)
print(f(2008))
plt.plot(years,pop,'o',2008,f(2008),'x')
plt.show()

coef = [3,-5,2,-8]
roots = np.roots(coef)
print(roots)
x = np.linspace(-3,3,200)
y = 3*x**3 - 5*x**2 + 2*x - 8
plt.plot(x,y)
plt.scatter(roots.real,np.zeros(len(roots)))
plt.show()

sizes = [200,400,600,800,1000]
times = []
for s in sizes:
    text = ''.join(random.choices(string.ascii_letters,k=s*1000))
    start = time.time()
    text.upper()
    times.append(time.time()-start)
plt.plot(sizes,times)
plt.show()

def f(x):
    return x**4 - 3*x**3 + 2
res = optimize.minimize_scalar(f)
print(res.x)
x = np.linspace(-2,3,200)
plt.plot(x,f(x))
plt.scatter(res.x,f(res.x))
plt.show()

def sys(y,t):
    theta,omega = y
    return [omega,-0.2*omega-theta]

t = np.linspace(0,20,400)
sol = linalg.expm(np.array([[0,1],[-1,-0.2]])*t[:,None,None])
theta = sol[:,0,0]
plt.plot(t,theta)
plt.show()
print(np.max(theta),t[np.argmax(theta)])
