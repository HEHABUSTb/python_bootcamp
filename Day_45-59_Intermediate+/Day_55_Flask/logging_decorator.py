# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        arg_str = ', '.join(map(str, args))
        print(f"You called {function.__name__}({arg_str})")
        result = function(*args)
        print(f"It returned: {result}")
        return result

    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)