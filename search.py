# This file was created with assistance from Gemini

import pandas as pd
import ast

def find_recipe_by_id(file_path, target_id):
    """
    Scans a large CSV file in chunks to find a recipe by its ID.
    
    Args:
        file_path (str): The path to the recipe CSV file.
        target_id (int): The ID of the recipe to find.
    """
    chunk_size = 500000  # Process 50,000 rows at a time
    
    print(f"Searching for recipe with ID: {target_id}...")
    
    try:
        # Create an iterator that reads the CSV in chunks
        chunk_iterator = pd.read_csv(file_path, chunksize=chunk_size)
        
        # Loop through each chunk
        for chunk in chunk_iterator:
            result = chunk[chunk['id'] == target_id]
            
            # If a match is found...
            if not result.empty:
                print("Recipe found!")
                

                recipe_data = result.iloc[0].to_dict() # makes the data a dictionary
                
                # Print each attribute neatly
                for key, value in recipe_data.items():
                    # Converts string lists to actual lists for better display
                    if key in ['ingredients', 'directions', 'NER'] and isinstance(value, str):
                        value = ast.literal_eval(value)
                    
                    if key != 'id' and key != 'NER' and key != 'source':
                        print(f"\n--- {key.upper()} ---")
                        if isinstance(value, list):
                            for item in value:
                                print(f"- {item}")
                        else:
                            print(value)
                
                return # Exit the function since we found the recipe
                
        print("❌ Recipe ID not found in the dataset.")

    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def find_recipes_with_ingredients(file_path, user_ingredients):
    """
    Scans a large CSV to find all recipes that can be made with a given
    set of ingredients.

    Args:
        file_path (str): The path to the recipe CSV file.
        user_ingredients (list): A list of ingredients the user has.

    Returns:
        list: A list of integer IDs for all matching recipes.
    """

    matching_recipe_ids = []
    

    user_ingredients_set = set(user_ingredients)
    
    chunk_size = 50000 
    
    print(f"Searching for recipes with ingredients: {user_ingredients}...")
    
    try:
        chunk_iterator = pd.read_csv(file_path, chunksize=chunk_size)

        for i, chunk in enumerate(chunk_iterator):
            print(f"-> Processing chunk {i+1}...")
            
            def is_match(recipe_ner_list):
                try:
                    recipe_ingredients = ast.literal_eval(recipe_ner_list)
                    return set(recipe_ingredients).issubset(user_ingredients_set)
                except (ValueError, SyntaxError):
                    return False

            matches = chunk['NER'].apply(is_match)
            
            matched_ids_in_chunk = chunk[matches]['id'].tolist()
            
            if matched_ids_in_chunk:
                matching_recipe_ids.extend(matched_ids_in_chunk)

        print(f"\n✅ Found {len(matching_recipe_ids)} matching recipes.")
        return matching_recipe_ids

    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# --- USAGE ---
# Replace with the actual path to your downloaded CSV
# RECIPE_FILE = 'full_dataset.csv' 
RECIPE_FILE = 'tiny_dataset.csv'

# find_recipe_by_id(RECIPE_FILE, ID_TO_FIND)
recipes = find_recipes_with_ingredients(RECIPE_FILE, ["flour", "sugar", "baking powder", "yeast", "buttermilk", "soda", "margarine", "warm water"])
for recipe in recipes:
    find_recipe_by_id(RECIPE_FILE, recipe)