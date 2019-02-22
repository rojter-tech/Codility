def solution(N, A):
    M = len(A)
    counters = N*[0]
    MAXOPER = N + 1

    currentmax = 0
    counterupdate = 0
    for i in range(M):
        X = A[i]
        pos = X - 1
        if X == MAXOPER:
            counterupdate = currentmax
        else:
            if counters[pos] < counterupdate:
                counters[pos] = counterupdate + 1
            else:
                counters[pos] = counters[pos] + 1
            if currentmax < counters[pos]:
                currentmax = counters[pos]
    
    for i in range(N):
        if counters[i] < counterupdate:
            counters[i] = counterupdate
    
    return counters


N = 5
A = [3,4,4,6,1,4,4]
print(solution(N,A))