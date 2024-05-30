def fibonacci_generator(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


n = 10
fibonacci_numbers = list(fibonacci_generator(n))
print(fibonacci_numbers)
