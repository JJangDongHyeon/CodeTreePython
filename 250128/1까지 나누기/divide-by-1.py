n = int(input())
val = n / 1
cnt = 0
for i in range(1, 100):
   val = val // i
   cnt += 1
   if val <= 1:
    print(cnt)
    break