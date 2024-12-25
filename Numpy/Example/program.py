from numpy import *
array1=array([1,2,3,4])
print(array1)
print(array1.size)
print(array1.shape)
print(array1.dtype)
print(array1.ndim)


array2=array([[1,2,3],[3,2,1],[4,5,6]])
print(array2)
print(array2.size)
print(array2.ndim)
print(array2.shape)
print(array2.dtype)
print(array2.itemsize)

array3=array([[1,2,3],[3,2,1],[4,5,6]],dtype=float64)
print(array3)
array4=array([[1,2,3],[3,2,1],[4,5,6]],dtype=complex)
print(array4)


Zeroes=zeros((3,3),dtype=int)
print(Zeroes)
Ones=ones((3,3),int)
print(Ones)

array4=arange(1,5)
print(array4)

array5=arange(0,10,2)
print(array5)

array5=linspace(1,5,10)
print(array5)

array6=array([[1,2],[3,4],[5,6]])
print(array6.shape)
print(array6.reshape(2,3))

array7=transpose(array6)
print(array7)
print(array7[:,1])
print(array7.max(0),array7.min(0),array7.sum(1),sqrt(array7))
print(std(array7))

Eye=eye(4,4,dtype=int)
print(Eye)

a=array([[1,2],[3,4]])
b=array([[5,6],[7,8]])
print(a+b)
print(a-b)
print(a.dot(b))
