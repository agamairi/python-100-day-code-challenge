# we talk about different data types in python, how you can use subscripting which helps in getting individual alphabets from a string

# making a tip calculator

# # code challenge 1

# user_input = input("please enter a number? ")

# num1 = int(user_input[0])
# num2 = int(user_input[1])
# total = num1 + num2
# print("the total of this your number is " + str(total))

# # Code challenge 2

# height = input("enter your height in m: ")
# weight = input("enter your wight in KG: ")

# BMI = float(weight) / float(height) ** 2

# print("your BMI is : " + str(int(BMI)))

# # coding challenge 3

# age = input("what is your current age? ")

# age = int(age)

# years_left = 90 - age
# days_left = years_left * 365
# weeks_left = years_left * 52
# months_left = years_left * 12

# print(
#     f'days remaining: {days_left}, weeks remaining: {weeks_left}, months left: {months_left}, Years left: {years_left}'
# )


# Tip Calculator

total = input("please enter the total amount: ")
total = float(total)

people_count = input("split the bill between how many people? ")
people_count = int(people_count)

tip_percent = input(
    "what percentage of the tip? select a value between 10, 12, 15: ")
tip_percent = int(tip_percent)

tip_amount = (total / people_count) * (tip_percent/100)

print(f'tip total = {tip_amount * people_count} divided among: {people_count} people, would result in each person paying: {tip_amount}')

# day 2, successfully completed
