import time
import random


def find_intersection(A, B, p, s, a, b):
    r = random.randrange(p, s+1)
    tmp1 = A[r]
    tmp2 = B[r]
    A[r] = A[s]
    B[r] = B[s]
    A[s] = tmp1
    B[s] = tmp2
    a = A[s]
    b = B[s]
    for i in range(p, s):
        if A[i] < b and B[i] > a:
            if A[i] > a:
                a = A[i]
            if B[i] < b:
                b = B[i]
    return (a, b)

def partion_right(A, B, a, p, s):
    i = p-1
    for j in range(p, s):
        if (A[j]) <= a:
            i += 1
            tmp1 = A[i]
            tmp2 = B[i]
            A[i] = A[j]
            B[i] = B[j]
            A[j] = tmp1
            B[j] = tmp2
    tmp1 = A[i + 1]
    tmp2 = B[i + 1]
    A[i + 1] = A[s]
    B[i + 1] = B[s]
    A[s] = tmp1
    B[s] = tmp2
    return i + 1

def partion_left_middle(A, B, b, p, r):
    i = p - 1
    for j in range(p, r):
        if (B[j]) <= b:
            i += 1
            tmp1 = A[i]
            tmp2 = B[i]
            A[i] = A[j]
            B[i] = B[j]
            A[j] = tmp1
            B[j] = tmp2
    tmp1 = A[i + 1]
    tmp2 = B[i + 1]
    A[i + 1] = A[r]
    B[i + 1] = B[r]
    A[r] = tmp1
    B[r] = tmp2
    return i + 1

def fuzzysort(A, B, p, s):
    if p < s:
        a = b = 0
        region = find_intersection(A, B, p, s, a, b)
        a = region[0]
        b = region[1]
        r = partion_right(A, B, a, p, s)
        q = partion_left_middle(A, B, b, p, r)
        fuzzysort(A, B, p, q-1)
        fuzzysort(A, B, r+1, s)

#A = [5,1,4,8]
#B = [7,3,6,10]
A = [6,9,13,3,11,13,12,14,9,5,7,1,1,6]
B = [7,11,14,7,15,14,14,15,15,7,9,5,9,10]
print ("Input array A is as follows" + str(A))
print ("Input array B is as follows" + str(B))

start_time = time.time()
fuzzysort(A, B, 0, len(A) -1)
end_time = time.time()
print("Time taken by fuzzy sort: ",end_time-start_time)

print ("Fuzzy Sorted Output array A is as follows" + str(A))
print ("Fuzzy Sorted Output array B is as follows" + str(B))

