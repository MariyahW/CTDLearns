# Section 1:Variables and Types
user={
    "name": "Samantha",
    "age": 11,
    "height": 3.6,
    "is_student": False
}

for value in user.values():
    print(value, type(value))

# Section 2: User Input and Math
from datetime import date
current_year = date.today().year
input_name = input("Hello, it's nice to meet you! What is your name? ")
input_age = input(f"So, {input_name}! What year were you born? ")

print(f"Hi again {input_name}, by my calculations, you are {current_year - int(input_age)}")

