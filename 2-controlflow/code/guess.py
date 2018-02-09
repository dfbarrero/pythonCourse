import random

guessesTaken = 0
myName = str(input('Hello! What is your name?'))

number = random.randint(1, 20)
print(myName + ', guess a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.') 
    guess = int(input())
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName)
if guess != number:
    number = str(number)
    print('Nope. The number was '+ number)

