arr = list(map(int, input().split()))
sum_val = 0; avg = 0
arr_one = [] ; arr_two = []

arr_one = arr[1::2]; arr_two = arr[2::3]
sum_val += sum(arr_one)
avg += sum(arr_two)

print(sum_val, f'{avg / len(arr_two):.1f}')
