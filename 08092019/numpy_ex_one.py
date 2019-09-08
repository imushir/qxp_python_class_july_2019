import numpy as np

a = np.array([1,2,3])

a = np.array([1, 2, 3], dtype = complex)
print(a)


dt = np.dtype(np.int32)
dt = np.dtype('>i4')
dt = np.dtype([('age',np.int8)])

a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)

dt = np.dtype([('age',np.int8)]) 
a = np.array([(10,),(20,),(30,)], dtype = dt) 
print(a['age'])


student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a['name'])
print(a['age'])
print(a['marks'])


a = np.array([[1,2,3],[4,5,6]])
print(a.shape)


a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
print(a)


a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print(b)


a = np.arange(24)
print(a)
print(a.ndim)


# now reshape it 
b = a.reshape(2,4,3) 
print(b) 
# b is having three dimensions


x = np.array([1,2,3,4,5], dtype = np.int8) 
print(x.itemsize)


x = np.array([1,2,3,4,5], dtype = np.float32) 
print(x.itemsize)


x = np.empty([3,2], dtype = int) 
print(x)

x = np.zeros((5,), dtype = np.int)
print(x)
x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(x)


x = np.ones([2,2], dtype = int)
print(x)


x = [1,2,3]
a = np.asarray(x, dtype = float) 
print(a)


x = [(1,2,3),(4,5)] 
a = np.asarray(x) 
print(a)


s = 'Hello World' 
a = np.frombuffer(s.encode('utf-8'), 'S1') 
print(a)


# obtain iterator object from list 

list = range(5) 
it = iter(list)  

# use iterator to create ndarray 
x = np.fromiter(it, dtype = float) 
print(x)


x = np.arange(5, dtype = float)
print(x)

x = np.arange(10,20,2) 
print(x)


x = np.linspace(10,20,5, endpoint = False) 
print(x)


x = np.linspace(10,20,5, retstep = True)
print(x)


a = np.logspace(1.0, 2.0, num = 10) 
print(a)




