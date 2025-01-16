arr_1, arr_2 = input().split(), input().split()
age_1, age_2 = int(arr_1[0]), int(arr_2[0])
gender_1, gender_2 = arr_1[1], arr_2[1] 

if (age_1 >= 19 and gender_1 == 'M') or (age_2 >= 19 and gender_2 == 'M'):
    print(1)
else:
    print(0)