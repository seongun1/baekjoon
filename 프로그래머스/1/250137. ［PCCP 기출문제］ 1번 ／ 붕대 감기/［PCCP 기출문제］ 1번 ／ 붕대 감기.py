def solution(bandage, health, attacks):
    answer = 0
    tmp = attacks[:]
    tmp.sort(key = lambda x : x[0],reverse = True)
    max_time = tmp[0][0]
    #print('max_time',max_time)
    max_health = health
    heal_time =0 #연속 힐 시간
    attack_time =0 #공격 시간
    for time in range(1,max_time+1):
        if time == attacks[attack_time][0]: #몬스터가 공격하는 시간이라면 = 데미지 받고, 연속 힐 시간 초기화
            health -= attacks[attack_time][1]
            heal_time =0
            attack_time = min(len(attacks) -1 , attack_time +1 )
        else: #몬스터 공격 안하는 시간 = 힐 하고, 연속 힐 시간 +1
            health = min(max_health, health + bandage[1])
            heal_time +=1
        if health <= 0: #만약 죽는다면 -> -1 return
            return -1
        if heal_time >= bandage[0]: #연속 힐 시간이 시전 시간을 넘는다면 = 추가 회복량, 시전 시간 초기화
            health = min(max_health , health + bandage[2])
            heal_time =0
        #print(time,health)
    return health
            
    return answer