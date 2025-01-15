arrA = input().split()
arrB = input().split()

mathA, engA = int(arrA[0]), int(arrA[1])
mathB, engB = int(arrB[0]), int(arrB[1])

if mathA > mathB and engA > engB:
    print(1)
else:
    print(0)