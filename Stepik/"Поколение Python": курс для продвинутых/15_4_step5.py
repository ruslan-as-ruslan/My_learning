import math

func_dict = {'квадрат': lambda x : x ** 2,
             'куб': lambda x : x ** 3,
             'корень': lambda x: x ** 0.5,
             'модуль': abs,
             'синус': math.sin
             }

n = int(input())
name = input()

print(func_dict[name](n))