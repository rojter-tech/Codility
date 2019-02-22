import heapq as que

def solution(A):
    minVal = []
    maxVal = []
     
    for elem in A:
        if len(minVal) < 2:
            que.heappush(minVal, -elem)
        else:
            que.heappushpop(minVal, -elem)
             
        if len(maxVal) < 3:
            que.heappush(maxVal, elem)
        else:
            que.heappushpop(maxVal, elem)
    
    maxval = que.heappop(maxVal) * que.heappop(maxVal)
    top = que.heappop(maxVal)
    maxval *= top
    minval = que.heappop(minVal) * que.heappop(minVal) * top

    return max(maxval, minval)

N = 50000
A1 = N*[-1]
A2 = N*[1]
A = A1 + A2
print(solution(A))