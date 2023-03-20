# Learning about conditional statements using python

# coding exercise 1 : odd even

value = int(input("please enter a number: "))

if value % 2 == 0:
    print("{} is even".format(value))
else:
    print("{} is odd".format(value))

# nesting of if else statements if quite common and a good way to check if 2 conditions are true

# coding challenge 2: leap year

year = int(input("please enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))
else:
    print("{} is not a leap year".format(year))


# coding challenge 3: pizza order

print("welcome to pizza deliveries")

size = input("what size pizza do you want? S or M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill_amt = 0

if size == 'S':
    bill_amt += 15
    if add_pepperoni == 'Y':
        bill_amt += 2
elif size == 'M':
    bill_amt += 20
    if add_pepperoni == 'Y':
        bill_amt += 3
elif size == 'L':
    bill_amt += 25
    if add_pepperoni == 'Y':
        bill_amt += 3

if extra_cheese == 'Y':
    bill_amt += 1

print(f'Your total Bill amounts to: {bill_amt} ')

# Coding challenge 4: Love Calculator

print("welcome to the love calculator")

name1 = input("What is your name? \n")
name2 = input("what is their name? \n")

combined_name = name1+name2

combined_name = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e

love_score = str(true) + str(love)

if (love_score < 10) or (love_score > 90):
    print(
        f"your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is {love_score}, you are alright together ")
else:
    print(f"your score is {love_score}")
