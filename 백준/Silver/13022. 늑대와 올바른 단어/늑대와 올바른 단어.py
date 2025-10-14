import sys

s = sys.stdin.readline().strip()

def is_wolf_word(s: str) -> int:
    i = 0
    n = len(s)
    if n == 0:
        return 0
    # 전체 길이가 4의 배수가 아니면 바로 0 (선택적)
    if n % 4 != 0:
        return 0

    while i < n:
        # 1) w 블록 길이 세기
        if s[i] != 'w':
            return 0
        cnt = 0
        while i < n and s[i] == 'w':
            cnt += 1
            i += 1

        # cnt 만큼 'o' 확인
        for _ in range(cnt):
            if i >= n or s[i] != 'o':
                return 0
            i += 1
        # cnt 만큼 'l' 확인
        for _ in range(cnt):
            if i >= n or s[i] != 'l':
                return 0
            i += 1
        # cnt 만큼 'f' 확인
        for _ in range(cnt):
            if i >= n or s[i] != 'f':
                return 0
            i += 1

    return 1

print(is_wolf_word(s))
