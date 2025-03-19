import sys

input = sys.stdin.readline

n = int(input())
num = int(input())

arr = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]  # 위, 오른쪽, 아래, 왼쪽
dy = [0, 1, 0, -1]
ans_x, ans_y = 0, 0

x, y = n // 2, n // 2  # 중앙에서 시작
arr[x][y] = 1

if num == 1:
    ans_x, ans_y = x + 1, y + 1

count = 2
dir_idx = 0  # 방향 인덱스
step = 1  # 한 방향으로 이동할 칸 수

while count <= n * n:
    # 같은 방향으로 step만큼 이동하기
    for _ in range(step):
        x += dx[dir_idx]
        y += dy[dir_idx]
        
        if not (0 <= x < n and 0 <= y < n):  # 범위 체크
            break
            
        arr[x][y] = count
        
        if count == num:
            ans_x, ans_y = x + 1, y + 1
            
        count += 1
        
        if count > n * n:
            break
    
    # 방향 전환
    dir_idx = (dir_idx + 1) % 4
    
    # 두 방향(위+오른쪽 또는 아래+왼쪽)으로 이동한 후에 step 증가
    if dir_idx % 2 == 0:
        step += 1

for row in arr:
    print(*row)
print(ans_x, ans_y)