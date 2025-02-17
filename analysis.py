
def greet(user_name):
    return f"Hello, {user_name}!"

def farewell(name):
    return f"Goodbye, {user_name}!"
user_name = "Jesudian"
print(farewell(user_name))

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
