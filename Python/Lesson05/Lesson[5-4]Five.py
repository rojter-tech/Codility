def solution(A, B, K):
    rangefits = int((B - A)/K)
    firstelemrest = A%K
    lastelemrest = B%K

    if firstelemrest == 0 or lastelemrest == 0:
        return rangefits + 1
    else: 
        if lastelemrest < firstelemrest:
            return rangefits + 1
        else:
            return rangefits


shift = 0
A = 101  + shift
B = 123456789 + shift
K = 10000
print(solution(A, B, K))

# 12345
shift = 0
A = 101  + shift
B = 123456789 + shift
K = 10000