sum = 0
cnt = 0
while True:
    n = int(input())
    
    if n < 20 or n > 29:
        print(f'{sum / cnt:.2f}')
        break
    sum += n
    cnt += 1
