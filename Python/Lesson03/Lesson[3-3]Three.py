#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(A):
    numberofints = len(A)
    sumsleft = [A[0]]
    sumsright = [A[numberofints - 1]]
    
    for i in range(numberofints - 2):
        sumsleft.append(sumsleft[i] + A[i+1])
        sumsright.append(sumsright[i] + A[numberofints - 2 - i])

    splitsum = []
    for i in range(numberofints - 1):
        diff = sumsleft[i] - sumsright[numberofints - 2 - i]
        absdiff = abs(diff)
        splitsum.append(absdiff)
    
    return min(splitsum)


A = [3,1,2,4,3]
print(solution(A))