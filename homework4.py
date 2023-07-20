def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while (i>0) and (A[i] > key):
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

    # return A

A = [1,4,2,8,9,3,3,19]
insertion_sort(A)
print(A)
