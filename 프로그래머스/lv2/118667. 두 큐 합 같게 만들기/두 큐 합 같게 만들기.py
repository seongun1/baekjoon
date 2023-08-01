from collections import deque

def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que1_sum = sum(que1)
    que2 = deque(queue2)
    que2_sum = sum(que2)
    target = sum(que1) + sum(que2)
    limit = 4 * len(que1)
    while(1):
        tmp =0
        if target %2 ==1:
            return -1
        if answer == limit:
            return -1
        if que1_sum < que2_sum:
            tmp = que2.popleft()
            que1.append(tmp)
            que1_sum += tmp
            que2_sum -= tmp
            answer +=1 
        elif que2_sum < que1_sum:
            tmp = que1.popleft()
            que2.append(tmp)
            que2_sum += tmp
            que1_sum -= tmp
            answer +=1
        else:
            return answer
        
    