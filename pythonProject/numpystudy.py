

# NUMPY LIBRARY WHICH IS CREATED BY TRAVIS OLIPHANT


import numpy as np
from termcolor import cprint, colored

# The version is stored under _version_
print(np.__version__)

# Creating a ndarray
cprint('creating nd array','blue','on_yellow')
var = np.array([1, 2, 3, 5])  # we can pass LIST, TUPLE, and integer value

print("\nndarray:", var)
print('type of', var, ':', type(var))
print()

# 0D, 1D, 2D array..
cprint('0D, 1D, 2D, 3D..','red','on_cyan')
nd=np.array((42))
nd1=np.array([1, 2, 3, 4])
nd2=np.array([[1,2,3,4],[5,6,7,8]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('\nOD array:', nd)
print("1D array:", nd1)
print('2D array:\n', nd2)
print("3D array:\n",d)
cprint('shape of the 3D array:','blue',attrs=['bold','underline'])
print(d.shape)
print()

# ARRAY INDEXING
cprint('ARRAY INDEXING','green','on_cyan')
arr=np.array([1,2,3,4,7,8])
arr1=np.array([[12,13,14,15],[16,17,18,19]])
print('\naccesing index 4 from',arr,':',arr[4])
print('accessing index 4 from\n',arr1,':',arr1[0:,3])
print('accessing index 2 from index 1th array\n',arr1,':',arr1[1,2])
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print('accessing indexes in 3d array:',arr2[0, 1, 2])
print()

# Slicing an array
cprint('slicing a multidimensional array','yellow','on_red')
# arrs=np.array([[1,2,3,4,5],[6,7,8,9,10]])
arrs = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('slicing in 2d array',arrs,':',arrs[1, 1:4])

# studying about datatype
print()
cprint('create an array with defined datatype','blue','on_green')
first=np.array([1,2,3,4,5],dtype='i')
print(first)
print('checking the datatype of ',first,':',first.dtype)
sec = np.array([1, 2, 3, 4], dtype='S')
print('checking the datatype of ',sec,':',sec.dtype)
print()

# copy and view
cprint('copy and view','red','on_green')
Myarray=np.array(['hello','world','apple','something'],dtype='S')
print('original array:',Myarray)
changed_arr=Myarray.view()
changed_arr[1]='man'

print('viewed array:',changed_arr)
print('original array:',Myarray)
copy=Myarray.copy()
copy[0]='hai'
print('copied array:',copy)
print()

# reshaping the array
cprint('RESHAPING THE ARRAY BY PASSING PARAMETERS', 'green', 'on_cyan')
data= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = data.reshape(2, 3, 2)
print('rashaped array:\n', newarr)

# iterating via array
cprint('ITERATING VIA ARRAY', 'blue', 'on_yellow', attrs=['underline'])
oldarray = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in oldarray:
  for y in x:
    for z in y:
      print('iterating....\n', z)

edited = np.array(oldarray, dtype='int', order='F')
for i in np.nditer(edited):
    print(i)
print()

# Splitting the array using 'split(), array_split()'
cprint("splitting the array using split(), array_split()", 'magenta', 'on_green', attrs=['bold'] )
split=np.arange(10).reshape((2,5))
print('num=\n',split)
splitted=np.split(split,2)
print('splitted array:\n',splitted)
print('splitted array using array_split():\n',splitted)

hsp = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr1 = np.hsplit(hsp, 3)
newarr2=np.vsplit(hsp,3)
print('using hsplit function:\n',newarr1)
print('using vsplit function:\n', newarr2)

# searching an array
print()
cprint('SEARCHING AN ARRAY', 'green', 'on_cyan', attrs=['bold'])
func=np.array([1, 2, 3, 4, 5, 6, 7, 8, 4])
x=np.where(func==4)
y=np.where(func%2==0)
print('searching the index for the element 4: \n', x)
print('listing out the elements divisible by 2: \n', y)

z= np.searchsorted(func, 1, side='right')
print('using searchsorted:', z)
print()

# sorting an array
cprint('sorting an nd array', 'blue', 'on_red' )
nd=np.array([[99, -9, 8, 5, 4], [1, 2, -1, 4, 5]])
m=np.sort(nd)
print(m)