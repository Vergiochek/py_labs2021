import choose_p
from data import Car, division, add_one


if __name__ == '__main__':
    # obj = Car
    # obj = division
    obj = add_one
    # obj = Car("LADA", "2106")
    my_serializer = choose_p.Serializer
    while True:
        print("1 - JSON \n"
              "2 - TOML\n"
              "3 - YAML\n"
              "4 - PICKLE\n"
              "5 - quit")
        user_input = int(input())
        if user_input == 1:
            my_serializer.serialize(obj=obj, format="JSON")
        elif user_input == 2:
            my_serializer.serialize(obj=obj, format="TOML")
        elif user_input == 3:
            my_serializer.serialize(obj=obj, format="YAML")
        elif user_input == 4:
            my_serializer.serialize(obj=obj, format="PICKLE")
        else:
            exit(0)