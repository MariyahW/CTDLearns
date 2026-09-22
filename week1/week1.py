from datetime import date
current_year = date.today().year

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

input_name = input("Hello, it's nice to meet you! What is your name? ")
input_age = input(f"So, {input_name}! What year were you born? ")

print(f"Hi again {input_name}, by my calculations, you are {current_year - int(input_age)} years old")

# Section 3: Type Conversion and f-Strings
num1=input("Pick a number, any number! ")
num2=input("Pick another number! ")
result = float(num1) * float(num2)
print(f"The product of {num1} and {num2} is {result} aka {num1} * {num2} = {result}")

# Section 4: Formatted Receipt
itemName="Python T-shirt"
itemPrice=19.99
quantity=3
totalPrice=itemPrice*quantity
print(f"++++++++++ RECEIPT +++++++++")
print(f"Item: {itemName}")
print(f"Price: ${itemPrice:.2f}")
print(f"Quantity: {quantity}")
print(f"++++++++++ TOTAL ++++++++++")
print(f"Total: ${totalPrice:.2f}")

# Section 5: Mini-Project -- Profile Card

profileName=input("What is your name?")
profileTown=input("Where is your hometown?")
profileHobby=input("What is your favorite hobby?")
profileFact=input("Tell me a fun fact about yourself!")
profileYear=input("What year were you born?")

print(f"++++++++++ PROFILE: {profileName} ++++++++++")
print(f"++ Hometown: {profileTown}")
print(f"++ Favorite Hobby: {profileHobby}")
print(f"++ Fun Fact: {profileFact}")
print(f"++ Age: {current_year - int(profileYear)}")
print(f"++++++++++ END OF PROFILE ++++++++++")