from math import *

def parse_html():
    return 3

def calculator(p1, p2, method = '+'):
    if method == '+':
        result = p1 + p2
    elif method == '*':
        result = p1 * p2
    elif method == ':':
        result = p1 / p2
    elif method == '-':
        result = p1 - p2
    elif method == '^':
        result = pow(p1,p2)
    else:
        result = 'None'
    return result

# class Imre(object):
#     imre = 42
#
#     def __init__(self):
#         self.a = 8
#         print('constructor')
#
#     def __repr__(self):
#         return 'hello, imre vagyok'
#
#
#     def vmi(self):
#         print(self.imre)
#
# i = Imre()
# i2 = Imre()
# print(i.imre)
# i.vmi()
#
# print(i.a)
#
# print(Imre.imre)
#
# i2.a = 45
#
# print(i2)



