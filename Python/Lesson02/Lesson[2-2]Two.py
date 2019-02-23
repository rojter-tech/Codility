#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(A, K):
    if len(A) == 0:
        return A
    for i in range(K):
        last = [A[-1]]
        del A[-1]
        A = last + A
    return A


A = []
K = 3
B = solution(A, K)
print(B)