def solution(files):
    tmp = []
    head ='' #HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
    number ='' #NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
    body ='' #NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다. 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
    
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                for j in range (len(number)):
                    if not number[j].isdigit():
                        body = number[j:]
                        number = number[:j]
                        break
                        # head / tail /body 구분하기
                        
                tmp.append([head,number,body])
                head ,number,body = '','',''
                break
    tmp = sorted(tmp, key= lambda x : (x[0].lower(),int(x[1])))
    
                        
    
   
    return [''.join(i) for i in tmp]