n = int(input())
sum, cnt = 0, 0
for i in range(n):
    n = int(input())
    sum += n
    cnt += 1
avg = sum / cnt
print(sum, end = ' ')
print(f'{avg:.1f}')