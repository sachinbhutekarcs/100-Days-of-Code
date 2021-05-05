# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

num = random.randint(0, len(names)-1)
print(f"{names[num]} is going to buy a meal today")
