import random
import copy
import time
import math

#挿入ソート
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while (i>0) and (A[i] > key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key


#マージソート
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1+1) 
    R= [0]*(n2+1)  
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q + j +1]
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j +=1

def merge_sort(A,p,r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        



#リストAを作成
n = 10000
A = []
for i in range(n):
    A.append(random.randint(0,10*n))
    
#リストAのコピーを作成
B = copy.deepcopy(A)
C = copy.deepcopy(A)

#実行時間を計測
start_time = time.perf_counter()
insertion_sort(B)
end_time = time.perf_counter()
print(end_time - start_time)

#実行時間を計測
start_time = time.perf_counter()
merge_sort(C,0,len(C)-1)
end_time = time.perf_counter()
print(end_time - start_time)
