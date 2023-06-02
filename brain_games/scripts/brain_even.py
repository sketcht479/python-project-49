import prompt
from random import randint
from brain_games.cli import welcome_user


def correct(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no". ')
    counter = 0
    while counter < 3:
        num = randint(0, 100)
        answer = prompt.string('Question:' + str(num) + ' ')
        if answer == correct(num):
            print('Correct!')
            counter += 1
        else:
            print("'"+answer + "'" + " is wrong answer ;(. Correct answer was " + "'" + correct(num)+"'")
            break
    print('Congratulations ' + name)


if __name__ == '__main__':
    main()
