arr_a = input().split()
arr_b = input().split()
arr_c = input().split()

symptoms_a, symptoms_b, symptoms_c  = arr_a[0], arr_b[0], arr_c[0]
temperature_a, temperature_b, temperature_c = int(arr_a[1]), int(arr_b[1]), int(arr_c[1])

count = 0

if (symptoms_a == 'Y' and temperature_a >= 37):
    count += 1
if (symptoms_b == 'Y' and temperature_b >= 37):
    count += 1
if (symptoms_c == 'Y' and temperature_c >= 37):
    count += 1

if count >= 2:
    print('E')
else:
    print('N')