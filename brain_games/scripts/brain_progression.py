import random
from brain_games.cli import welcome_user
from brain_games.cli import basegame


def main():
    name = welcome_user()
    sinopsis = 'What number is missing in the progression?'
    counter = 0
    print(sinopsis)
    while counter < 3:
        start = random.randint(1, 100)
        step = random.randint(1, 10)
        lenght = random.randint(5, 10)
        progression = [i for i in range(start, start + step * lenght, step)]
        correct_answer = random.choice(progression)
        progression[progression.index(correct_answer)] = '..'

        if basegame(str(correct_answer), progression, name) == 0:
            counter += 1
        else:
            break
    if counter == 3:
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
