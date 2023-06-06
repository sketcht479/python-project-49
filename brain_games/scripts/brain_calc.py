import random
from brain_games.cli import welcome_user
from brain_games.cli import basegame


def main():
    name = welcome_user()
    sinopsis = 'What is the result of the expression?'
    counter = 0
    print(sinopsis)
    while counter < 3:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        list_op = ['+', '-', '*']
        op = random.choice(list_op)
        question = str(num1) + op + str(num2)
        match op:
            case '+':
                correct_answer = str(num1 + num2)
            case '-':
                correct_answer = str(num1 - num2)
            case '*':
                correct_answer = str(num1 * num2)

        if basegame(correct_answer, question, name) == 0:
            counter += 1
        else:
            break
    if counter == 3:
        print('Congratulations, ' + name)


if __name__ == '__main__':
    main()
