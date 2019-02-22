def solution(N, A):
    countersList = N*[0]
    M = len(A)
    MAXCOUNTOPERATOR = N + 1

    countupdate = 0
    currentmax = 0
    for i in range(M):
        X = A[i]
        pos = X - 1
        if X != MAXCOUNTOPERATOR:
            if countersList[pos] < countupdate:
                countersList[pos] = countupdate + 1
            else:
                countersList[pos] = countersList[pos] + 1
            if currentmax < countersList[pos]:
                currentmax = countersList[pos]
        else:
            countupdate = currentmax
    
    for i in range(N):
        if countersList[i] < countupdate:
            countersList[i] = countupdate

    return countersList

N = 5
A = [3,4,4,6,1,4,4]
print(solution(N,A))