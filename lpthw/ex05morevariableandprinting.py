my_name = "Zed A. Shaw"
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# 1 -> remove my_
name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# 2 -> variables for lbs - kg and inchs - cm
name = "Zed A. Shaw"
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"
height_cm=height*2.54 # 1 inch = 2.54 cm
weight_kg=weight*0.454 # 1 lbs = 0.454 kg

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {height_cm} cms tall.")
print(f"He's {weight_kg} kgs heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")
