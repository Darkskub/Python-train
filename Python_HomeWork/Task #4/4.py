def log_call(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"Function {func.__name__},outputs the following numbers: {all_args}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def fibonacci_generator(n=10, name="fibonacci"):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


result = list(fibonacci_generator())
print(result)
