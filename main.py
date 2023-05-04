# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def headfirst_data_types():
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    headfirst_data_types()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
