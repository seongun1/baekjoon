import sys
from collections import deque

# --- 함수 정의 부분 ---

def check_bell(ground_do, ground_su):
    """종을 칠 수 있는지 확인하고 승자를 반환합니다."""
    # 도도 승리 조건: 그라운드에 5가 있을 때
    if (ground_do and ground_do[-1] == 5) or (ground_su and ground_su[-1] == 5):
        return 'do'
    # 수연 승리 조건: 그라운드 합이 5일 때
    elif (ground_do and ground_su) and (ground_do[-1] + ground_su[-1] == 5):
        return 'su'
    return None # 종을 칠 수 없으면 None 반환

def collect_cards(winner, do_deck, su_deck, ground_do, ground_su):
    """승자가 그라운드의 카드를 모두 덱으로 가져갑니다."""
    if winner == 'do':
        do_deck.extendleft(ground_su)
        do_deck.extendleft(ground_do)
    else: # winner == 'su'
        su_deck.extendleft(ground_do)
        su_deck.extendleft(ground_su)
    
    ground_do.clear()
    ground_su.clear()

# --- 메인 로직 시작 ---

input = sys.stdin.readline
n, m = map(int, input().split())

# 덱 초기화
do_deck = deque()
su_deck = deque()
for _ in range(n):
    a, b = map(int, input().split())
    do_deck.append(a)
    su_deck.append(b)

ground_do = deque()
ground_su = deque()

# 게임 진행 루프
for turn in range(m):
    # 1. 카드를 냅니다. (플레이어 결정 및 카드 옮기기)
    if turn % 2 == 0: # 도도 턴
        ground_do.append(do_deck.pop())
    else: # 수연 턴
        ground_su.append(su_deck.pop())

    # 2. 카드를 낸 직후 덱이 비면 즉시 종료합니다.
    if not do_deck or not su_deck:
        break

    # 3. 종을 칠 수 있는지 확인하고, 쳤다면 카드를 모읍니다.
    bell_winner = check_bell(ground_do, ground_su)
    if bell_winner:
        collect_cards(bell_winner, do_deck, su_deck, ground_do, ground_su)

# --- 최종 승패 판정 ---

# 루프가 끝난 이유가 덱이 비어서인지 확인
if not do_deck:
    print('su')
elif not su_deck:
    print('do')
else: # M번의 턴을 모두 진행한 경우
    if len(do_deck) > len(su_deck):
        print('do')
    elif len(su_deck) > len(do_deck):
        print('su')
    else:
        print('dosu')