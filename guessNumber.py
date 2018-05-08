import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess<secretNumber:
        print('Your guess is too low.')
    elif guess>secretNumber:
        print('Your guess is too huge.')
    else:
        break   #This is the the correct condition

if guess==secretNumber:
    print('Amazing Job! You have guessed the correct number in ' + str(guessTaken)+ ' guesses!')
else:
    print('Sorry! You couldnt guess the right number. I was thinking of' + str(secretNumber))