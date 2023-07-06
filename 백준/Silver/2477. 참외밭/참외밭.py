import sys
input = sys.stdin.readline

k=int(input()) # 1m^2의 넓이에 자라는 참외의 갯수 = k
index =[list(map(int,input().split()))for _ in range(6)]

#제일 긴 가로에 각각 붙어있는 양 옆의 세로를 빼면, 우리가 빼야 할 세로값이 구해진다.
w_max =0 ;w_index =0
h_max =0 ;h_index =0
#최대 변 구하기
for i in range (6):
    if index[i][0] == 1 or index[i][0] ==2:
        if w_max<index[i][1]:
            w_max = index[i][1]
            w_index = i
    elif index[i][0] == 3 or index[i][0] == 4:
        if h_max < index[i][1]:
            h_max = index[i][1]
            h_index = i

w_sub = abs(index[(h_index-1)%6][1]-index[(h_index+1)%6][1])
h_sub = abs(index[(w_index-1)%6][1]-index[(w_index+1)%6][1])
result =(w_max * h_max -w_sub * h_sub) * k
print(result)