# function without parameters
# def greet():
#   print("Hello!")
#   print("How do you do?")
#   print("Isn't the weather pleasant today?")

# greet()

# # function with parameters
# def greet_with_variables(name):
#   print(f"Hello, {name}!")
#   print(f"How do you do, {name}?")
#   print("Isn't the weather present today?")

# greet_with_variables(input("What is your name? "))

# function with more than 1 parameters
def greet_with(name, location):
  print(f"Hello, {name}!")
  print(f"What is it like, in {location}?")

# greet_with(input("Enter your name. "), input("Enter your location. "))
greet_with(location = input("Enter your location. "), name = input("Enter your name. "))
