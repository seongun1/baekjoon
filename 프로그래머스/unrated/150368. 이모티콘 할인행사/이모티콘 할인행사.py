discounts = [10,20,30,40] #할인율
answer =[-1.-1]
def solution(users, emoticons):
   
    n,m = len(users),len(emoticons)
    discounts_list = [0] * m

    def search (k): #이모티콘의 할인율과, 가격을 각각 비교함
        global answer
        if k == m:
            plus_people,sales_amount = 0, 0 #이모티콘 플러스에 가입한 사람, 이모티콘 판매액을 늘린 판매액
            for i in range (n):
                sales =0
                for j in range(m):
                    if users[i][0] <= discounts_list[j]:
                        sales += emoticons[j] * (100-discounts_list[j]) // 100
                if sales >= users[i][1]:
                    plus_people +=1
                else:
                    sales_amount +=sales
            if plus_people > answer[0] or plus_people == answer[0] and sales_amount > answer[1]:
                answer= [plus_people,sales_amount]
            return
        for i in range (4):
            discounts_list[k] = discounts[i]
            search(k+1)
                        
    search(0)

    return answer