import random as rand
print("Welcome to Math Quiz!")
#Setup question related variables for later
correct_answers = 0
incorrect_answers = 0
#Get input until arithmetic is not invalid
invalid_arithmetic = True
valid_arithmetic_list = ['+', '-', '*', '/']
while invalid_arithmetic:
    arithmetic = input("\nPlease enter an arithmetic: ")
    if arithmetic in valid_arithmetic_list:
        invalid_arithmetic = False
    else:
        print("Invalid input")
invalid_question_amount = True
#Get input until question amount is not invalid
while invalid_question_amount:
    question_amount = input("Please enter the amount of questions: ")
    question_amount = int(question_amount)
    if isinstance(question_amount, int):
        invalid_question_amount = False
    else:
        print("Invalid input")
for i in range(question_amount):
    #Get 2 random numbers
    num1 = rand.randint(1,12)
    num2 = rand.randint(1,12)
    #Find arithmetic & ask question
    if arithmetic == '+':
        answer = input(f"\nWhat is {num1} + {num2}? ")
        result = num1 + num2
    if arithmetic == '-':
        answer = input(f"\nwhat is {num1} - {num2}? ")
        result = num1 - num2
    if arithmetic == '*':
        answer = input(f"\nwhat is {num1} * {num2}? ")
        result = num1 * num2
    if arithmetic == '/':
        answer = input(f"\nwhat is {num1} / {num2}? ")
        result = num1 / num2
    answer = int(answer)
    #Check if answer == result and judge accordingly
    if answer == result:
        correct_answers += 1
        print("Correct")
    else:
        incorrect_answers += 1
        print(f"Incorrect, the answer was actually {result}")
#Print the score
print(f"\nYou got {correct_answers}/{question_amount} right")
if incorrect_answers > 1 or incorrect_answers < 1:
    print(f"You missed {incorrect_answers} questions")
else:
    print("You missed 1 question")
