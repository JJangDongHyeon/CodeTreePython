n = int(input())
a = n - 1
result = 0
c = False

while True:
    if a <= 1:
        break
    result = n % a
    if result == 0:  
        c = True
        break
    elif result != 0:
        c = False
    a -= 1
    

if c == True:
    print('C')
else:
    print('N')