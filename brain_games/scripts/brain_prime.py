import random
from brain_games.cli import welcome_user
from brain_games.cli import basegame


def main():
    name = welcome_user()
    sinopsis = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    counter = 0
    print(sinopsis)
    while counter < 3:
        number = random.randint(1, 100)
        if number < 10:
            divisions = [i for i in range(2, number)]
        else:
            divisions = [i for i in range(2, 10)]

        correct_answer = 'yes'
        for i in divisions:
            if number % i == 0:
                correct_answer = 'no'
                break

        if basegame(correct_answer, number, name) == 0:
            counter += 1
        else:
            break
    if counter == 3:
        print('Congratulations, ' + name)


if __name__ == '__main__':
    main()
