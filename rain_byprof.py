def solution(l):
    def make_shade(bricks):
        for i in range(len(bricks)-1):
            if bricks[i]>bricks[i+1]:
                bricks[i+1]=bricks[i]
        return bricks
    left_view=make_shade(l[:])
    right_view=make_shade(l[::-1])[::-1]
    overlap=[min(i,j) for i,j in zip(left_view,right_view)]
    answer=sum([i-j for i,j in zip(overlap,l)])

    return answer

print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))