import sys

s = sys.stdin.readline().rstrip('\n')
bomb = sys.stdin.readline().rstrip('\n')
blen = len(bomb)

stack = []
last_char = bomb[-1]  # 마지막 문자로 빠르게 체크

for ch in s:
    stack.append(ch)
    # 마지막 문자와 같을 때만 비교 수행 -> 불필요한 슬라이스 줄임
    if ch == last_char and len(stack) >= blen:
        # 스택의 끝부분이 bomb인지 확인
        if ''.join(stack[-blen:]) == bomb:
            # 같으면 제거
            del stack[-blen:]


print(''.join(stack) if stack else "FRULA")
