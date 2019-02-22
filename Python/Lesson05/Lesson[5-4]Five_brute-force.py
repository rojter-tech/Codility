def solution(A, B, K):
    trackdiv = 0
    for i in range(A,B+1):
        if i%K == 0:
            trackdiv = trackdiv + 1
    return trackdiv


shift = 6
A = 11  + shift
B = 345 + shift
K = 17
print(solution(A, B, K))



shift = 0
A = 101  + shift
B = 123456789 + shift
K = 10000