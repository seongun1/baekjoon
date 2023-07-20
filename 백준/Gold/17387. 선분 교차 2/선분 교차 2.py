#선분 교차2 교차하면 1을 출력, 아니면 0을 출력. 선분 = 양쪽에 끝나는 점이 있는 직선
import sys
input = sys.stdin.readline
point = []
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

point.append([x1,y1])
point.append([x2,y2])
point.append([x3,y3])
point.append([x4,y4])

def CCW (p1,p2,p3): #신발끈 공식
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0]*p1[1]) - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])

def check_to_cross(p1,p2,p3,p4):
    result =0
    flag  = False
    p123 = CCW(p1,p2,p3)
    p124 = CCW(p1,p2,p4)
    p341 = CCW(p3,p4,p1)
    p342 = CCW(p3,p4,p2)

    if p123 * p124 ==0 and p341 *p342 ==0: # 두 선분이 평행하고 -> A보다 D가 크고, C보다 B가 더 큰 경우
        flag =True
        if min(p1[0],p2[0]) <= max (p3[0],p4[0]) and  min(p3[0],p4[0])<= max (p1[0],p2[0]) and min(p1[1],p2[1]) <= max (p3[1],p4[1]) and min(p3[1],p4[1])<= max (p1[1],p2[1]):
            result = 1
    if p123 * p124 <=0 and p341 * p342 <=0:
        if not flag:
            result =1

    return result

print(check_to_cross(point[0],point[1],point[2],point[3]))