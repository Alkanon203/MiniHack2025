# Save this as generate_lunch_recipes_corrected.py
import csv
import random
import json

BASE_RECIPES_CSV_CONTENT = """
0,"Turkey Club Sandwich","[""3 slices of bread, toasted"", ""4 slices of cooked turkey"", ""2 slices of cooked bacon"", ""1 slice of cheddar cheese"", ""2 lettuce leaves"", ""2 slices of tomato"", ""2 Tbsp. mayonnaise""]","[""Spread mayonnaise on one side of each slice of toast."", ""On the first slice, layer lettuce, turkey, and tomato."", ""Place the second slice of toast on top. Layer bacon and cheese on it."", ""Top with the final slice of toast. Secure with toothpicks and cut diagonally.""]","www.example-lunch.com/recipe/0","Generated","[""bread"", ""turkey"", ""bacon"", ""cheddar cheese"", ""lettuce"", ""tomato"", ""mayonnaise""]"
1,"Classic BLT Sandwich","[""2 slices of bread, toasted"", ""4 slices of cooked bacon"", ""3 lettuce leaves"", ""3 slices of tomato"", ""2 Tbsp. mayonnaise""]","[""Spread mayonnaise on both slices of toast."", ""Layer the bacon, lettuce, and tomato on one slice of bread."", ""Top with the other slice of bread and slice in half.""]","www.example-lunch.com/recipe/1","Generated","[""bread"", ""bacon"", ""lettuce"", ""tomato"", ""mayonnaise""]"
2,"Grilled Cheese Sandwich","[""2 slices of bread"", ""2 slices of American cheese"", ""1 Tbsp. butter""]","[""Butter one side of each slice of bread."", ""Place one slice of bread, butter-side down, in a nonstick skillet over medium heat."", ""Top with cheese, then the second slice of bread, butter-side up."", ""Grill for 2-3 minutes per side, until the bread is golden brown and the cheese is melted.""]","www.example-lunch.com/recipe/2","Generated","[""bread"", ""American cheese"", ""butter""]"
3,"Chicken Salad Sandwich","[""2 slices of bread or 1 croissant"", ""1 c. cooked, shredded chicken"", ""1/4 c. mayonnaise"", ""2 Tbsp. diced celery"", ""1 tsp. lemon juice"", ""salt and pepper to taste""]","[""In a bowl, mix together the shredded chicken, mayonnaise, celery, and lemon juice."", ""Season with salt and pepper."", ""Serve the chicken salad on bread or a croissant with lettuce if desired.""]","www.example-lunch.com/recipe/3","Generated","[""bread"", ""croissant"", ""chicken"", ""mayonnaise"", ""celery"", ""lemon juice"", ""salt"", ""pepper""]"
4,"Tuna Melt Sandwich","[""2 slices of bread"", ""1 can (5 oz.) tuna, drained"", ""1/4 c. mayonnaise"", ""1 slice of provolone cheese"", ""1 Tbsp. butter""]","[""In a bowl, mix tuna and mayonnaise."", ""Butter one side of each slice of bread."", ""Place one slice of bread, butter-side down, in a skillet. Top with tuna salad and then the cheese slice."", ""Top with the second slice of bread, butter-side up. Cook for 2-3 minutes per side until golden and the cheese is melted.""]","www.example-lunch.com/recipe/4","Generated","[""bread"", ""tuna"", ""mayonnaise"", ""provolone cheese"", ""butter""]"
5,"Simple Veggie Wrap","[""1 large flour tortilla"", ""1/4 c. hummus"", ""1/2 c. fresh spinach"", ""1/4 c. shredded carrots"", ""1/4 c. sliced cucumber"", ""1/4 sliced bell pepper""]","[""Lay the tortilla flat and spread a layer of hummus over it, leaving a small border."", ""Layer the spinach, carrots, cucumber, and bell pepper on top of the hummus."", ""Tightly roll the tortilla, tucking in the sides as you go.""]","www.example-lunch.com/recipe/5","Generated","[""flour tortilla"", ""hummus"", ""spinach"", ""carrots"", ""cucumber"", ""bell pepper""]"
6,"Caesar Salad with Chicken","[""1 heart of romaine lettuce, chopped"", ""1 c. cooked, grilled chicken breast, sliced"", ""1/4 c. Caesar dressing"", ""2 Tbsp. grated Parmesan cheese"", ""1/4 c. croutons""]","[""In a large bowl, combine the chopped romaine and sliced chicken."", ""Drizzle with Caesar dressing and toss to coat."", ""Top with Parmesan cheese and croutons just before serving.""]","www.example-lunch.com/recipe/6","Generated","[""romaine lettuce"", ""chicken"", ""Caesar dressing"", ""Parmesan cheese"", ""croutons""]"
7,"Greek Salad","[""1 head of romaine lettuce, chopped"", ""1/2 cucumber, sliced"", ""1/2 red onion, thinly sliced"", ""1/2 c. Kalamata olives"", ""1/2 c. crumbled feta cheese"", ""1/4 c. Greek vinaigrette""]","[""In a large bowl, combine lettuce, cucumber, red onion, and olives."", ""Drizzle with vinaigrette and toss."", ""Sprinkle feta cheese on top before serving.""]","www.example-lunch.com/recipe/7","Generated","[""romaine lettuce"", ""cucumber"", ""red onion"", ""Kalamata olives"", ""feta cheese"", ""Greek vinaigrette""]"
8,"Caprese Salad","[""1 large ripe tomato, sliced"", ""4 oz. fresh mozzarella cheese, sliced"", ""1/4 c. fresh basil leaves"", ""2 Tbsp. balsamic glaze"", ""1 Tbsp. olive oil""]","[""Arrange alternating slices of tomato and mozzarella on a plate."", ""Tuck the fresh basil leaves in between the slices."", ""Drizzle with olive oil and balsamic glaze right before serving.""]","www.example-lunch.com/recipe/8","Generated","[""tomato"", ""mozzarella cheese"", ""basil"", ""balsamic glaze"", ""olive oil""]"
9,"Classic Tomato Soup","[""1 (28 oz.) can crushed tomatoes"", ""1 c. vegetable broth"", ""1/2 c. heavy cream"", ""1 tsp. sugar"", ""salt and pepper to taste""]","[""In a saucepan, combine crushed tomatoes and vegetable broth. Bring to a simmer over medium heat."", ""Reduce heat to low and cook for 10 minutes."", ""Stir in heavy cream and sugar. Season with salt and pepper."", ""Serve hot, often paired with a grilled cheese sandwich.""]","www.example-lunch.com/recipe/9","Generated","[""crushed tomatoes"", ""vegetable broth"", ""heavy cream"", ""sugar"", ""salt"", ""pepper""]"
10,"Chicken Noodle Soup","[""4 c. chicken broth"", ""1 c. cooked, shredded chicken"", ""1 c. egg noodles, uncooked"", ""1/2 c. sliced carrots"", ""1/2 c. sliced celery""]","[""In a large pot, bring chicken broth to a boil."", ""Add carrots and celery. Cook for 5 minutes."", ""Stir in the egg noodles and cook for 6-8 minutes, or until tender."", ""Add the cooked chicken and heat through. Season with salt and pepper if needed.""]","www.example-lunch.com/recipe/10","Generated","[""chicken broth"", ""chicken"", ""egg noodles"", ""carrots"", ""celery""]"
11,"Broccoli Cheddar Soup","[""2 c. chicken broth"", ""1 c. milk"", ""1 head of broccoli, chopped into small florets"", ""1 c. shredded cheddar cheese"", ""1/4 c. flour"", ""4 Tbsp. butter""]","[""In a pot, melt butter. Whisk in flour and cook for 1 minute."", ""Gradually whisk in milk and chicken broth until smooth. Bring to a simmer."", ""Add broccoli florets and cook for 10-15 minutes until tender."", ""Reduce heat to low and stir in the cheddar cheese until melted. Do not boil.""]","www.example-lunch.com/recipe/11","Generated","[""chicken broth"", ""milk"", ""broccoli"", ""cheddar cheese"", ""flour"", ""butter""]"
12,"Simple Burrito Bowl","[""1 c. cooked rice"", ""1/2 c. canned black beans, rinsed"", ""1/2 c. canned corn"", ""1/2 c. salsa"", ""1/4 c. shredded cheese"", ""1 dollop of sour cream""]","[""Place the cooked rice in the bottom of a bowl."", ""Top the rice with black beans, corn, and salsa."", ""Sprinkle with shredded cheese and add a dollop of sour cream.""]","www.example-lunch.com/recipe/12","Generated","[""rice"", ""black beans"", ""corn"", ""salsa"", ""cheddar cheese"", ""sour cream""]"
13,"Quinoa Bowl with Roasted Veggies","[""1 c. cooked quinoa"", ""1 c. mixed roasted vegetables (broccoli, bell peppers, zucchini)"", ""1/4 c. hummus"", ""1 Tbsp. lemon juice""]","[""Place the cooked quinoa in a bowl."", ""Top with the roasted vegetables."", ""In a small bowl, thin the hummus with lemon juice and a little water to make a dressing."", ""Drizzle the hummus dressing over the bowl.""]","www.example-lunch.com/recipe/13","Generated","[""quinoa"", ""broccoli"", ""bell peppers"", ""zucchini"", ""hummus"", ""lemon juice""]"
14,"Macaroni and Cheese","[""2 c. cooked elbow macaroni"", ""2 Tbsp. butter"", ""2 Tbsp. flour"", ""1 1/2 c. milk"", ""2 c. shredded cheddar cheese""]","[""While macaroni is cooking, melt butter in a saucepan. Whisk in flour and cook for 1 minute."", ""Gradually whisk in milk until the sauce is smooth and bubbly."", ""Reduce heat and stir in the cheese until melted."", ""Combine the cheese sauce with the cooked macaroni and serve.""]","www.example-lunch.com/recipe/14","Generated","[""elbow macaroni"", ""butter"", ""flour"", ""milk"", ""cheddar cheese""]"
15,"Cheese Quesadilla","[""1 large flour tortilla"", ""1 c. shredded Mexican cheese blend"", ""1 Tbsp. butter (optional)""]","[""Place the tortilla in a large, dry skillet over medium heat (or melt butter first for a crispier result)."", ""Sprinkle the cheese evenly over the entire tortilla."", ""Once the cheese begins to melt, fold the tortilla in half."", ""Cook for 1-2 minutes per side, until golden brown and the cheese is fully melted."", ""Cut into wedges and serve with salsa or sour cream.""]","www.example-lunch.com/recipe/15","Generated","[""flour tortilla"", ""Mexican cheese blend"", ""butter""]"
16,"Italian Sub","[""1 sub roll, sliced lengthwise"", ""4 slices of salami"", ""4 slices of ham"", ""2 slices of provolone cheese"", ""shredded lettuce"", ""sliced tomato"", ""sliced onion"", ""Italian dressing""]","[""Layer the ham, salami, and provolone cheese on the bottom half of the sub roll."", ""Top with lettuce, tomato, and onion."", ""Drizzle with Italian dressing."", ""Place the top half of the roll on and serve.""]","www.example-lunch.com/recipe/16","Generated","[""sub roll"", ""salami"", ""ham"", ""provolone cheese"", ""lettuce"", ""tomato"", ""onion"", ""Italian dressing""]"
17,"Philly Cheesesteak","[""1 sub roll, sliced lengthwise"", ""1/2 lb. thinly sliced ribeye steak"", ""1 Tbsp. oil"", ""1/2 onion, sliced"", ""4 slices of provolone cheese""]","[""Heat oil in a skillet over medium-high heat. Add onions and cook until softened and lightly browned."", ""Add the sliced steak to the skillet and cook, chopping with a spatula, until browned."", ""Arrange the meat and onions into the shape of the sub roll. Place the provolone slices on top to melt."", ""Place the opened sub roll over the meat and cheese, then use a spatula to flip the entire contents into the roll.""]","www.example-lunch.com/recipe/17","Generated","[""sub roll"", ""ribeye steak"", ""oil"", ""onion"", ""provolone cheese""]"
18,"Cobb Salad","[""1 head of romaine lettuce, chopped"", ""1 c. cooked chicken, diced"", ""2 hard-boiled eggs, chopped"", ""2 slices of bacon, cooked and crumbled"", ""1/2 avocado, diced"", ""1/2 c. cherry tomatoes, halved"", ""1/4 c. crumbled blue cheese"", ""Ranch dressing to taste""]","[""Arrange the chopped lettuce on a large platter or in a bowl."", ""Create neat rows of the chicken, eggs, bacon, avocado, and tomatoes over the lettuce."", ""Sprinkle the blue cheese over the top."", ""Drizzle with Ranch dressing just before serving.""]","www.example-lunch.com/recipe/18","Generated","[""romaine lettuce"", ""chicken"", ""eggs"", ""bacon"", ""avocado"", ""tomatoes"", ""blue cheese"", ""Ranch dressing""]"
19,"Taco Salad","[""2 c. shredded lettuce"", ""1/2 lb. ground beef, cooked with taco seasoning"", ""1/2 c. shredded cheddar cheese"", ""1/4 c. salsa"", ""1/4 c. crushed tortilla chips"", ""sour cream for topping""]","[""Place the shredded lettuce in a bowl."", ""Top with the seasoned ground beef, cheese, and salsa."", ""Sprinkle crushed tortilla chips over the top and add a dollop of sour cream.""]","www.example-lunch.com/recipe/19","Generated","[""lettuce"", ""ground beef"", ""taco seasoning"", ""cheddar cheese"", ""salsa"", ""tortilla chips"", ""sour cream""]"
20,"Lentil Soup","[""1 Tbsp. olive oil"", ""1 onion, chopped"", ""2 carrots, chopped"", ""2 celery stalks, chopped"", ""1 c. brown or green lentils, rinsed"", ""6 c. vegetable broth"", ""1 tsp. cumin""]","[""Heat olive oil in a large pot. Add onion, carrots, and celery and cook until softened."", ""Stir in the lentils, vegetable broth, and cumin."", ""Bring to a boil, then reduce heat and simmer for 40-50 minutes, or until lentils are tender.""]","www.example-lunch.com/recipe/20","Generated","[""olive oil"", ""onion"", ""carrots"", ""celery"", ""lentils"", ""vegetable broth"", ""cumin""]"
21,"Black Bean Soup","[""1 Tbsp. olive oil"", ""1 onion, chopped"", ""2 cans (15 oz.) black beans, rinsed"", ""3 c. vegetable broth"", ""1 tsp. cumin"", ""Juice of 1 lime""]","[""Heat oil in a pot and cook onion until soft."", ""Add one can of black beans, broth, and cumin. Bring to a simmer and cook for 10 minutes."", ""Carefully transfer the soup to a blender and blend until smooth (or use an immersion blender)."", ""Return the soup to the pot, stir in the second can of whole black beans and the lime juice. Heat through.""]","www.example-lunch.com/recipe/21","Generated","[""olive oil"", ""onion"", ""black beans"", ""vegetable broth"", ""cumin"", ""lime""]"
22,"Mediterranean Bowl","[""1 c. cooked quinoa"", ""1/2 c. chickpeas"", ""1/4 c. diced cucumber"", ""1/4 c. diced tomato"", ""2 Tbsp. crumbled feta cheese"", ""1 Tbsp. lemon vinaigrette""]","[""Combine all ingredients in a bowl."", ""Toss gently to mix."", ""Serve chilled or at room temperature.""]","www.example-lunch.com/recipe/22","Generated","[""quinoa"", ""chickpeas"", ""cucumber"", ""tomato"", ""feta cheese"", ""lemon vinaigrette""]"
23,"Leftover Pizza","[""2 slices of leftover pizza""]","[""For best results, place pizza slices in a dry, non-stick skillet over medium-low heat."", ""Cover the skillet and heat for 3-5 minutes, until the cheese is re-melted and the crust is crisp."", ""Alternatively, microwave for 45-60 seconds for a softer crust.""]","www.example-lunch.com/recipe/23","Generated","[""pizza""]"
24,"Simple Pasta with Marinara","[""2 oz. spaghetti or other pasta, dry"", ""1 c. marinara sauce"", ""1 Tbsp. grated Parmesan cheese""]","[""Cook pasta according to package directions. Drain."", ""While pasta cooks, warm the marinara sauce in a small saucepan."", ""Toss the cooked pasta with the warm sauce."", ""Top with Parmesan cheese before serving.""]","www.example-lunch.com/recipe/24","Generated","[""pasta"", ""marinara sauce"", ""Parmesan cheese""]"
25,"Loaded Baked Potato","[""1 large baking potato"", ""1 Tbsp. butter"", ""2 Tbsp. sour cream"", ""1 Tbsp. cooked, crumbled bacon"", ""1 Tbsp. shredded cheddar cheese""]","[""Wash the potato and prick several times with a fork. Microwave on high for 5-7 minutes, or bake at 400°F for 1 hour, until tender."", ""Cut the potato open lengthwise and fluff the inside with a fork."", ""Top with butter, sour cream, bacon, and cheese.""]","www.example-lunch.com/recipe/25","Generated","[""potato"", ""butter"", ""sour cream"", ""bacon"", ""cheddar cheese""]"
26,"Cuban Sandwich","[""1 loaf of Cuban bread"", ""4 oz. sliced roasted pork"", ""4 slices of Swiss cheese"", ""4 slices of deli ham"", ""dill pickles, sliced lengthwise"", ""yellow mustard"", ""2 Tbsp. butter, melted""]","[""Slice Cuban bread loaf in half lengthwise. Spread a generous amount of mustard on the inside of both halves."", ""Layer the roast pork, ham, Swiss cheese, and pickles on the bottom half of the bread. Top with the other half."", ""Brush the outside of the sandwich with melted butter."", ""Press the sandwich in a panini press or in a heavy skillet until the cheese is melted and the bread is golden and crisp.""]","www.example-lunch.com/recipe/26","Generated","[""Cuban bread"", ""pork"", ""Swiss cheese"", ""ham"", ""pickles"", ""mustard"", ""butter""]"
27,"Spinach Salad with Berries","[""3 c. fresh spinach"", ""1/2 c. sliced strawberries"", ""1/4 c. blueberries"", ""1/4 c. crumbled goat cheese"", ""2 Tbsp. sliced almonds"", ""poppy seed dressing""]","[""In a bowl, combine the spinach, strawberries, and blueberries."", ""Sprinkle the goat cheese and almonds over the top."", ""Drizzle with poppy seed dressing when ready to serve.""]","www.example-lunch.com/recipe/27","Generated","[""spinach"", ""strawberries"", ""blueberries"", ""goat cheese"", ""almonds"", ""poppy seed dressing""]"
28,"Chicken Tenders","[""1 lb. chicken breast tenders"", ""1 c. breadcrumbs"", ""1/4 c. grated Parmesan cheese"", ""1 egg, beaten"", ""1/2 c. flour""]","[""Set up three shallow dishes: one with flour, one with the beaten egg, and one with breadcrumbs mixed with Parmesan cheese."", ""Dredge each chicken tender in flour, then dip in the egg, then coat thoroughly with the breadcrumb mixture."", ""Bake at 400°F (200°C) for 15-20 minutes, or air fry at 380°F (190°C) for 12-15 minutes, until golden and cooked through.""]","www.example-lunch.com/recipe/28","Generated","[""chicken tenders"", ""breadcrumbs"", ""Parmesan cheese"", ""egg"", ""flour""]"
29,"Sloppy Joe","[""1 lb. ground beef"", ""1 onion, chopped"", ""1 c. ketchup"", ""1 Tbsp. Worcestershire sauce"", ""2 Tbsp. brown sugar"", ""4 hamburger buns""]","[""In a skillet, brown the ground beef and onion; drain fat."", ""Stir in the ketchup, Worcestershire sauce, and brown sugar. Simmer for 10 minutes."", ""Serve the meat mixture on hamburger buns.""]","www.example-lunch.com/recipe/29","Generated","[""ground beef"", ""onion"", ""ketchup"", ""Worcestershire sauce"", ""brown sugar"", ""hamburger buns""]"
30,"Egg Salad Sandwich","[""4 hard-boiled eggs, peeled and chopped"", ""1/4 c. mayonnaise"", ""1 Tbsp. mustard"", ""2 Tbsp. chopped celery"", ""salt and pepper to taste"", ""4 slices of bread""]","[""In a bowl, gently mash the chopped hard-boiled eggs."", ""Stir in the mayonnaise, mustard, and celery."", ""Season with salt and pepper to taste."", ""Serve between two slices of bread.""]","www.example-lunch.com/recipe/30","Generated","[""hard-boiled eggs"", ""mayonnaise"", ""mustard"", ""celery"", ""salt"", ""pepper"", ""bread""]"
31,"Peanut Butter & Jelly Sandwich","[""2 slices of bread"", ""2 Tbsp. peanut butter"", ""1 Tbsp. jelly or jam""]","[""Spread peanut butter on one slice of bread."", ""Spread jelly or jam on the other slice of bread."", ""Press the two slices together.""]","www.example-lunch.com/recipe/31","Generated","[""bread"", ""peanut butter"", ""jelly""]"
"""

