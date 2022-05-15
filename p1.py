#Program takes two ints as a range(start and end) and makes user guess the random number generated

import random

flag = True
while(flag):
    start = (input("Enter the start of the range: "))
    if (start.isdigit()):
        pass
    else:
        print("Please enter a valid number")
        continue
    end = (input("Enter the end of the range: "))
    if (int(end)> int(start) and end.isdigit()):
        flag = False
    else:
        print("Please enter a valid number")

random_num = random.randint(int(start),int(end))
#print(f"start: {start}\nend: {end}\nrand: {random_num}")
correct = False
guesses = 0
while(not correct):
    guessed_num = (input("Guess a number: "))
    if(not guessed_num.isdigit()):
        print("Please enter a valid number")
        continue
    if(int(guessed_num) > int(end) or int(guessed_num) < int(start)):
        print("Please enter a valid number")
        continue
    guesses += 1
    if (int(guessed_num) == random_num):
        correct = True
if guesses > 1:
    print(f"You guessed the number in {guesses} attempts")
else: 
    print(f"You guessed the number in {guesses} attempt")