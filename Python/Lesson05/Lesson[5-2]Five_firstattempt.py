def minimalfrompart(p, q, onesIndex, twosIndex, threesIndex, foursIndex):
    for elem in onesIndex:
        if elem >= p and elem <= q:
            return 1
    for elem in twosIndex:
        if elem >= p and elem <= q:
            return 2
    for elem in threesIndex:
        if elem >= p and elem <= q:
            return 3
    for elem in foursIndex:
        if elem >= p and elem <= q:
            return 4

def impactnumber(s):
    if s == 'A':
        return 1
    elif s == 'C':
        return 2
    elif s == 'G':
        return 3
    else:
        return 4

def solution(S, P, Q):
    N = len(S)
    if N == 1:
        return impactnumber(S[0])

    impactSequence = N*[None]
    onesIndex = []; twosIndex = []
    threesIndex = []; foursIndex = []
    impactLengths = 4*[0]
    for i in range(N):
        thisimpact = impactnumber(S[i])
        impactSequence[i] = thisimpact
        if thisimpact == 1:
            onesIndex.append(i)
            impactLengths[0] = impactLengths[0] + 1
        elif thisimpact == 2:
            twosIndex.append(i)
            impactLengths[1] = impactLengths[1] + 1
        elif thisimpact == 3:
            threesIndex.append(i)
            impactLengths[2] = impactLengths[2] + 1
        elif thisimpact == 4:
            foursIndex.append(i)
            impactLengths[3] = impactLengths[3] + 1
    
    for i in range(4):
        if impactLengths[i] == N:
            return i + 1
    
    minImpactSeq = []
    for p, q in zip(P,Q): 
        thismin = minimalfrompart(p,q, onesIndex, twosIndex, threesIndex, foursIndex)
        minImpactSeq.append(thismin)
        
        
    return minImpactSeq


#S = "CAGCCTA"
S = "TT"
P = [2,5,0]
Q = [4,5,6]
P = [0]
Q = [0]
print(solution(S,P,Q))