SANDWICH_PROTEINS = ["turkey", "ham", "roast beef",
                     "chicken salad", "tuna salad", "chickpeas"]
SANDWICH_BREADS = ["sourdough", "whole wheat",
                   "rye", "white bread", "a tortilla wrap"]
SANDWICH_VEGGIES = ["lettuce", "tomato",
                    "onion", "pickles", "spinach", "cucumber"]
SANDWICH_SPREADS = ["mayonnaise", "mustard", "hummus", "pesto"]
SALAD_BASES = ["romaine lettuce", "spinach", "mixed greens", "kale"]
SALAD_PROTEINS = ["grilled chicken", "chickpeas",
                  "hard-boiled egg", "tuna", "deli turkey"]
SALAD_TOPPINGS = ["cucumbers", "tomatoes", "onions",
                  "croutons", "shredded cheese", "bell peppers"]
SALAD_DRESSINGS = ["ranch", "Caesar",
                   "vinaigrette", "Greek dressing", "balsamic"]
SOUP_BASES = ["vegetable broth", "chicken broth", "beef broth"]
SOUP_VEGGIES = ["onion", "garlic", "celery", "carrots"]
SOUP_MAINS = ["lentils", "black beans",
              "split peas", "diced potatoes", "mini pasta"]
BOWL_GRAINS = ["quinoa", "brown rice", "farro", "white rice"]
BOWL_PROTEINS = ["black beans", "chickpeas",
                 "grilled chicken", "tofu", "ground beef"]
