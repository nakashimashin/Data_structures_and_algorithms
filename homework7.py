import math
import random


class Heap:
    
    def __init__(self, A):
        self.A = A
        
    def __len__(self):
        return len(self.A)

    def __getitem__(self, key):
        return self.A[key]#

    def __setitem__(self, key, value):
        self.A[key] = value
        
    def __str__(self):
        return str(self.A)

#Left,Rightの定義
    
def Parent(i):
    return[i/2]

def Left(i):
    return 2*i

def Right(i):
    return 2*i+1
    
# Max-Heapifyのコード

def Max_Heapify(A,i):
    l = Left(i)
    r = Right(i)
    if l <= A.heap_size and A[l-1] > A[i-1]:#
        largest = l
    else:
        largest = i
    if r<=A.heap_size and A[r-1] > A[largest-1]:
        largest = r
    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        Max_Heapify(A,largest) 
# build_max_heapのコード
        
def build_max_heap(A):
    A.heap_size = len(A)#
    for i in range(math.floor(len(A)/2),-1,-1):##
        Max_Heapify(A,i+1)#
           
        
#Heapsortのコード

def heapsort(A):
    build_max_heap(A)#
    for i in range(len(A)-1,0,-1):##pytho
        A[0],A[i] = A[i],A[0]
        A.heap_size = A.heap_size - 1
        Max_Heapify(A,1)
        
#リストB
A = [0]*8
B = Heap(A)

#正しくソートされているか確認
B = Heap(random.sample([1,2,3,4,5,6,7,8],8))
print(B)
heapsort(B)#
print(B)
