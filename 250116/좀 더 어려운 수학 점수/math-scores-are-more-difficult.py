arr_a, arr_b = input().split(), input().split()
math_a, eng_a = int(arr_a[0]), int(arr_a[1])
math_b, eng_b = int(arr_b[0]), int(arr_b[1])

if math_a > math_b:
    print('A')
elif math_a < math_b:
    print('B')
elif eng_a > eng_b:
    print('A')
else:
    print('B')