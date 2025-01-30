n = int(input())
a = 0 
for i in range(n * 2):
    if i % 2 == 0 :
        for j in range((i // 2) + 1):
            print('*', end = ' ')
        print()
    else:
        for j in range(n - a):
            print('*', end = ' ' )
        print()
        a += 1