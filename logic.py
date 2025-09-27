#This program will ask the user how many meals they want for breakfast, lunch, and dinner. Then it outputs the amount of recipes 
#they asked for. The recipes will be random.

import random

breakfast_recipes = ["eggs", "pancakes", "porridge", "waffles"]
lunch_recipes = ["burgers", "fries", "pizza"]
dinner_recipes = ["steak", "pasta", "salad"]

def br(meal,food):
    recipes = random.choice(food)
    print(f"Breakfast: {recipes}")


def lu(meal,food):
    recipes = random.choice(food)
    print(f"Lunch: {recipes}")


def di(meal,food):
    recipes = random.choice(food)
    print(f"Dinner: {recipes}")

def main():
    print("\nWelcome to the G-ATE-R Meal Planner!!!")
    print("--------------------------------------")
    print("Instructions:")
    print("Please input the amount of days you want your meals planned and a list of ingredients you currently have. ", end="")
    print("We will generate a list of recipes for each day.")

    while True:
        try:
            days = int(input("\nHow many days do you want your meals planned?: "))
            if days > 0:
                print("\nMeal Plan")
                print("---------------------------")
                for i in range(1,days+1):
                    print(f"Day{i}")
                    breakfast = br(days,breakfast_recipes)
                    lunch = lu(days,lunch_recipes)
                    dinner = di(days,dinner_recipes)
                    print()
                break
            else:
                print("Invalid input. Please choose a positive integer.")
        except ValueError:
            print("Invalid input. Please choose a positive integer.")

    print("Thank you for planning your meals with the G-ATE-R. We hope to see you again!")

main()
