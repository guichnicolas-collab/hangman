import random
import os
import string
from words import words

blanks = [] # list of blanks to be filled in with the word
guessed = set() # set of guessed letters
lives = 7 # number of lives
word = random.choice(words) # random word from the list
direct_win = False # flag for direct win
alphabet = string.ascii_lowercase # alphabet

# Add as many blanks to the blanks list as letters in the word
for i in range(len(word)):
  if word[i] not in alphabet or word[i] == " ":
    blanks.append(word[i])
    continue
  blanks.append("_")

# Func for displaying hangman
def hangman(lives):
  if lives == 7:
    print("____")
    print("|  |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("---")
  elif lives == 6:
    print("____")
    print("|  |")
    print("|  0")
    print("|")
    print("|")
    print("|")
    print("---")
  elif lives == 5:
    print("____")
    print("|  |")
    print("|  0")
    print("| <")
    print("|")
    print("|")
    print("---")
  elif lives == 4:
    print("____")
    print("|  |")
    print("|  0")
    print("| < >")
    print("|")
    print("|")
    print("---")
  elif lives == 3:
    print("____")
    print("|  |")
    print("|  0")
    print("| <|>")
    print("|")
    print("|")
    print("---")
  elif lives == 2:
    print("____")
    print("|  |")
    print("|  0")
    print("| <|>")
    print("|  |")
    print("|")
    print("---")
  elif lives == 1:
    print("____")
    print("|  |")
    print("|  0")
    print("| <|>")
    print("|  |")
    print("| ( ")
    print("---")
  elif lives == 0:
    print("____")
    print("|  |")
    print("|  0")
    print("| <|>")
    print("|  |")
    print("| ( )")
    print("---")

# Func for printing everything in the board
def print_main():
  os.system('cls' if os.name == 'nt' else 'clear')
  hangman(lives)
  print("Guessed letters: " + " ".join(guessed))
  print()
  print(" ".join(blanks))

# Func for checking if guess is acceptable
def validate(guess):
  # If any or these conditions are true, return false as an invalid guess
  if guess == "give up":
    print("The word was " + word + ".")
    exit(0)
  if len(guess) == len(word):
    return True
  if len(guess) != 1:
    if len(guess) > 1:
      print("Too many letters!")
    else:
      print("Empty guess!")
    return False
  elif guess in guessed:
    print("Letter already guessed!")
    return False
  elif guess.isdigit():
    print("Invalid guess!")
    return False
  elif guess not in alphabet:
    print("Not in alphabet!")
    return False
  # If none of them are true, return true as a valid guess
  return True

# loop until we die or win
while lives > 0 and "_" in blanks:
  # display the tiles, lives, and guessed letters
  print_main()
  
  # get valid player guess
  flag = True
  while flag:
    guess = input("Enter your guess: ").lower()
    if validate(guess):
      flag = False
  if len(guess) == 1:
    guessed.add(guess)
      
  
  # if they attempted to guess the entire word at once check if they got it right
  if len(guess) == len(word):
    if guess == word:
      direct_win = True
      for i in range(len(word)):
        blanks[i] = word[i]
      break
    else:
      # if they fail, they die immediately
      break
  
  # if they guessed only a single letter, place it where it appears in the word
  elif guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        blanks[i] = guess
        
  # otherwise, take away a life
  else:
    lives -= 1

else:
  # when the loop ends (without breaking), meaning they guessed the word letter by letter
  print_main()
  if lives == 0:
    print("Sorry, you lost. The word was " + word + ".")
  else:
    print("Good Job!")
  exit(0)

# when the loop is stopped by a break statement
print_main()
if direct_win:
  print("Good Job!")
else:
  print("Sorry, you lost. The word was " + word + ".")

