import inspect

class VerboseMixin:
    def print_output(self, verbosity:str, action:str='', *args:str, **kwargs:str) -> None:
        method_name = inspect.currentframe().f_back.f_code.co_name
        output = f'[{verbosity}] - {method_name} \n'
        for arg in args:
            output += arg + ' - '

        for kwarg in kwargs:
            output += kwarg + ' - '
        
        print(output)

class LogMixin:
    def __init__(self) -> None:
        pass