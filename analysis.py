import pandas as pd

def sum_values():
    df = pd.read_csv('data/sample_data.csv')
    return df['value'].sum()

# Add the following lines in the main block
    print(f"Sum of values: {sum_values()}")

def farewell(user_name):
    return f"Goodbye, {user_name}!"
user_name = "Jesudian"


def greet(user_name):
    return f"Hello, {user_name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print(farewell(user_name))
