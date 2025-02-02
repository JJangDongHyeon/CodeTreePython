n = int(input())

arr = list(map(float, input().split()))
avg_sum = 0
for i in range(n):
    avg_sum += arr[i]

avg = avg_sum / len(arr)

print(f'{avg:.1f}')
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')