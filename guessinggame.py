
import random  #importing the random module

print("Hello there! this is a guessing game created by AOV")


userName = input("Please enter a username: \n") #Assignment of player's name to the variable userName

print("Your username has been saved as " + userName)
print("Lets begin " + userName)

secretNumber = random.randint(1, 10)   #Assigning a random int to this variable

while True:       #
  guess = int(input("guess the secret number from 1 - 10: "))

  if guess == secretNumber:              #comparing user's guess and the secretNumber using, not-equal-to
    print("Congratulations!! You are correct")

    break

  elif guess == 0:                        #Comparing 'guess' with 0. Zero is not a valid number in this game
      print(userName + ", you are better than this, 0 is not a valid number in this game")

  elif guess >= 8 :
      print("Your guess is too high, try something lesser")

  elif guess <= 4:
      print("You are almost there, try a higher number")

  else: 
      print("Wrong answer")

  

print("""Now let's try something more fun!
You're welcome to level 2""")

    

#This is where level 2 begins
#complete the following words

print("Complete the following words to score higher")

userInput = ""

while True:
   userInput = input("input the missing letters 'Prof******al : \n")
   userInput = userInput.lower() #converts whatever string the user inputs to lowercase and reassigns to userInput
   
   if userInput == "ession": #compares the user input
      print("Oh! thank goodness I thought you would fail. You are correct")

      print("You have completed the 2 stages of this boring game successfully")

      break

   else:
      print("Wrong answer, you need to learn your spellings. Try again")
