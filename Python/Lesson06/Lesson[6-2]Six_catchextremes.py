import random

def solution(A):
    oor = 10**3 + 1
    maxThree = 3*[-oor]
    minTwo = 2*[oor]

    for elem in A:
        if elem >= maxThree[0]:
            maxThree[2] = maxThree[1]
            maxThree[1] = maxThree[0]
            maxThree[0] = elem
        elif elem >= maxThree[1]:
            maxThree[2] = maxThree[1]
            maxThree[1] = elem
        elif elem >= maxThree[2]:
            maxThree[2] = elem
        
        if -elem >= -minTwo[0]:
            minTwo[1] = minTwo[0]
            minTwo[0] = elem
        elif -elem >= -minTwo[1]:
            minTwo[1] = elem
    
    maxval = maxThree[1]*maxThree[2]
    top = maxThree[0]
    maxval *= top
    minval = minTwo[0]*minTwo[1]*top

    return max(maxval,minval)

N = 50000
A1 = N*[-1]
A2 = N*[1]
A = A1 + A2
print(solution(A))