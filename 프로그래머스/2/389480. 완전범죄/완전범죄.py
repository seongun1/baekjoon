def solution(info, n, m):
    # info: list of (a_i, b_i)
    INF = 10**12

    total_b = sum(b for _, b in info)
    B = total_b

    # 필요량 계산: sum_selected_b > need  <=> need = total_b - m
    need = total_b - m

    # 빠른 처리: 이미 total_b < m 이라면 b 조건은 만족
    if need < 0:
        # 아무것도 훔치지 않아도 b_remaining < m 이므로 a = 0 이 가능하면 0 반환
        return 0 if 0 < n else -1

    # dp[w] = 최소 a 합으로 정확히 w의 b 를 얻음
    dp = [INF] * (B + 1)
    dp[0] = 0

    for a_i, b_i in info:
        # 뒤에서부터 갱신 (0/1 knapsack)
        # 범위를 B..0으로 두면 모든 w에 대해 검사 가능
        for w in range(B, -1, -1):
            if dp[w] == INF:
                continue
            nw = w + b_i
            if nw > B:
                nw = B
            if dp[nw] > dp[w] + a_i:
                dp[nw] = dp[w] + a_i

    # 이제 w >= need+1 (정수 엄격 부등호 때문에) 중 dp[w]가 최소인 값을 찾음
    target = need + 1
    if target > B:
        # 필요량이 B 초과면 불가능
        return -1

    ans = INF
    for w in range(target, B + 1):
        if dp[w] < ans and dp[w] < n:  # a < n 조건도 만족해야 함
            ans = dp[w]

    return ans if ans != INF else -1
