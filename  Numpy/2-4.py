import numpy as np
P = np.array([[2,1,6],[7,6,7],[7,3,2],[3,7,4],[1,4,5],[1,6,2],[4,4,7]])
flag =['A619','B569','B349','C857','D827','D727','E463']
m = -1
Q = np.zeros((9*len(P),3),dtype=int)
for i in range(len(P)):
    for j in range(len(P)):
        if i < j and m < Q.shape[0]-1:   # i != j
            m += 1
            for n in range(3):
                Q[m][n] = (P[i]-P[j])[n]
            print(m+1, Q[m], (flag[i],flag[j]))