def solution(bandage, health, attacks):
    answer = 0
    max_seconds = attacks[-1][0]
    
    max_health = health #최대 체력
    heal_seconds  =0 # 연속으로 힐 한 시간
    for seconds in range(1,max_seconds+1):
        can_heal = True
        for a in attacks:
            if seconds == a[0]: #몬스터가 공격하는 시간이 있다면
                health -= a[1] # 대미지 만큼 대미지를 받는다.
                heal_seconds =0
                can_heal = False #힐을 하지 못하고 다음 초로 넘어간다.
                
                
        if health <=0: #체력이 0 밑으로 떨어지면 게임 종료하며 return -1
            return -1
        
        #print(seconds,health)
        if can_heal: #힐을 할 수 있는 시간(몬스터에게 대미지를 안받는 시간)
            if max_health > health: #체력이 최대 체력보다 작다면 힐을 한다.
                health += bandage[1]
                heal_seconds +=1
            if heal_seconds >= bandage[0]: #시전 시간을 넘어간다면, 추가 힐
                health += bandage[2]
                heal_seconds =0 #연속 힐 시간 초기화

            if max_health < health:
                health = max_health

    
    return health