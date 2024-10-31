scores = [int(input()) for _ in range(5)] 

min_scores = [max(score, 40) for score in scores]

average_score = sum(min_scores)

print(average_score)
