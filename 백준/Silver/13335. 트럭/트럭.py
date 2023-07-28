import sys
input = sys.stdin.readline

n,w,l = map(int,input().split()) #트럭의 갯수, 다리의 길이, 다리의 최대 하중
truck = list(map(int,input().split()))
time =0
bridge =[0] * w
while bridge:
    time +=1
    bridge.pop(0)
    if truck:
        if sum(bridge) + truck[0] <= l:
            bridge.append(truck.pop(0))
        else:
            bridge.append(0)
print(time)