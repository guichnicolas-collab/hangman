import random
import os

# list of words
words = """variable
staircase
elect
read
deliver
grass
king
heavy
avenue
widen
intelligence
floor
elegant
flex
crisis
exotic
train
track
warm
road
seed
past
dish
advice
share
jewel
forest
leftovers
fuss
smell
slump
calm
disco
scramble
loan
bench
discipline
keep
alcohol
stamp
quest
record
screw
anniversary
marble
health
gate
artist
tooth
reliable
notorious
connection
graphic
drag
orange
equation
abundant
courage
swop
response
make
inhabitant
acquisition
museum
hook
even
mechanical
boot
folk
width
nightmare
increase
journal
quote
screen
prisoner
gloom
hostage
admission
auditor
smooth
copyright
cheek
replacement
teach
give
firefighter
spite
deprive
weakness
investment
concert
shake
qualified
canvas
advantage
sunrise
declaration
possible
develop
mourning
mood
confront
oppose
petty
quiet
precede
personal
mess
shine
laundry
arrest
pension
exhibition
shape
application
oral
weak
productive
fine
essential
excuse
television
shaft
warrant
worry
lecture
remember
column
consensus
simplicity
compete
organisation
parameter
calf
proposal
circulation
loot
displace
aluminium
statement
dimension
overall
formation
talkative
suspicion
blame
operational
brainstorm
error
convention
volcano
dawn
manual
trap
honest
mask
rabbit
opponent
woman
extend
ethics
selection
colleague
literacy
paradox
definition
misplace
pack
innovation
descent
technology
court
conductor
possession
approve
baseball
motorcycle
prison
north
coffin
overall
reliable
radical
attitude
blank
cabin
earthquake
abuse
preoccupation
drama
hierarchy
popular
specimen
damage
dismissal
snack
lamp
inquiry
coincidence
jazz
puzzle
hanger
applied
stop
love
refrigerator
absorption
guide
country
pavement
electron
satisfaction
archive
poll
deserve
rice
light
style
robot
calm
negotiation
revenge
epicalyx
blow
pluck
tempt
discovery
gasp
bare
parachute
division
family
drawing
articulate
career
operational
spring
duke
army
wolf
cigarette
connection
craftsman
confront
economics
annual
injection
chop
bland
pyramid
violation
intelligence
function
loop
condition
class
list
tuple
dictionary
building
architecture
engineering
television
telephone
zebra
xylophone
waterpolo
quilt
juice
jelly
jellyfish
jaundice
discombobulated
a
an
the
ice cream
rice cooker
endoplasmic reticulum
grandmother
guacamole
chocolate chip cookie
s'mores
cookies n'cream
why
sly
fly
shy
try
plow
xylophone
jazz
xylem
golgi aparatus
mitochondria
cell
computer
meeting
fluffy
blue
blanket
homophobia
orientation
"""

words = words.split("\n")
blanks = []
guessed = set()
lives = 7
word = random.choice(words)
direct_win = False
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Add as many blanks to the blanks list as letters in the word
for i in range(len(word)):
  # if word[i] == " ":
  if word[i] not in alphabet:
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

