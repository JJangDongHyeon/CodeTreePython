n = int(input())

# Write your code here!

for i in range(n):
    for j in range((n - i) - 1):
        print(' ', end = '')
    for j in range((i * 2) + 1):
        print('*', end = '')
    print()

for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end = '')
    for j in range(n - (i * 2)):
        print('*', end = '')
    print()