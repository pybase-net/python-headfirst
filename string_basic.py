#!/usr/bin/env python3

alphabet = []

a_index = ord('a')
for index in range(0, 25):
    alphabet.append(chr(a_index + index))

print(alphabet)


def generate_repeated_strings(number_of_chars=5):
    result = []
    for index in range(0, number_of_chars):
        result.append(alphabet[index]*(index+1))
    return result


print(generate_repeated_strings())
