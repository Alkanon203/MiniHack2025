import csv
import ast
import random


def load_recipes_from_csv(filepath):
    recipes = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    # A standard, clean loader for properly formatted CSVs
                    recipe_data = {
                        'id': int(row[0]),
                        'title': row[1],
                        'ingredients_full': ast.literal_eval(row[2]),
                        'instructions': ast.literal_eval(row[3]),
                        'ingredients_clean': ast.literal_eval(row[6])
                    }
                    recipes.append(recipe_data)
                except (ValueError, SyntaxError, IndexError):
                    continue
    except FileNotFoundError:
        print(f"Warning: Could not find the file {filepath}")
    return recipes


def find_makeable_dishes(user_ingredients_set, all_recipes, match_threshold=0.50):
    makeable_recipes = []
    for recipe in all_recipes:
        recipe_ingredients_phrases = recipe.get('ingredients_clean', [])
        if not recipe_ingredients_phrases:
            continue
        ingredients_user_has_count = 0
        for required_phrase in recipe_ingredients_phrases:
            words_in_phrase = set(required_phrase.replace('_', ' ').split())
            if words_in_phrase.issubset(user_ingredients_set):
                ingredients_user_has_count += 1
        if len(recipe_ingredients_phrases) == 0:
            continue
        match_percentage = ingredients_user_has_count / \
            len(recipe_ingredients_phrases)
        if match_percentage >= match_threshold:
            missing_ingredients = []
            for phrase in recipe_ingredients_phrases:
                words_in_phrase = set(phrase.replace('_', ' ').split())
                if not words_in_phrase.issubset(user_ingredients_set):
                    missing_ingredients.append(phrase.replace('_', ' '))
            recipe['missing'] = missing_ingredients
            makeable_recipes.append(recipe)
    return makeable_recipes


def get_meal_object(food):
    if not food:
        return None
    return random.choice(food)


def display_recipe(recipe):
    if recipe is None:
        print("No recipe was selected or found.")
        return
    print("\n" + "="*40)
    print(f"Recipe: {recipe['title']}")
    print("="*40)
    if recipe.get('missing'):
        missing_str = ", ".join(recipe['missing'])
        print(f"NOTE: You might be missing these ingredients: {missing_str}")
    print("\n--- Ingredients ---")
    for item in recipe['ingredients_full']:
        print(f"- {item}")
    print("\n--- Instructions ---")
    for i, step in enumerate(recipe['instructions'], 1):
        print(f"{i}. {step}")
    print("="*40)


def main():
    all_breakfasts = load_recipes_from_csv('breakfast_recipes_500.csv')
    all_lunches = load_recipes_from_csv('lunch_recipes_500.csv')
    all_dinners = load_recipes_from_csv('dinner_recipes_500.csv')

    print("\nWelcome to the G-ATE-R Meal Planner!!!")
    print("--------------------------------------")
    print("Instructions:")
    print("Please input the amount of days you want your meals planned and a list of ingredients you currently have. ", end="")
    print("We will generate meals you can make. We can also generate the recipes for the meal of your choosing.")

    user_input_str = input("\nEnter your ingredients, separated by commas: ")
    user_ingredients = {ingredient.strip().lower()
                        for ingredient in user_input_str.split(',')}

    makeable_breakfasts = find_makeable_dishes(
        user_ingredients, all_breakfasts)
    makeable_lunches = find_makeable_dishes(user_ingredients, all_lunches)
    makeable_dinners = find_makeable_dishes(user_ingredients, all_dinners)

    print(f"\nFound {len(makeable_breakfasts)} potential breakfasts, {len(makeable_lunches)} potential lunches, and {len(makeable_dinners)} potential dinners.")

    planned_meals = {}

    while True:
        try:
            days = int(
                input("\nHow many days do you want your meals planned?: "))
            if days > 0:
                print("\nMeal Plan")
                print("---------------------------")
                for i in range(1, days + 1):
                    print(f"Day {i}")
                    breakfast_obj = get_meal_object(makeable_breakfasts)
                    lunch_obj = get_meal_object(makeable_lunches)
                    dinner_obj = get_meal_object(makeable_dinners)
                    planned_meals[i] = {
                        'breakfast': breakfast_obj, 'lunch': lunch_obj, 'dinner': dinner_obj}
                    b_title = breakfast_obj['title'] if breakfast_obj else "No makeable breakfast found."
                    l_title = lunch_obj['title'] if lunch_obj else "No makeable lunch found."
                    d_title = dinner_obj['title'] if dinner_obj else "No makeable dinner found."
                    print(f"  Breakfast: {b_title}")
                    print(f"  Lunch: {l_title}")
                    print(f"  Dinner: {d_title}")
                    print()
                break
            else:
                print("Invalid input. Please choose a positive integer.")
        except ValueError:
            print("Invalid input. Please choose a positive integer.")

    while True:
        view_choice = input(
            "\nWould you like to see a recipe? (yes/no): ").lower().strip()
        if view_choice == 'no':
            break
        if view_choice == 'yes':
            try:
                recipe_query = input(
                    "Enter the day and meal (e.g., '1 breakfast', '3 dinner'): ").lower()
                day_str, meal_type = recipe_query.split()
                day_num = int(day_str)
                if day_num in planned_meals and meal_type in planned_meals[day_num]:
                    recipe_to_show = planned_meals[day_num][meal_type]
                    if recipe_to_show:
                        display_recipe(recipe_to_show)
                    else:
                        print(
                            f"No recipe was found for Day {day_num} {meal_type}.")
                else:
                    print(
                        "Invalid selection. Please enter a valid day and meal type (breakfast, lunch, dinner).")
            except (ValueError, KeyError):
                print("Invalid format. Please use the format 'day meal'.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print("\nThank you for planning your meals with the G-ATE-R. We hope to see you again!")


if __name__ == "__main__":
    main()
