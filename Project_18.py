import random
Random = random.randint(1, 6)
Guess = int(input("Please guess my chosen number between 1 and 6:\n"))
if Guess == Random:
    print(" Great, You guessed correctly")
elif Guess > Random:
    print("Your guessed number was bigger than my chosen number\n")
elif Guess < Random:
    print("Your guessed number was lower than my chosen number\n")
    
print(";) My chosen number was: ",  Random)
