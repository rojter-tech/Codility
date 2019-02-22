def solution(X, Y, D):
    interval = Y - X
    stepfromborder = interval%D
    if stepfromborder == 0:
        return int(interval/D)
    else:
        return int(interval/D + 1)

X = 3
Y = 11
D = 3

print(solution(X, Y, D))