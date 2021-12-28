def solution(s):
    l,r,length=0,0,0
    for i in s:
        if i=='(':
            l+=1
        else:
            r+=1
        if r>l:
            l, r= 0, 0
        elif r==l:
            length=max(length,l*2)
    l, r= 0, 0
    for i in s[::-1]:
        if i == '(':
            l += 1
        else:
            r += 1
        if r < l:
            l, r= 0, 0
        elif r == l:
            length = max(length, l * 2)
    return length
print(solution(")()())"))