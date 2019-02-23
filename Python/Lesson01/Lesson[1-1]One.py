#BinaryGap
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(N):
    thebinary = bin(N)
    j = 0
    onesposition = []
    for i in thebinary:
        if i == '1':
            onesposition.append(j)
        j = j + 1
    
    oneslength = len(onesposition)
    gaps = []
    if oneslength > 1:
        for i in range(oneslength - 1):
            gaps.append(onesposition[i + 1] - onesposition[i] - 1)
    else:
        return 0

    return max(gaps)

N = 529
B = solution(N)
print(B)