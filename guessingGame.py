import random

print('Let's play a number guessing game)

num = random.randint(1, 9)

chances = 0

print('Guess a number from 1 to 9 within five chances')

while chances < 5:
    guess = int(input('Enter your guess:'))

    if (guess == num):
        print('Correct!')
        break

    elif (guess < num):
        print('Your guess is too low!')
        print('Guess a number higher than this')

    else:
        print('Your guess is too high!')
        print('Guess a number lower than this')

    chances += 1

if (chances == 5 and guess != num):
    print('You lose!')