arr = list(map(int, input().split()))
new_arr = []
for i in range(len(arr)):
    if arr[i] == 0:
        new_arr = [elem for elem in arr[:i]]
        break

for j in range(len(new_arr)):
    if new_arr[j] % 2 != 0:
        print(new_arr[j] + 3, end = ' ')
    else:
        print(new_arr[j] // 2 , end = ' ')    

            
      