import numpy as np
#Create a 4 x 4 matrix and add values 4,5,6 above the parent diagonal.
arr1=np.zeros((4,4),dtype=int)
values=[4,5,6]
for i,val in enumerate(values):
    arr1[i,i+1]=val
print(arr1)

#Given a Numpy array arr = np.arange(11), negate all the elements between 6 and 10.

arr2=np.arange(11)
for i in range(len(arr2)):
    if arr2[i]>6 and arr2[i]<10:
        arr2[i]*=-1
print(arr2)

mat = np.array([['abc','A'],['def','B'],['ghi','C'],['jkl','D']])
arr3 = np.array(['abc', 'dfe', 'ghi', 'kjl'])

for i in range(len(arr3)):
    if mat[i,0] in arr3:
        print(mat[i,1])


mat2 = np.array([[1,21,3],[5,4,2],[56,12,4]])
sorted=mat2[mat2[:,1].argsort()]
print(sorted)


arr3 = np.array([90, 14, 24, 13, 13, 590, 0, 45, 16, 50])
top_4=np.sort(arr3)[-4:][::-1]
print(top_4)
