CURRENT_YEAR = 2024
METER_TO_FEET = 3.281

firstname = input(("your firstname: ")) #function #built-in fuction
lastname = input(("your lastname: "))
year_born = input(("when you were born: "))
height_meter = input(("your height (meter): "))


year_born = int(year_born)
age = CURRENT_YEAR - year_born

height_meter = float(height_meter)
height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1) 

print("\n---") # newline charecter
print("your name is " + firstname + " " + lastname)
print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
print("you are " + str(height_feet) + " feet tall")