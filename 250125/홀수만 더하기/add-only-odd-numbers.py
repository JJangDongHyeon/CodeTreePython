sum = 0
n = int(input())
for i in range(n):
    n = int(input())
    if n % 2 != 0 and n % 3 == 0:
        sum += n
print(sum)  