# This is a sample Python script.
import random
import re

# Convention for naming constant in Python
COURSE_NAME = 'Python headfirst'


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def headfirst_data_types():
    """ headfirst data types """

    # Is Python case-sensitive ?: yes
    aVariable = "aVariable"
    avariable = "avariable"
    print(avariable, aVariable, COURSE_NAME)
    print('# Datatypes')
    course_name = "Python headfirst"
    # string concat
    course_name += " 2023"
    print(f"{course_name}")
    course_content = 'Python basic ' 'Knowledge and Oop!111 lorem opsum'
    print(f"{course_content} 2023")
    # string character at
    # course_content[0] is readonly
    print(f"{course_content[0]}")
    print(f"{course_content.lower()}")
    number_of_uppercase_chars, number_of_lowercase_chars = 0, 0

    for index in range(len(course_content)):
        if not course_content[index].isalpha():
            continue
        if course_content[index].islower():
            number_of_lowercase_chars += 1
        else:
            number_of_uppercase_chars += 1
    print(f"Number of uppercase chars: {number_of_uppercase_chars}")
    print(f"Number of lowercase chars: {number_of_lowercase_chars}")
    course_content_excerpt = f"{course_content[0:10]} ..." if len(course_content) > 10 else course_content
    print(course_content_excerpt)
    for char_ascii in range(ord('a'), ord('z')):
        print(chr(char_ascii))

    # numbers: int, float
    print(type(number_of_lowercase_chars).__name__)
    print(type(0.5).__name__)
    print(type(chr(ord('z'))).__name__)
    print(type("aaa").__name__)
    # numbers: format
    print('{:.2f}'.format(3.12345))
    print('{:X>9}'.format(123))
    for month in range(12):
        print(f'{month + 1:0>2}')
    # currency format
    currency = '$'
    print(f'{currency}{100_000_000:,}')  # underscore number is available from 3.6
    print("{0}-{1}".format(5, 'a'))

    # regex
    # regex : MobiPhone number regex
    phone_number_regex = r'093[0-9]{7,8}'
    print("{}:{}".format("0937", re.match(phone_number_regex, "0937")))
    print("{}:{}".format("0937590123 0937590321", re.findall(phone_number_regex, "0937590123 0937590321")))
    # trim space
    print(re.sub(r'\s{2,}', " ", "a generated  text with spaces  "))
    # repeat string and parse
    print('{:,}'.format(int("1" + "0" * 10)))
    # parse float
    tax = "0.15"
    print(f'Tax:{float(tax)}%')
    # magic with float
    print(0.1 + 0.2, 0.30000000000000004, len(str(0.30000000000000004)))
    # bool and falsy
    print(type(False), bool(None), bool(1), bool(0), bool(""), bool(0.0), bool("0"), bool("  "), bool("False"))
    print('a' < 'b', 'a' > 'b', bool([]), bool({}), bool(()))
    # comparison
    a, b, c = True, False, None
    if a and b and c:
        print("All true")
    if a or b or c:
        print("One of them is True")
    if not (a and b and c):
        print("Not all true")
    # shorthand if
    print("a is True") if a else None
    print("c is False") if not c else ""
    # control flow
    random_number = random.randint(1, 100)
    mod_value = random_number % 3
    match mod_value:
        case 0:
            print("{0}/{1} : Chia het".format(random_number, 3))
        case _:
            print("{0}/{1} : Chia co du! {2}".format(random_number, 3, mod_value))
    status_codes = [200, 201, 204, 400, 401, 403, 404, 500, 501, 502]
    random_index = random.randint(0, len(status_codes) - 1)
    status_code = status_codes[random_index]
    match status_code:
        case 200 | 201 | 204:
            print(f"Success request {status_code}")
        case 400 | 401 | 403 | 404:
            print(f"Client error request {status_code}")
        case 500 | 501 | 502:
            print(f"Server error request {status_code}")
    # type struct
    list_of_foods = ['a', 'b', 'c', 'd', 'e']
    food_start_index = random.randint(0, len(list_of_foods) - 1)
    selected_food = random.randint(0, len(list_of_foods))
    foods = []
    if food_start_index + selected_food <= len(list_of_foods):
        foods.extend(list_of_foods[food_start_index:(food_start_index + selected_food)])
    else:
        foods.extend(list_of_foods[food_start_index:len(list_of_foods)])
        foods.extend(list_of_foods[:food_start_index + selected_food - len(list_of_foods)])
    print(list_of_foods, list_of_foods[food_start_index])
    match foods:
        case ['a']:
            print("only one food type", foods, food_start_index, selected_food, )
        case ['a', 'b'] | ['a', 'c'] | ['b', 'c']:
            print('double food types', foods, food_start_index, selected_food, )
        case ['a', 'b', 'c']:
            print('triple food types', foods, food_start_index, selected_food, )
        case ['a', 'b', 'c', *rest]:
            print('More than 3 food types', foods, food_start_index, selected_food, )
        case _:
            print('not even one', foods, food_start_index, selected_food, )
    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print(headfirst_data_types.__doc__)
    headfirst_data_types()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
