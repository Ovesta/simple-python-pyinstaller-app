'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).

RUS:
библиотека calc содержит функцию add2, которая принимает 2 значения и складывает их вместе.
Если какое-либо значение является строкой (или оба они являются), add2 гарантирует,
что они обе строки, что приводит к объединенному результату.
ПРИМЕЧАНИЕ. Если значение, переданное в функцию 'add2', является плавающим,
это должно быть сделано в кавычках (то есть в виде строки).
'''

# If 'value' is not an integer, convert it to a float and failing that, a string.
## Если 'value' не является целым числом, преобразовать его в число с плавающей точкой и,
## в противном случае, строку.

def conv(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

# The 'add2' function itself
def add2(arg1, arg2):
    # Convert 'arg1' and 'arg2' to their appropriate types
    arg1conv = conv(arg1)
    arg2conv = conv(arg2)
    # If either 'arg1' or 'arg2' is a string, ensure they're both strings.
    if isinstance(arg1conv, str) or isinstance(arg2conv, str):
        arg1conv = str(arg1conv)
        arg2conv = str(arg2conv)
    return arg1conv + arg2conv
