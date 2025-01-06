import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr =[list(map(int,input().split())) for _ in range(n)]
    arr.sort()
    min_interview_rank = 100001
    cnt = []
    for paper_rank , interview_rank in arr:
        if min_interview_rank > interview_rank:
            cnt.append((paper_rank,interview_rank))
            min_interview_rank = interview_rank
    print(len(cnt))
