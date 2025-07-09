#Exercise 2:
"""
Find the top 3 students with the highest scores and print their names and
scores.

"""
import os
os.system('cls')
scores = {
 'Alice': 85, 'Bob': 92, 'Charlie': 78,
 'David': 90, 'Eve': 88, 'Frank': 95, 'Grace': 80
}
# # lambda arguments: expression
#lambda item: item[1] mean:
#For every tuple in the list, return the second value (which is the score) — that’s what we’ll use to sort.
top_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
#Sorted will make things in dict become tuple
top_3 = top_scores[:3]
for name, score in top_3:
    print(f"{name}: {score}")