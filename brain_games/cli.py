import prompt


def welcome_user():
    name = prompt.string("May I have your name? ")
    print("Hello " + name + '!')
    return name


def basegame(correct_answer, question, name):
    print('Question: ' + str(question))

    user_answer = prompt.string('Your answer: ')
    if user_answer == correct_answer:
        print('Correct!')
        return 0
    else:
        print("'" + user_answer + "'" + " is wrong answer ;(. Correct answer was " + "'" + correct_answer + "'" + " Let's try again " + name + '!')
