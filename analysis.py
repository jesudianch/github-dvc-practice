
def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"

print(farewell(user_name))


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
