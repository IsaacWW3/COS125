# Task 0
# The following code belongs to a game. It is the code which
# deceases a player's health due to damage and prints out a
# message indicating damage taken and if the player is still 
# in action (still playing). The game does not want to display
# negative health values, so any health below zero is set to
# zero.

alive = True
health = 45
damage = 48

health = health - damage

if health <= 0:
    alive = not alive
    health = 0

print(f"{damage} damage taken. Current health: {health}")

if not alive:
    print("You are out of action.")

#  I deleted the second if statement and changed the < to <=