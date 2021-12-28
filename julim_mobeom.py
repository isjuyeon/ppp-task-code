def Solution(S,T):
    index=-1
    for i in S:#S에 있는 걸 다 찾으면 되니까 for문의 범위는 S이다.이게 진짜 대박이라고 생각함. 몇번을 돌리냐가 아니라 정말 다 털어야될 것은 뭔지!
        if i not in T:
            return -1#for i in S를 병렬로 분리해서 적었을 것 같은데 어차피 둘다 in S이면 정말 잘 짠 코드.
        while(True):
            index += 1
            #무조건 index는 추가 되어야 한다.index가 늘여진 총 길이이다.#if문이 위에 있으면
            if i==T[index%len(T)]:#이거 위로만 반복된다. break가 되면 for문의 원소가 넘어간다.
                break
    return index//len(T)+1
#index=0
#if i~다음에 index+=1은 틀렸음. 매번 +=1되는게 아니니까.
print(Solution('caa','cac'))