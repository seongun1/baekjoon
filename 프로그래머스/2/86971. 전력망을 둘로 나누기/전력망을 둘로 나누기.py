def solution(n, wires):
    answer = n
    
    for i in range(len(wires)):
        tmp = wires.pop(0)
        arr1 = []
        arr2 = []
        arr3 = []
        arr1.append(tmp[0])
        arr2.append(tmp[1])
        print(wires)
        for w in wires:
            a,b = w[0],w[1]
            if a in arr1 or b in arr1:
                arr1.append(a)
                arr1.append(b)
            elif a in arr2 or b in arr2:
                arr2.append(a)
                arr2.append(b)
            else:
                arr3.append([a,b])
        while(arr3):
            x,y = arr3.pop(0)
            success = False
            if x in arr1 or y in arr1:
                arr1.append(x)
                arr1.append(y)
                success = True
            elif x in arr2 or y in arr2:
                arr2.append(x)
                arr2.append(y)
                success = True
            if not success:
                arr3.append([x,y])
            
        #중복제거
        arr1 = list(set(arr1))
        arr2 = list(set(arr2))
        #print(arr1,arr2)
        answer = min(answer,abs(len(arr1) - len(arr2)) )
        wires.append(tmp)
        
    return answer