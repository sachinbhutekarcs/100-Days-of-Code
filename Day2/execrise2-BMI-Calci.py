#Write a program to calculate BMI for given weight & height

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(int(weight) / (int(height) ** 2))
print(BMI)