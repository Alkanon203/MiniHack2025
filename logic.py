#This program will ask the user how many meals they want for breakfast, lunch, and dinner. Then it outputs the amount of recipes 
#they asked for. The recipes will be random.

import random

breakfast_recipes = ["eggs", "pancakes", "porridge", "waffles"]
lunch_recipes = ["burgers", "fries", "pizza"]
dinner_recipes = ["steak", "pasta", "salad"]

breakfast = int(input("How many meals for breakfast do you want?: "))
lunch = int(input("How many meals for lunch do you want?: "))
dinner = int(input("How many meals for dinner do you want?: "))


def br(meal,food):
    for i in range(0,meal):
        recipes = random.choice(food)
        print(f"Breakfast: {recipes}")


def lu(meal,food):
    for i in range(0,meal):
        recipes = random.choice(food)
        print(f"Lunch: {recipes}")


def di(meal,food):
    for i in range(0,meal):
        recipes = random.choice(food)
        print(f"Dinner: {recipes}")


print("\nMeal Plan")
print("---------------------------")
if breakfast > 0:
    br(breakfast,breakfast_recipes)
if lunch > 0:
    lu(lunch,lunch_recipes)
if dinner > 0:
    di(dinner,dinner_recipes)