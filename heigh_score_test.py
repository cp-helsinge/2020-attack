from game_objects import global_heighscore

# Set a global key for this specific game
heighscore_key = 'fgj25jd8cack5fdfd9t'

# Create a heigh score object
heighscore = global_heighscore.GlobalHeighscore(heighscore_key)

# Set a new heigh score
heighscore.set("Carl",240)

# Print heigh score list
print("\n+ Heighscore: " + "-" * 27 + "+"  )
rank = 1
for i in heighscore.list:
    print("| {:>4} | {:<20} | {:>8} |".format( rank , i['name'], i['score']))
    rank += 1 
print("+" + "-" * 40 + "+"  )

# Update heigh score list (updated on creation of object)
# heighscore.get()
 