
#Assignment 2:

#Approach 1 – The Power Method with For Loops

import math
import time
import matplotlib.pyplot as plt

N = 5
A = [[9,14,14,11,16],[9,7,10,1,11],[1,15,10,12,1],[1,1,1,1,1],[1,8,2,4,10]]
X =(1,1,1,1,1)
TOL = 10**(-6) #tol


while True:

 d = 0
 y = []
 e =[]
 for i in range(len(A[0])):    # this loops through columns of the matrix
      total = 0
      for j in range(len(X)):  # this loops through vector coordinates & rows of matrix
          total += X[j] * A[j][i]
      y.append(total)          # After all the iterations axb=c
      #print(y)
 ymax = math.fabs(y[1])

 for i in range(2,N):
     if ((math.fabs(y[i])) > ymax): # Find the largest element and assign it to d where d is the eigenvalue
         ymax = math.fabs(y[i])

 for i in range(N):
     if (ymax <= 0):
         print(' *** The power method doesn’t converge! ***')
         exit()
     else:
       y[i] = y[i] / ymax       # Calculate the eigenvector

 for i in range(N):
     temp = 0
     temp = math.fabs((math.fabs(y[i])) - (math.fabs(X[i])))
     e.append(temp)

 emax = e[1]
 for i in range(2,N):
    if(e[i]>emax):
        emax=e[i]

 for i in range(N):
     X=y

 if ( emax < TOL ):
      break

print( ' Largest Eigenvalue is :', ymax )

#print( 'Eigenvector is :')
#for i in range(N):
    #print('[',y[i],']')


print( 'time.time(): ',  time.time())


# N = 3
# A = [[6,3,2],[7,2,3],[5,5,1]] time:1569690784.78989
# A = [[6,3,2],[3,3,3],[5,5,1]] time:1569691237.421257
# A = [[1,1,1],[3,3,3],[5,5,1]] time:1569691282.076889
# A = [[1,1,1],[3,3,3],[2,2,2]] time:1569691336.693917
# A = [[1,2,3],[3,5,3],[4,2,4]] time:1569691407.902312

p1 = [1569690784.78989,1569691237.421257,1569691282.076889,1569691336.693917,1569691407.902312 ]

sum1 = 0
Ave1 = 0
for i in p1:
    sum1 += sum1 + i
Ave1 = sum1/5
print('Performance N=3:', Ave1)


# N = 4
# A = [[1,2,3,1],[3,5,3,1],[4,2,4,1],[1,1,1,1]] time:1569694071.608535
# A = [[1,2,3,5],[3,5,4,4],[4,5,4,1],[1,3,4,5]] time:1569694151.394975
# A = [[1,7,8,5],[3,7,4,8],[1,2,4,5],[1,6,7,8]] time:1569694220.795313
# A = [[9,7,8,9],[9,9,9,9],[1,9,8,7],[2,9,7,8]] time:1569694288.611074
# A = [[9,4,8,4],[9,1,1,1],[5,9,8,8],[5,9,5,8]] time:1569694344.3300722

p2 = [ 1569694071.608535,1569694151.394975,1569694220.795313,1569694288.611074,1569694344.3300722 ]

sum2 = 0
Ave2 = 0
for i in p2:
    sum2 += sum2 + i
Ave2 = sum2/5
print('Performance N=4:', Ave2)

# N = 5
# A = [[9,4,8,4,1],[9,1,1,1,1],[5,9,8,8,1],[5,9,5,8,1],[1,2,3,4,5]] time:1569694597.820024
# A = [[2,3,8,4,1],[9,8,7,6,5],[5,7,7,7,1],[5,6,7,8,1],[1,6,7,8,5]] time:1569694680.061257
# A = [[11,3,8,9,1],[9,8,10,6,11],[5,15,13,12,1],[5,6,7,8,1],[1,7,7,9,10]] time:1569694743.943454
# A = [[12,3,14,15,16],[9,11,10,16,11],[11,15,13,15,1],[15,14,11,8,12],[11,18,12,14,10]] time:1569694855.41048
# A = [[9,14,14,11,16],[9,7,10,1,11],[1,15,10,12,1],[1,1,1,1,1],[1,8,2,4,10]] time:1569694990.543963

p3 = [ 1569694597.820024,1569694680.061257,1569694743.943454,1569694855.41048,1569694990.543963  ]

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