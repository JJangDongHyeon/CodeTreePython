arr = list(map(int, input().split()))
sum_val = 0 ; cnt = 0
for i in arr:
    if i != 0:
        cnt += 1
    elif i == 0:
        break
sum_val = sum(arr[:cnt])
print(f'{sum_val} {sum_val / cnt :.1f}')
