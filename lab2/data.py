def division(num1, num2):
    result = num1 / num2
    print(result)
    return result


add_one = lambda x: x + 1


class Car(object):
    brand = "Peugeot"
    model = "406"

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model