#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(X, A):
    N = len(A)
    reqpos = X*[0]
    appliedpos = 0
    for i in range(N):
        if reqpos[A[i] - 1] == 0:
            reqpos[A[i] - 1] = A[i]
            appliedpos = appliedpos + 1
        if appliedpos == X:
            return i
    return -1


X = 5
A = [1,5,3,4,2,3,4,5]
print(solution(X,A))