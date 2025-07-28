def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    # 1) diff 행렬 생성
    diff = [[beginning[i][j] ^ target[i][j]
             for j in range(m)] for i in range(n)]

    INF = float('inf')
    best = INF

    # row0_flip = 0 or 1 두 가지 경우를 모두 시도
    for row0_flip in (0, 1):
        # 2) diff2는 실제 연산하면서 바뀔 복사본
        diff2 = [row[:] for row in diff]
        flips = row0_flip  # 첫 행을 뒤집었다면 +1

        # (1) 첫 행 뒤집기
        if row0_flip:
            for j in range(m):
                diff2[0][j] ^= 1

        # (2) 열 뒤집기: 이제 diff2[0][j] 가 1인 열은 모두 뒤집는다
        for j in range(m):
            if diff2[0][j] == 1:
                flips += 1
                for i in range(n):
                    diff2[i][j] ^= 1

        # (3) 행 뒤집기: 이제 diff2[i][0] 이 1인 행은 모두 뒤집는다
        for i in range(n):
            if diff2[i][0] == 1:
                flips += 1
                for j in range(m):
                    diff2[i][j] ^= 1

        # (4) 모두 0이 되었는지 확인
        ok = all(diff2[i][j] == 0 for i in range(n) for j in range(m))
        if ok:
            best = min(best, flips)

    return best if best < INF else -1
