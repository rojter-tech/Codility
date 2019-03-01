def bracketrecurs(S):

    pos = 0
    str_concat = ""
    if len(S) == 0:
        return "1"
    else:
        for elem in S:
            nextpos = pos + 1
            tail = bracketrecurs(S[nextpos:])
        
            if elem != '(' and elem != ')':
                str_concat += elem
            if elem == '(' or elem == ')':
                if str_concat == "":
                    str_concat = "1"
                return str(float(str_concat) * float(bracketrecurs(tail)))
        
            pos += 1
    
    return S

#(1(1(1)))
#1(1(1)))
#1(1)))
#1)))
#))
#)
#

if __name__ == "__main__":
    S = "(1(1(1)2)1)3"
    print(bracketrecurs(S))
    S2 = 4*S
    print(S2)

