import os
os.system('cls')
win=float(input("Enter the win match:"))
lose=float(input("Enter the lose match:"))
draw=float(input("Enter the draw match:"))
total_game=win+lose+draw
percenage_of_won=(win*100)/total_game
percenage_of_lose=(lose*100)/total_game
percenage_of_draw=(draw*100)/total_game
print("Total games:",total_game)
print("Percentage of game won",percenage_of_won)
print("Percentage of game lose",percenage_of_lose)
print("Percentage of game draw",percenage_of_draw)