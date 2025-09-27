def IngredientsInput():
        ingredients = []
        print("Enter your ingredients one at a time (type 'done!' to finish):")

        while True:
                item = input("Ingredient: ").strip().lower()
                if item == 'done':
                    break
        
                if item.isnumeric():   
                    print("Error: ingredient names cannot be numbers. Please enter text.")
                    continue  
                
                if item:
                    ingredients.append(item)
                
        return ingredients
ingredients = IngredientsInput()
print(ingredients)