import numpy as np 
a = np.arange(10)
print(a)
s = slice(2,7,2)
print("Step size is ", s)
print(a[s])

a = np.arange(10) 
b = a[2:7:2] 
print(b)


a = np.arange(10) 
b = a[5] 
print(b)


a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
print(a)  

# slice items starting from index
print('Now we will slice the array from the index a[1:]')
print(a[1:])



 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print('Array is:') 
print(a)
print('\n')  

# this returns array of items in the second column 
print('The items in the second column are:')  
print(a[...,1]) 
print('\n')  

# Now we will slice all items from the second row 
print('The items in the second row are:') 
print(a[1,...])
print('\n')  

# Now we will slice all items from column 1 onwards 
print('The items column 1 onwards are:') 
print(a[...,1:])


x = np.array([[1, 2], [3, 4], [5, 6]])

#[1, 2]-- ((0,0), (0, 1))
#[3, 4]-- ((1, 0), (1,1))
#[5, 6] -- ((2, 0), (2, 1))

y = x[[0,1,2], [0,1,0]] #((0, 0), (1, 1), (2, 0))
print(y)


x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
   
print('Our array is:') 
print(x)
print('\n') 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols] 
   
print('The corner elements of this array are:')
print(y)


x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print('Our array is:') 
print(x)
print('\n')  

# slicing 
z = x[1:4,1:3]


print('After slicing, our array becomes:')
print(z) 
print('\n')  

# using advanced index for column 
y = x[1:4,[1,2]] 

print('Slicing using advanced index for column:') 
print(y)

x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print('Our array is:') 
print(x)
print('\n')  

# Now we will print the items greater than 5 
print('The items greater than 5 are:')
print(x[x > 5])



a = np.array([1, 2+6j, 5, 3.5+5j]) 
print(a[np.iscomplex(a)])



# iterating over array

a = np.arange(0,60,5)
a = a.reshape(3,4)

print('Original array is:')
print(a)
print('\n')

print('Modified array is:')
for x in np.nditer(a):
   print(x)


a = np.arange(0,60,5) 
a = a.reshape(3,4) 
   
print('Original array is:')
print(a) 
print('\n')  
   
print('Transpose of the original array is:')
b = a.T 
print(b)
print('\n')  
   
print('Modified array is:')
for x in np.nditer(b): 
   print(x)


a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)
print('\n')

print('Transpose of the original array is:')
b = a.T
print(b)
print('\n')

print('Sorted in C-style order:')
c = b.copy(order = 'C')
print(c)
for x in np.nditer(c):
   print(x)


print('Sorted in F-style order:')
c = b.copy(order = 'F')
print(c)
for x in np.nditer(c):
   print(x)

a = np.arange(0,60,5) 
a = a.reshape(3,4) 

print('Original array is:') 
print(a)
print('\n')  

print('Sorted in C-style order:')
for x in np.nditer(a, order = 'C'): 
   print(x)  
print('\n')

print('Sorted in F-style order:') 
for x in np.nditer(a, order = 'F'): 
   print(x)

a = np.arange(0,60,5)
a = a.reshape(3,4)
print('Original array is:')
print(a)

for x in np.nditer(a, op_flags = ['readwrite']):
   x[...] = 2*x
print('Modified array is:')
print(a)


a = np.array([1,2,3,4,5]) 
np.save('outfile',a)

b = np.load('outfile.npy') 
print(b)

a = np.array([1,2,3,4,5]) 
np.savetxt('out.txt',a) 
b = np.loadtxt('out.txt') 
print(a)