BOWL_VEGGIES = ["roasted broccoli", "bell peppers",
                "corn", "avocado", "shredded carrots"]


def generate_recipe(recipe_id, existing_titles):
    recipe_type = random.choice(["Sandwich/Wrap", "Salad", "Soup", "Bowl"])
    title, ingredients_full, instructions, ingredients_clean = "", [], [], []
    if recipe_type == "Sandwich/Wrap":
        protein, bread, veggie, spread = map(random.choice, [
                                             SANDWICH_PROTEINS, SANDWICH_BREADS, SANDWICH_VEGGIES, SANDWICH_SPREADS])
        title = f"{protein.title()} {bread.split()[-1].title()}"
        if bread == "a tortilla wrap":
            title = f"{protein.title()} Wrap"
        ingredients_full = [
            f"2 slices of {bread}", f"4 oz. {protein}", f"1/4 c. {veggie}", f"1 Tbsp. {spread}"]
        instructions = [f"Toast {bread} if desired.", f"Spread {spread} on bread.",
                        f"Layer {protein} and {veggie}.", "Combine and serve."]
        ingredients_clean = [bread.replace(
            ' ', '_'), protein.replace(' ', '_'), veggie, spread]
    elif recipe_type == "Salad":
        base, protein, topping, dressing = map(
            random.choice, [SALAD_BASES, SALAD_PROTEINS, SALAD_TOPPINGS, SALAD_DRESSINGS])
        title = f"{protein.title()} Salad with {dressing.title()}"
        ingredients_full = [
            f"2 c. {base}", f"1 c. {protein}", f"1/4 c. {topping}", f"2 Tbsp. {dressing}"]
        instructions = [f"Combine {base}, {protein}, and {topping} in a large bowl.",
                        f"Drizzle with {dressing} and toss to combine."]
        ingredients_clean = [base.replace(
            ' ', '_'), protein.replace(' ', '_'), topping, dressing]
    elif recipe_type == "Soup":
        main, base, veg = map(
            random.choice, [SOUP_MAINS, SOUP_BASES, SOUP_VEGGIES])
        title = f"Simple {main.title()} and {veg.title()} Soup"
        ingredients_full = [f"4 c. {base}", f"1 c. {main}",
                            f"1/2 c. chopped {veg}", "salt and pepper"]
        instructions = [f"In a pot, bring {base} to a simmer.",
                        f"Add {main} and {veg}. Cook until tender.", "Season with salt and pepper."]
        ingredients_clean = [base.replace(' ', '_'), main.replace(
            ' ', '_'), veg, "salt", "pepper"]
    elif recipe_type == "Bowl":
        grain, protein, veg, sauce = map(random.choice, [BOWL_GRAINS, BOWL_PROTEINS, BOWL_VEGGIES, [
                                         "salsa", "tahini sauce", "yogurt sauce"]])
        title = f"{protein.title()} and {veg.title()} {grain.title()} Bowl"
        ingredients_full = [
            f"1 c. cooked {grain}", f"1/2 c. {protein}", f"1/2 c. {veg}", f"2 Tbsp. {sauce}"]
        instructions = [f"Place {grain} in the bottom of a bowl.",
                        f"Top with {protein} and {veg}.", f"Drizzle with {sauce} and serve."]
        ingredients_clean = [grain.replace(' ', '_'), protein.replace(
            ' ', '_'), veg.replace(' ', '_'), sauce.replace(' ', '_')]
    if title in existing_titles:
        title += f" ({random.randint(1, 99)})"
    return {'id': recipe_id, 'title': title, 'ingredients_full': ingredients_full, 'instructions': instructions, 'url': f"www.example-lunch.com/recipe/{recipe_id}", 'source': 'Generated', 'ingredients_clean': ingredients_clean}


