arr = list(map(int, input().split()))
result_arr = []
sum_val = 0; cnt = 0
for i in arr:
    if i != 0:
        if i % 2 == 0:
            result_arr.append(i)
    else:
        break
sum_val = sum(result_arr) ; cnt = len(result_arr)

print(cnt, sum_val)
