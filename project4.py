i = int(input())
counter = 0
while i != 1:
   counter = counter + 1
   if i % 2 == 0:
       i = i /2
   elif i % 2 != 0:
       i = i * 3 + 1
print(counter)        




#Get random numbers for the dice 
import random


# make players score zero to start
player1_score = 0
player2_score = 0


# roll the dice 15 times
for i in range(15):


   #random numbers between 1 and 6 for each player.
   player1_value = random.randint(1, 6)
   player2_value = random.randint(1, 6)


   # showed the nuber he dice rolled on 
   print("Player 1 rolled: ", player1_value)
   print("Player 2 rolled: ", player2_value)


   # Selection: based on comparison of the values, take the appropriate path through the code.
   if player1_value > player2_value:
       print("player 1 wins.")
       player1_score = player1_score + 1  # This is how we increment a variable
   elif player2_value > player1_value:
       print("player 2 wins")
       player2_score = player2_score + 1
   else:
       print("It's a draw")


   input("Press enter to continue.")  # Wait for person input to proceed.


print("### Game Over ###")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)