def main_generate_csv(num_total_recipes=500):
    output_filepath = 'lunch_recipes_500.csv'
    from io import StringIO
    f = StringIO(BASE_RECIPES_CSV_CONTENT.strip())
    reader = csv.reader(f)
    base_recipes = [{'id': int(row[0]), 'title': row[1], 'ingredients_full': row[2], 'instructions': row[3],
                     'url': row[4], 'source': row[5], 'ingredients_clean': row[6]} for row in reader if row]
    all_generated_recipes = list(base_recipes)
    existing_titles = {recipe['title'] for recipe in base_recipes}
    current_id = len(base_recipes)
    while len(all_generated_recipes) < num_total_recipes:
        new_recipe = generate_recipe(current_id, existing_titles)
        all_generated_recipes.append(new_recipe)
        existing_titles.add(new_recipe['title'])
        current_id += 1
    with open(output_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for recipe in all_generated_recipes:
            writer.writerow([recipe['id'], recipe['title'], json.dumps(recipe['ingredients_full']), json.dumps(
                recipe['instructions']), recipe['url'], recipe['source'], json.dumps(recipe['ingredients_clean'])])
    print(
        f"Successfully generated {len(all_generated_recipes)} lunch recipes to '{output_filepath}'!")


if __name__ == '__main__':
    main_generate_csv(num_total_recipes=500)
