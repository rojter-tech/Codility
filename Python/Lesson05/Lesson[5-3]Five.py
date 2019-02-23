#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(A):
    n = len(A)
    minavg = 10**5 + 1
    minpos = 0
    for i in range(n-1):
        thisavg = (A[i] + A[i+1])/2
        if thisavg < minavg:
            minavg = thisavg
            minpos = i
        if i < n - 2:
            thisavg = (A[i] + A[i+1] + A[i+2])/3
            if thisavg < minavg:
                minavg = thisavg
                minpos = i
    
    return minpos

A = [4,2,2,5,1,1,8]
print(solution(A))