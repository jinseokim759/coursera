# Using explicit type conversion, change the following 
# inputs so the types match with the following below
#  
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# Modify the line below
name = input('What is your name? ')
name = str(name)
name_type = type(name)

print(f"Type of name variable is: " + str(name_type))

# Modify the line below
age = input('What is your age? ')
age = int(age)
age_type = type(age)

print(f"Type of age variable is: " + str(age_type))

# Modify the line below
height = input('What is your height in meters? ')
height = float(height)
height_type = type(height)

print(f"Type of height variable is: " + str(height_type))

# Modify the line below
loyalty = input('Are you part of our loyalty program? ')
loyalty = bool(loyalty)
loyalty_type = type(loyalty)

print(f"Type of loyalty variable is: " + str(loyalty_type))