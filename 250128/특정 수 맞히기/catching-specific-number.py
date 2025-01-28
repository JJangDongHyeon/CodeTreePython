while True:
    n = int(input())
    if n < 25:
        print('Higher')
        continue
    elif n > 25:
        print('Lower')
        continue
    else:
        print('Good')
        break
    