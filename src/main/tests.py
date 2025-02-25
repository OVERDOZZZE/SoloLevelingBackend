# from django.test import TestCase

# Create your tests here.

import re


def func():
    while True:
        try:
            a = eval(input('Enter value: '))
        except ValueError as e:
            return f'Error: {e}'
        else:
            if type(a) is int:
                return not a % 2
            elif type(a) is float:
                return f'{len(str(a).split(".")[0]), len(str(a).split(".")[1])}'
            else:
                return f'{len(str(a))}, {str(a).count(".")}'


# print(func())

x = 231.564564

s = re.match(r'(\d+)\.(\d+)', str(x))

print(s.group(1), s.group(2))

