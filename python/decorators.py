"""
Decorators in Python
"""


def generalized_decorator(function):
    def wrapper(*args, **kwargs):
        print(
            "The function called {} is invoked!".format(
                function.__code__.co_name
            )
        )
        function(*args, **kwargs)
        print("The function call has ended!")

    return wrapper


@generalized_decorator
def add_two(x, y):
    print(x + y)


def main():
    add_two(1, 2)


if __name__ == "__main__":
    main()
