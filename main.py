# This is a sample Python script.
import re

# Convention for naming constant in Python
COURSE_NAME = 'Python headfirst'


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def headfirst_data_types():
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
    # falsy values in python


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    headfirst_data_types()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
