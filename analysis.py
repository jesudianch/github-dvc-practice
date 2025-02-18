def farewell(user_name):
    return f"Goodbye, {user_name}!"
user_name = "Jesudian"


def greet(user_name):
    return f"Hello, {user_name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print(farewell(user_name))
