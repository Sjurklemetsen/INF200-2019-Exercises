__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'


from random import randint


def guess_number():
    guess = 0
    while guess < 1:
        guess = int(input('Your guess: '))
    return guess


def sum_dices():
    return randint(1, 6) + randint(1, 6)


def correct_guess(corr_number, guess):
    return corr_number == guess


if __name__ == '__main__':

    corr_guess = False
    tries = 3
    corr_number = sum_dices()
    while not corr_guess and tries > 0:
        guess = guess_number()
        corr_guess = correct_guess(corr_number, guess)
        if not corr_guess:
            print('Wrong, try again!')
            tries -= 1

    if tries > 0:
        print('You won {} points.'.format(tries))
    else:
        print('You lost. Correct answer: {}.'.format(corr_number))
