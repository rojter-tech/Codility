def solution(A):
    N = len(A)
    zerosIndexes = []
    numberofzeros = 0
    numberofones = 0
    for i in range(N):
        if A[i] == 0:
            zerosIndexes.append(i)
            numberofzeros = numberofzeros + 1
        else:
            numberofones = numberofones + 1

    if numberofzeros == N or numberofones == N:
        return 0

    onesafterfirstzero = numberofones - zerosIndexes[0]
    onesAfterZeros = [onesafterfirstzero]
    trackones = onesafterfirstzero
    for i in range(len(zerosIndexes) - 1):
        diff = abs(zerosIndexes[i + 1] - zerosIndexes[i] - 1)
        trackones = trackones - diff
        onesAfterZeros.append(trackones)

    sumpassingcars = 0
    for elem in onesAfterZeros:
        sumpassingcars = sumpassingcars + elem
        if sumpassingcars > 10**9:
            return -1

    return sumpassingcars

A = [1,1,0,1]
print(solution(A))