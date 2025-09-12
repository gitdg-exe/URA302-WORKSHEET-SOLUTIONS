import numpy as np

a1 = np.arange(5,26)
print(a1)

a2 = np.random.randint(10,51,(3,4))
print(a2)

print(a1.shape,a1.size,a1.dtype)
print(a2.shape,a2.size,a2.dtype)

arr1 = np.array([2,4,6,8,10])
arr2 = np.array([1,3,5,7,9])
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

b = np.arange(1,10).reshape(3,3)
print(b*5)

c = np.arange(10,26).reshape(4,4)
print(c[1])
print(c[:,-1])
c[0]=0
print(c)

d = np.random.randint(20,41,10)
print(d[d>30])

e = np.arange(11,23)
print(e.reshape(3,4))

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A@B)
print(A.T)

f = np.random.randint(10,61,15)
print(f.mean(),np.median(f),f.std())

M = np.array([[2,1,3],[0,5,6],[7,8,9]])
print(np.linalg.det(M))
print(np.linalg.inv(M))
w,v = np.linalg.eig(M)
print(w)
print(v)

pos = np.array([[0,0],[2,3],[4,7],[7,10],[10,15]])
print(np.linalg.norm(pos[-1]-pos[0]))
steps = np.diff(pos,axis=0)
print(np.sum(np.linalg.norm(steps,axis=1)))
