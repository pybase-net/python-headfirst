#!/usr/bin/env python3

class MembershipType:
    NORMAL_MEMBER = 'normal_member'
    GOLD_MEMBER = 'gold_member'


class User:
    def log(self):
        print(self)


class Employee(User):
    def log(self):
        print('This is employee')


class Customer(User):
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
