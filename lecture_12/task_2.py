dict_ = {
    'key': 'bar'
}

def catch_errors(func):
    def wrapper(*args, **kwargs):
        for x in args[0]:
            key_error = x
        try:
            if kwargs.keys() <= dict_.keys():
                func(*args, **kwargs)
        except KeyError:
            print(f'Found 1 error during execution of your function: KeyError no such key as {key_error}')
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'key': 'bar'})
some_function_with_risky_operation({'foo': 'bar'})