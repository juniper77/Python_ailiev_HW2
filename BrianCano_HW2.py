#Brian Cano


A = 5 * np.random.random((3, 5)) #3 rows by 5 columns of random numbers
print ("Matrix A: \n", A)

print ("Size of A: \n", A.size)
#returns the number of elements in matrix. so, 3(5) = 15

print ("Shape (rows columns) of A: \n", A.shape)
#returns the values of rows and column, or "length" of a matrix (3, 5)

A = A[:,:4]  #resize matrix A to size (3,4) ...
#this selects all rows and all but the last column 
print ("Matrix A resized; last column dropped: \n", A)

B=A.T #get the transpose of A, assign it to B 
print ("B is the transpose of A: \n", B)

print ("min value of column 1 in matrix B: \n", B[:,1].min())
#find the min value of column 1 in matrix B
# Note that I count the leftmost column as column 0.  

print ("Min of A: \n", A.min())
A.min() #min value in entrire matrix A
print ("Max of A: \n", A.max())
#max value in entrire matrix A

X = np.random.random(4)
print ("Vector X: \n", X)
 #make a vector X with 4 random numbers

#create a func4on and pass X and A in it

def func4on(vector1, matrix1):
    D = vector1*matrix1
    return D
    
D=func4on(X, A)    
print ("This is D, the result of a function: \n", D)


Z = complex(2, 3) #Create a complex number Z with absolute and real parts != 0
 
#Show its real and imaginary parts as well as its absolute value
print ("The real part of my complex number is: ",end="")
print(Z.real) 
print ("The imaginary part of my complex number is: ",end="")
print(Z.imag)

print ("The absolute value of my complex number is: ", abs(Z))

B = str(B)
print ('Brian Cano is done with HW2') 
    
