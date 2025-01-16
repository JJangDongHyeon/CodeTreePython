arr = input().split()
middle, final = int(arr[0]), int(arr[1])

if (middle >= 90) and final >= 95:
    print(100000)
elif (middle >= 90) and final >= 90:
    print(50000)
else:
    print(0)