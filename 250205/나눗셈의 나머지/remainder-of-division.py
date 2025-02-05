arr = list(map(int, input().split()))

result = [0 for _ in range(10)]
a = arr[0] # 1000
b = arr[1] # 4
while True:
    digit = a % b
    a = a // b
    result[digit] += 1
    if a <= 1:
        break
sum = 0;count = 0
for _ in result:
    count += 1 

for i in range(count):
    sum += result[i] ** 2
print(sum)