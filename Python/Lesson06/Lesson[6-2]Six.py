import itertools as gen

def maxtripleprod(elemcombo):
    combolen = len(elemcombo)
    productsList = combolen*[None]
    for i in range(combolen):
        thisproduct = elemcombo[i][0]*elemcombo[i][1]*elemcombo[i][2]
        productsList[i] = thisproduct
    return max(productsList)

def solution(A):
    n = len(A)
    if n > 6:
        sortedA = sorted(A)
        topbottom = 6*[0]
        for i in range(3):
            topbottom[i] = sortedA[n-1-i]
            topbottom[6-1-i] = sortedA[i]
        elemcombo = list(gen.combinations(topbottom, 3))
    else:
        elemcombo = list(gen.combinations(A, 3))

    return maxtripleprod(elemcombo)


N = 50000
A1 = N*[-1]
A2 = N*[1]
A = A1 + A2
print(solution(A))