# Randomization

import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# code challenge 1:

# a function called coin_toss that takes no input and returns a string with a random heads or tails.
randomSide = random.randint(0, 1)
if randomSide == 1:
    print("heads")
else:
    print("tails")

# PYTHON LISTS (IMPORTANT)
# lists are mutable (can be changed)
# lists are contained by the square brackets
# lists can store different data types, even in the same list
# list values are comma separated

# code challenge 2
list_of_people = ["Person 1", "Person2", "Person3", "Person4"]
list_of_people.append("John")
person_paying = list_of_people[random.randint(0, len(list_of_people) - 1)]
print(person_paying + " is going to buy the meal today")

# can also use random.choice() which will reduce the code and achieve the same thing, this was done to check the understanding of this part.

# Nesting of lists

fruits = ["apple", "banana", "watermelon", "peach"]
vegetables = ["ladyfinger", "potato", "capsicum"]

combined_list = [fruits, vegetables]
print(combined_list)

# code challenge 3
row1 = ["O", "O", "O"]
row2 = ["O", "O", "O"]
row3 = ["O", "O", "O"]
board = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure?")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = board[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# code challenge 4: rock paper scissors

playerChoice = int(
    input("what do you choose? 0 for rock, 1 for paper, 2 for scissors\n"))
choiceList = ["rock", "paper", "scissors"]
if playerChoice >= 3:
    print("invalid choice")
computerChoice = random.randint(0, len(choiceList) - 1)
print("Play Game: 3, 2, 1...GO!\nPlayer Choice: " +
      choiceList[playerChoice] + "\n\nComputer Choice: " + choiceList[computerChoice])

if playerChoice == 0 and computerChoice == 2:
    print("You Win!")
elif computerChoice == 2 and playerChoice == 1:
    print("You lost!")
elif computerChoice > playerChoice:
    print("You Lose!")
elif playerChoice > computerChoice:
    print("You win!")
elif computerChoice == playerChoice:
    print("It is a draw!")
else:
    print("You lost")
