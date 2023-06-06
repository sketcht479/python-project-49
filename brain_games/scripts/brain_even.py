from random import randint
from brain_games.cli import welcome_user
from brain_games.cli import basegame


def main():
    name = welcome_user()
    sinopsis = 'Answer "yes" if the number is even, otherwise answer "no".'
    counter = 0
    print(sinopsis)
    while counter < 3:
        question = randint(0, 100)
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if basegame(correct_answer, question, name) == 0:
            counter += 1
        else:
            break
    if counter == 3:
        print('Congratulations, ' + name)


if __name__ == '__main__':
    main()
