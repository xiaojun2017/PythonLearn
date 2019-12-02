try:
    text = input("Enter text:")
except EOFError:
    print('input error.')


class ShortInputException(Exception):
    """自定义异常类"""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input("Enter something: ")
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    else:
        print("input result is:", text)
except EOFError:
    print("InputError")
except ShortInputException as ex:
    print('ShortException, len:', len(text))
else:
    print("No Exception war occur")
