#!/usr/bin/env python3
from random import randint

foods = ["Apple", "Rice", "Noodle"]
drinks = ["Water", "Coffee", "Tea"]

print("-"*20)

for food in foods:
    print(food)

print("-"*20)

for drink in drinks:
    print(drink)


def random_order(things):
    return things[randint(0, len(things)-1)]


mixed = []
mixed.append(random_order(foods))
mixed.append(random_order(drinks))

print("-"*20)

for item in mixed:
    print(item)

print("-"*20)

tada_mixed = list(map(lambda item: f"Tada:{item}", mixed))
print(tada_mixed)

scores = [1, 3, 5]


def find_score_index(scores, value):
    try:
        return scores.index(value)
    except ValueError:
        return None


print(find_score_index(scores, 0))
print(find_score_index(scores, 3))
for v in range(0, randint(10, 100)):
    scores.append(v) if not find_score_index(scores, v) else None

print(scores, len(scores))


things = ['a', 1, 2, 'b', 3, 'c', 'd', 'a', 'a', '2']

a_indices = [a for a in things if a == 'a']
a_indexes = [index for index, v in enumerate(things) if v == 'a']

print(a_indices, a_indexes)
