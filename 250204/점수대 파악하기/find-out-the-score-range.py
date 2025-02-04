scores = list(map(int, input().split()))
scores = scores[:scores.index(0)]

score_counts = [0] * 11

for score in scores:
    score_counts[score // 10] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {score_counts[i]}")
