import random
### Game Art
Rock ="""
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
### variables
cpuScore = 0
playerScore = 0
tieScore = 0
possibilities = [Rock,Paper,Scissors]
### Input amount of rounds if a string is entered, it will repeat the question 
print("="*40)
while True:
  try:
    rounds = int(input("How many rounds do you want to play? "))
    break
  except ValueError:
    print("Enter a valid number!")
print("="*40)


### Main Game Loop
def _main_(playerScore,cpuScore,tieScore, rounds):
  while rounds > 0:
    
    ### Generate computer pick
    computer = random.choice(possibilities)
    ### Player Input
    while True:
      player = input("Pick a hand. Rock, Paper, or Scissors: ").lower()
      if(player == "rock" or player == "paper" or player == "scissors"):
        if player == "rock":
          player = Rock
        if player == "paper":
          player = Paper
        if player == "scissors":
          player = Scissors
        break
      else:
        print("="*40)
        print("Invalid input. Try again.")
        print("="*40)

    ### Print results
    print("-"*40)
    print("Your hand: ", player)
    print("Cpu hand: ", computer)
    print("-"*40)
    result = checkForWinner(player, computer)
    if(result == "Player"):
      playerScore += 1
      rounds -= 1
    elif(result == "Cpu"):
      cpuScore += 1
      rounds -= 1
    else:
      tieScore += 1
    print("="*40)
    print("Your score: ", playerScore, "CPU: ", cpuScore, "Ties: ", tieScore)
    print(rounds)
    print("="*40)

### Check for winner
def checkForWinner(player, computer):
  if(player == Rock and computer == Paper):
    print("Sorry you lost this round :(")
    return "Cpu"
  elif(player == Rock and computer == Scissors):
    print("Congrats! You have won this round :)")
    return "Player"
  elif(player == Scissors and computer == Paper):
    print("Congrats! You win this round :)")
    return "Player"
  elif(player == Scissors and computer == Rock):
    print("Sorry, you lost this round :(")
    return "Cpu"
  elif(player == Paper and computer == Rock):
    print("Congrats! You win this round :)")
    return "Player"
  elif(player == Paper and computer == "Scissors"):
    print("Sorry, you lost this round :(")
    return "Cpu"
  else:
    print("It's a tie, play again! :|")
    return "Tie"

### Calls main loop/Game start
_main_(playerScore,cpuScore,tieScore,rounds)
### Game over
print("Game over!")
print("="*40)
