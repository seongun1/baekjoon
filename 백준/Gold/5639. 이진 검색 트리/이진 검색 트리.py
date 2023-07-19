import sys

#전위 순회 = 루트 - 왼 - 오 // 후위 순회 = 왼 - 오 - 루트
sys.setrecursionlimit(10**6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postorder (first,end):
    if first > end :
        return
    mid = end +1
    for i in range(first+1,end+1):
        if num_list[first] < num_list[i]:
            mid = i
            break
    postorder(first +1 , mid -1)#재귀함수로써 왼쪽부분을 완성
    postorder(mid,end) # 오른쪽 부분을 완성
    print(num_list[first])

postorder(0,len(num_list)-1)