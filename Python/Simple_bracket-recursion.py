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
                multiply = int(float(str_concat))
                numbertail = int(bracketrecurs(tail))
                multistring = str(multiply * numbertail)
                return multistring
        
            pos += 1
    
    return S

if __name__ == "__main__":
    S = "(2(3))"
    print(bracketrecurs(S))
    S2 = 4*S
    #print(S2)

