# calculation
from typing import Set
import random


def calculate(num1, num2):
    return sum(range(num1, num2 + 1))


def calculate2(num1, num2):
    return (num1 + num2) * (num2 - num1 + 1) / 2


def calculate3(*numbers):
    answer = 0
    for number in numbers:
        answer += number

    return answer


def get_answers():
    answers: Set[int] = set()
    while len(answers) < 6:
        answers.add(random.randint(1, 49))
    return answers


answer1 = calculate(1, 10)
answer2 = calculate2(1, 10)
answer3 = calculate3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(answer1)
print(answer2)
print(answer3)

answers = get_answers()
print(sorted(answers))
