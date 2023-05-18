#!/usr/bin/env python3
import random


class MembershipType:
    NORMAL_MEMBER = 'normal_member'
    GOLD_MEMBER = 'gold_member'


class User:

    def log(self):
        print('This is user log')


class Employee(User):
    def log(self):
        print('This is employee')
        super().log()
        print("-" * 10)


class Customer(User):
    def log(self):
        print('This is customer')
        super().log()
        print("-" * 10)

    def __init__(self, first_name, last_name, membership_type):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_type = membership_type

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @first_name.deleter
    def first_name(self):
        del self._first_name

    def update_membership(self, membership_type):
        self.membership_type = membership_type

    def fullname(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return f"{self.fullname()} - {self.membership_type}"

    def __eq__(self, other):
        return self.fullname() == other.fullname()

    __repr__ = __str__

    def print_all_customers(customers):
        for customer in customers:
            customer.log()


c1 = Customer("Python Basic Tutorial", "Pybase", MembershipType.NORMAL_MEMBER)
c2 = Customer("Flaks Tutorial", 'Pybase', MembershipType.GOLD_MEMBER)
c3 = Customer("Python Basic Tutorial", "Pybase", MembershipType.NORMAL_MEMBER)

customers = [c1, c2, Employee()]

print(c1 == c2, c1 == c3)

Customer.print_all_customers(customers)

print(customers)


class Top:
    pass


class Left(Top):
    pass


class Right(Top):
    pass


class Bottom(Left, Right):
    pass


class Bao(object):

    def __init__(self):
        self.name = "Bao"

    def hello(self):
        print(f"this is ${self.name}")

    def __str__(self):
        return self.name


class Keo(Bao):
    def __init__(self):
        self.name = "Keo"


class Bua(Keo):
    def __init__(self):
        self.name = "Bua"


class Bao(Bua):
    def __init__(self):
        self.name = "Bao"


bao = Bao()
keo = Keo()
bua = Bua()

print(bao, keo, bua)


class Calculation:
    @staticmethod
    def is_prime(number):
        # not a natural number
        if number % 1 != 0 or number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        i = 3
        while i < number:
            if number % i == 0:
                return False
            i += 2
        return True

    @staticmethod
    def generate_list_of_prime_numbers(length):
        if length < 1:
            return []
        if length == 1:
            return [3]
        n = 1
        limit = 100
        list_of_numbers = []
        while len(list_of_numbers) < length and len(list_of_numbers) < limit:
            if Calculation.is_prime(n):
                list_of_numbers.append(n)
            n += 2
        return list_of_numbers


class Question:
    ANSWERS = ("A", "B", "C", "D")

    def __init__(self, question, answers, correct_answer_index):
        question = str(question).strip()
        assert len(question) > 0, f"Question must not be empty!"
        self._question = question
        self.answers = answers
        self.correct_answer_index = correct_answer_index

    @property
    def question(self):
        return self._question

    def display_question(self):
        display = f"{self.question}\n"
        for answer_index in range(0, len(self.answers)):
            display += f"{Question.ANSWERS[answer_index]}. {self.answers[answer_index]}\n"
        print(display)

    def display_answer(self):
        print(
            f"Correct Answer is {Question.ANSWERS[self.correct_answer_index]}.{self.answers[self.correct_answer_index]}\n")


class Game:
    MAX_LEVEL = 100

    @classmethod
    def start_game(cls):
        print(f"This game has {cls.MAX_LEVEL} levels! Have fun!")
        q = cls().generate_next_question()
        return q

    def __init__(self):
        self.level = 0
        self.questions = []

    def generate_next_question(self):
        self.level += 1
        a = random.randint(0, 10 * Game.MAX_LEVEL)
        b = random.randint(0, 10 * Game.MAX_LEVEL)
        question = f"{a} + {b} = ?"
        correct_answer = a + b
        answers = [correct_answer]
        while len(answers) < 4:
            random_answer = random.randint(0, 2 * 10 * Game.MAX_LEVEL)
            try:
                if answers.index(random_answer):
                    continue
            except ValueError:
                answers.append(random_answer)

        random.shuffle(answers)
        correct_answer_index = answers.index(correct_answer)
        qu = Question(question=question, answers=answers, correct_answer_index=correct_answer_index)
        self.questions.append(qu)
        return qu


game = Game()
q = game.start_game()
q.display_question()
q.display_answer()
print(f"Level: {game.level}")
