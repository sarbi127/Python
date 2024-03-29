
#Assignment 2:

#Approach 2 – The Power Method with NumPy Functions

import time
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

N = 3
TOL = 10**(-6) #tol

def power_method(A,x):
    eig = []
    Ac = np.copy(A)
    lamb = 0
    for i in range(N):
        while True:
            x_1 = Ac.dot(x) # y_n = A*x_(n-1)
            x_norm = la.norm(x_1)
            #print(x_norm)
            if ((x_norm) < 1 ):
                print(' *** The power method doesn’t converge! ***')
                exit()
            else:
                x_1 = x_1/x_norm  # x_n = y_n/||y_n||

            if(abs(lamb - x_norm) <= TOL): # If precision is reached, it returns eigenvalue
                break
            else:
                lamb = x_norm
                x = x_1
        eig.append(lamb)

    eig=np.amax(eig) #max eigenvalue

    return eig

A = np.array([[9,14,14,11,16],[9,7,10,1,11],[1,15,10,12,1],[1,1,1,1,1],[1,8,2,4,10]])
X = np.array([1, 1, 1, 1, 1])
print('Largest Eigenvalue is :',power_method(A,X))


print( 'time.time(): ',  time.time())


# N = 3
# A = [[6,3,2],[7,2,3],[5,5,1]] time:1569699348.125547
# A = [[6,3,2],[3,3,3],[5,5,1]] time:1569699441.4448042
# A = [[1,1,1],[3,3,3],[5,5,1]] time:1569699461.359714
# A = [[1,1,1],[3,3,3],[2,2,2]] time:1569699484.4515998
# A = [[1,2,3],[3,5,3],[4,2,4]] time:1569699502.3370082

p1 = [ 1569699348.125547,1569699441.4448042,1569699461.359714,1569699484.4515998,1569699502.3370082 ]

sum1 = 0
Ave1 = 0
for i in p1:
    sum1 += sum1 + i
Ave1 = sum1/5
print('Performance N=3:', Ave1)

# N = 4
# A = [[1,2,3,1],[3,5,3,1],[4,2,4,1],[1,1,1,1]] time:1569699643.372194
# A = [[1,2,3,5],[3,5,4,4],[4,5,4,1],[1,3,4,5]] time:1569699679.833382
# A = [[1,7,8,5],[3,7,4,8],[1,2,4,5],[1,6,7,8]] time:1569699698.5883899
# A = [[9,7,8,9],[9,9,9,9],[1,9,8,7],[2,9,7,8]] time:1569699720.7301419
# A = [[9,4,8,4],[9,1,1,1],[5,9,8,8],[5,9,5,8]] time:1569699749.8404741

p2 = [ 1569699643.372194,1569699679.833382,1569699698.5883899,1569699720.7301419,1569699749.8404741 ]

sum2 = 0
Ave2 = 0
for i in p2:
    sum2 += sum2 + i
Ave2 = sum2/5
print('Performance N=4:', Ave2)



# N = 5
# A = [[9,4,8,4,1],[9,1,1,1,1],[5,9,8,8,1],[5,9,5,8,1],[1,2,3,4,5]] time:1569699947.431254
# A = [[2,3,8,4,1],[9,8,7,6,5],[5,7,7,7,1],[5,6,7,8,1],[1,6,7,8,5]] time:1569699972.6733718
# A = [[11,3,8,9,1],[9,8,10,6,11],[5,15,13,12,1],[5,6,7,8,1],[1,7,7,9,10]] time:1569700002.299587
# A = [[12,3,14,15,16],[9,11,10,16,11],[11,15,13,15,1],[15,14,11,8,12],[11,18,12,14,10]] time:1569700028.201375
# A = [[9,14,14,11,16],[9,7,10,1,11],[1,15,10,12,1],[1,1,1,1,1],[1,8,2,4,10]] time:1569700052.440317

p3 = [ 1569699947.431254,1569699972.6733718,1569700002.299587,1569700028.201375,1569700052.440317 ]

sum3 = 0
Ave3 = 0
for i in p3:
    sum3 += sum3 + i
Ave3 = sum3/5
print('Performance N=5:', Ave3)

P_N = [Ave1,Ave2,Ave3]
#print(P_N)

x = []
y = []

plt.plot(P_N, label=' For varying N ')
plt.xlabel('x')
plt.title(' The Performance ')
plt.legend()
plt.show()
plt.savefig('fig.png')












