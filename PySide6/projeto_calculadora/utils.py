import re

NUm_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def is_num_or_dot(string: str):
    return bool(NUm_OR_DOT_REGEX.search(string))


def is_valid_number(string: str):
    valid = False
    try:
        float(string)
        # print('deu bom')
        valid = True
    except ValueError:
        # print('deu ruim')
        valid = False
    return valid


def convert_to_int(string: str):
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


def isempty(string: str):
    # string == ''
    return len(string) == 0
