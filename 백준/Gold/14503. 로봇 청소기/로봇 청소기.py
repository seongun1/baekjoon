import sys
input = sys.stdin.readline

# 방향 정의: 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())  # 로봇 청소기 위치와 초기 방향
arr = [list(map(int, input().split())) for _ in range(n)]

def clean_up(x, y, d):
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    answer = 0  # 청소한 칸의 개수

    while True:
        # 1. 현재 칸이 청소되지 않은 경우 청소
        if arr[x][y] == 0:
            arr[x][y] = 2  # 청소 완료 표시
            answer += 1

        cleaned_or_wall = True  # 4방향 모두 청소되었거나 벽인지 확인
        for _ in range(4):
            d = (d + 3) % 4  # 반시계 방향으로 회전
            nx, ny = x + dx[d], y + dy[d]
            
            # 청소되지 않은 빈 칸이 있을 경우 한 칸 전진
            if in_range(nx, ny) and arr[nx][ny] == 0:
                x, y = nx, ny
                cleaned_or_wall = False
                break
        
        # 2. 4방향이 모두 청소되었거나 벽인 경우
        if cleaned_or_wall:
            # 후진 시도
            back_dir = (d + 2) % 4
            nx, ny = x + dx[back_dir], y + dy[back_dir]
            
            # 후진할 칸이 벽이라면 종료
            if not in_range(nx, ny) or arr[nx][ny] == 1:
                return answer
            
            # 후진할 수 있는 경우 위치 갱신 (청소는 하지 않음)
            x, y = nx, ny

print(clean_up(r, c, d))
