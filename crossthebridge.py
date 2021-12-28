def Solution(N,L,M,W):
    bridge,c=[0]*L,0
    while W!=[]:#이렇게 풀면 while문이 다 돌고난 다음에 i가 들어가는거기때문에 반박자 늦다. 예로 최대하중때문에 한개만 들어가는 상황이랑 두개 다 들어가는 상황
        c+=1
        bridge.pop(0)#처음과 끝 모두에서 예외가 없다.
        if W[0] + sum(bridge) <= M:
            # bridge.pop(0)
            bridge.append(W.pop(0))
        else:
            # bridge.pop(0)
            bridge.append(0)
    return c+L
#가장 깔끔한 코드.

print(Solution(3,2,8,[5,3,7]))