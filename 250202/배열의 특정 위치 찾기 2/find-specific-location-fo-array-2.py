arr = list(map(int, input().split()))
sum_hol = 0; sum_jjak = 0

for i in range(len(arr)):
    if i % 2 != 0:
        sum_hol += arr[i]
    else:
        sum_jjak += arr[i]
    
if sum_hol > sum_jjak:
    print(sum_hol - sum_jjak)
else:
    print(sum_jjak - sum_hol)
