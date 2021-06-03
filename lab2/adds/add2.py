def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

amount = int(input("How much: "))
generator = fibonacci()
for i in range(amount):
    print(next(generator))