arr = input().split()
a, b = int(arr[0]), int(arr[1])
sum, avr, cnt = 0, 0, 0
for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i 
        cnt += 1
    
avr = sum / cnt
print(sum, end = " ")
print(f'{avr:.1f}')