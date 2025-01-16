a, b = float(input()), float(input())

if 1.0 <= a and 1.0 <= b:
    print('High')
elif 0.5 <= a and 0.5 <= b:
    print('Middle')
else:
    print('Low')