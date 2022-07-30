from assistant_exceptions import *

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UnknownAssistentCommand as e:
            print(e)
        except UnknownAssistentValue as e:
            print(e)
    return inner