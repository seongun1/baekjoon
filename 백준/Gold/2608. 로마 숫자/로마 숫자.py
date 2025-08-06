import sys
input =sys.stdin.readline

arr = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
rom = list(arr.keys())
#print(rom)
val = list(input().strip() for _ in range(2))
#print(val)   
def rom_to_val(rom):
    val = 0
    ran = len(rom)
    for i, ch in enumerate(rom):
        char = arr[ch]
        if i+1 < ran and char < arr[rom[i+1]]:
            val -= arr[rom[i]]
        else:
            val += arr[rom[i]]
    return val

num_list = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def val_to_rom(num):
    ans =[]
    idx = 0
    while (num !=0):
        if not num //num_list[idx][0]:
            idx +=1
            continue
        count = num // num_list[idx][0]
        num %= num_list[idx][0]
        ans.append(num_list[idx][1] * count)
    return ''.join(ans)
        

ans_int = 0
for v in val:
    ans_int += rom_to_val(v)
print(ans_int)
print(val_to_rom(ans_int))