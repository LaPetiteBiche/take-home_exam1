import numpy as np

array = np.loadtxt('/files/take-home-1/Exam/Question_4/aux_data.txt')
array = np.reshape(array,(20,20))
print(array)
x1, x2 = array.shape

max = 0

for x in range(x1-3) :
    for i in range(x2-3) :
        test = array[x,i]*array[x,i+1]*array[x,i+2]*array[x,i+3]
        if test > max:
            max = test
            numbers = (array[x,i],array[x,i+1],array[x,i+2],array[x,i+3])
        test = array[i,x]*array[i+1,x]*array[i+2,x]*array[i+3,x]
        if test > max:
            max = test
            numbers = (array[i,x],array[i+1,x],array[i+2,x],array[i+3,x])
        test = array[x,i]*array[x+1,i+1]*array[x+2,i+2]*array[x+3,i+3]
        if test > max:
            max = test
            numbers = (array[x,i],array[x+1,i+1],array[x+2,i+2],array[x+3,i+3])
        test = array[x+3,i]*array[x+2,i+1]*array[x+1,i+2]*array[x,i+3]
        if test > max:
            max = test
            numbers = (array[x+3,i],array[x+2,i+1],array[x+1,i+2],array[x,i+3])

print(max)
print(numbers)