import pandas as pd
import ast # Used to safely evaluate string-formatted lists 

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
            # Check if the target ID is in the current chunk's 'id' column
            result = chunk[chunk['id'] == target_id]
            
            # If a match is found...
            if not result.empty:
                print("Recipe found!")
                
                # Extract the recipe's data as a dictionary
                recipe_data = result.iloc[0].to_dict()
                
                # Print each attribute neatly
                for key, value in recipe_data.items():
                    # Safely convert string lists to actual lists for better display
                    if key in ['ingredients', 'directions', 'NER'] and isinstance(value, str):
                        value = ast.literal_eval(value)
                    
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
    # Create an empty list to store the IDs of matching recipes
    matching_recipe_ids = []
    
    # Convert the user's ingredients to a set for fast checking
    user_ingredients_set = set(user_ingredients)
    
    chunk_size = 50000  # Process 50,000 rows at a time
    
    print(f"Searching for recipes with ingredients: {user_ingredients}...")
    
    try:
        # Create an iterator that reads the CSV in chunks
        chunk_iterator = pd.read_csv(file_path, chunksize=chunk_size)
        
        # Loop through each chunk
        for i, chunk in enumerate(chunk_iterator):
            print(f"-> Processing chunk {i+1}...")
            
            # This function will check one row at a time
            def is_match(recipe_ner_list):
                try:
                    # Safely convert the string '["salt", "pepper"]' to a list
                    recipe_ingredients = ast.literal_eval(recipe_ner_list)
                    # Check if the recipe's ingredients are all in the user's pantry
                    return set(recipe_ingredients).issubset(user_ingredients_set)
                except (ValueError, SyntaxError):
                    # Handle cases where the cell might be empty or malformed
                    return False

            # Apply the function to the 'NER' column to find all matches in the chunk
            # This creates a boolean Series (True for matches, False for non-matches)
            matches = chunk['NER'].apply(is_match)
            
            # Get the IDs from the rows where 'matches' is True
            matched_ids_in_chunk = chunk[matches]['id'].tolist()
            
            # Add the found IDs to our main list
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
#RECIPE_FILE = 'full_dataset.csv' 
# RECIPE_FILE = 'tiny_dataset.csv'

# find_recipe_by_id(RECIPE_FILE, ID_TO_FIND)
# recipes = find_recipes_with_ingredients(RECIPE_FILE, ["flour", "sugar", "baking powder", "yeast", "buttermilk", "soda", "margarine", "warm water"])
# for recipe in recipes:
#     find_recipe_by_id(RECIPE_FILE, recipe)