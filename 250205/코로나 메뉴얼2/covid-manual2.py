result = [0 for i in range(4)]

for i in range(3):
    arr = input().split()
    
    if arr[0] == 'Y' and int(arr[1]) >= 37:
        result[0] += 1

    elif arr[0] == 'N' and int(arr[1]) >= 37:
        result[1] += 1

    elif arr[0] == 'Y' and int(arr[1]) <= 37:
        result[2] += 1
        
    elif arr[0] == 'N' and int(arr[1])<= 37:
        result[3] += 1    
    
for k in result:
    print(k, end = ' ')
if result[0] >= 2:
    print('E')
