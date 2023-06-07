import random
from brain_games.cli import welcome_user
from brain_games.cli import basegame

def nod(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    nd = n2
    while (n1 % nd != 0) or (n2 % nd != 0):
        nd -= 1
    return nd


def main():
    name = welcome_user()
    sinopsis = 'Find the greatest common divisor of given numbers.'
    counter = 0
    print(sinopsis)
    while counter < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = str(num1) + ' ' + str(num2)
        correct_answer = str(nod(num1, num2))

        if basegame(correct_answer, question, name) == 0:
            counter += 1
        else:
            break
    if counter == 3:
        print('Congratulations, ' + name)


if __name__ == '__main__':
    main()
