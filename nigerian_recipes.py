# nigerian_recipes.py

# Import the Recipe class we created earlier.
from recipe import Recipe


# Store our Nigerian recipes in a list.
NIGERIAN_DISHES = [

    # RECIPE 1: JOLLOF RICE
    Recipe(
        "NG001",
        "Jollof Rice",
        "Rice",
        "Nigerian",
        "1. Blend tomatoes, peppers and onions.\n"
        "2. Fry the mixture with oil and seasoning.\n"
        "3. Add rice and stock.\n"
        "4. Cover and cook until the rice is soft.\n"
        "5. Stir and serve.",
        [
            {"name": "Rice", "measure": "3 cups"},
            {"name": "Tomatoes", "measure": "5 medium"},
            {"name": "Red bell pepper", "measure": "2"},
            {"name": "Onion", "measure": "2"},
            {"name": "Vegetable oil", "measure": "1/2 cup"},
            {"name": "Tomato paste", "measure": "3 tbsp"},
            {"name": "Stock", "measure": "4 cups"},
            {"name": "Seasoning cubes", "measure": "2"},
            {"name": "Thyme", "measure": "1 tsp"}
        ],
        ""
    ),

    # RECIPE 2: EGUSI SOUP
    Recipe(
        "NG002",
        "Egusi Soup",
        "Soup",
        "Nigerian",
        "1. Blend or grind the melon seeds.\n"
        "2. Prepare your meat and stockfish.\n"
        "3. Heat palm oil in a pot.\n"
        "4. Add the egusi mixture and cook.\n"
        "5. Add meat, stock and seasoning.\n"
        "6. Add vegetables and simmer until ready.",
        [
            {"name": "Ground egusi", "measure": "2 cups"},
            {"name": "Palm oil", "measure": "1/2 cup"},
            {"name": "Spinach or ugu", "measure": "2 cups"},
            {"name": "Beef", "measure": "500 g"},
            {"name": "Stockfish", "measure": "1 cup"},
            {"name": "Onion", "measure": "1"},
            {"name": "Pepper", "measure": "2"},
            {"name": "Seasoning cubes", "measure": "2"}
        ],
        ""
    ),

    # RECIPE 3: EFO RIRO
    Recipe(
        "NG003",
        "Efo Riro",
        "Soup",
        "Nigerian",
        "1. Wash and slice the vegetables.\n"
        "2. Blend tomatoes, pepper and onions.\n"
        "3. Heat palm oil and fry the pepper mixture.\n"
        "4. Add cooked meat and seasoning.\n"
        "5. Add the vegetables and stir.\n"
        "6. Allow to simmer briefly and serve.",
        [
            {"name": "Spinach or ugu", "measure": "4 cups"},
            {"name": "Tomatoes", "measure": "4"},
            {"name": "Red bell pepper", "measure": "2"},
            {"name": "Palm oil", "measure": "1/3 cup"},
            {"name": "Beef", "measure": "400 g"},
            {"name": "Onion", "measure": "1"},
            {"name": "Seasoning cubes", "measure": "2"}
        ],
        ""
    ),

    # RECIPE 4: MOI MOI
    Recipe(
        "NG004",
        "Moi Moi",
        "Snack",
        "Nigerian",
        "1. Soak beans and remove their outer skins.\n"
        "2. Blend beans with pepper and onions.\n"
        "3. Add seasoning, oil and water.\n"
        "4. Pour the mixture into containers.\n"
        "5. Steam until firm and fully cooked.",
        [
            {"name": "Beans", "measure": "2 cups"},
            {"name": "Red bell pepper", "measure": "2"},
            {"name": "Onion", "measure": "1"},
            {"name": "Vegetable oil", "measure": "1/4 cup"},
            {"name": "Seasoning cubes", "measure": "2"},
            {"name": "Salt", "measure": "1 tsp"}
        ],
        ""
    ),

    # RECIPE 5: SUYA
    Recipe(
        "NG005",
        "Suya",
        "Grilled Meat",
        "Nigerian",
        "1. Cut beef into thin strips.\n"
        "2. Mix ground peanut spice with seasoning.\n"
        "3. Coat the beef with the spice mixture.\n"
        "4. Thread the beef onto skewers.\n"
        "5. Grill until fully cooked.\n"
        "6. Serve with sliced onions and tomatoes.",
        [
            {"name": "Beef", "measure": "500 g"},
            {"name": "Ground peanut", "measure": "1 cup"},
            {"name": "Paprika", "measure": "1 tbsp"},
            {"name": "Ground ginger", "measure": "1 tsp"},
            {"name": "Onion", "measure": "1"},
            {"name": "Salt", "measure": "1 tsp"}
        ],
        ""
    ),

    # RECIPE 6: NIGERIAN PEPPER SOUP
    Recipe(
        "NG006",
        "Nigerian Pepper Soup",
        "Soup",
        "Nigerian",
        "1. Wash and season the meat.\n"
        "2. Place the meat in a pot with water.\n"
        "3. Add pepper soup spice and ground pepper.\n"
        "4. Cook until the meat is tender.\n"
        "5. Add scent leaves and simmer briefly.\n"
        "6. Serve hot.",
        [
            {"name": "Goat meat", "measure": "500 g"},
            {"name": "Pepper soup spice", "measure": "2 tbsp"},
            {"name": "Ground pepper", "measure": "1 tsp"},
            {"name": "Scent leaves", "measure": "1 cup"},
            {"name": "Onion", "measure": "1"},
            {"name": "Seasoning cubes", "measure": "2"}
        ],
        ""
    ),

    # RECIPE 7: NIGERIAN FRIED RICE
    Recipe(
        "NG007",
        "Nigerian Fried Rice",
        "Rice",
        "Nigerian",
        "1. Cook rice until almost tender.\n"
        "2. Dice carrots, green beans and onions.\n"
        "3. Heat oil in a frying pan.\n"
        "4. Add vegetables and stir-fry.\n"
        "5. Add rice, seasoning and curry powder.\n"
        "6. Stir well and cook until ready.",
        [
            {"name": "Rice", "measure": "3 cups"},
            {"name": "Carrots", "measure": "2"},
            {"name": "Green beans", "measure": "1 cup"},
            {"name": "Sweet corn", "measure": "1 cup"},
            {"name": "Green pepper", "measure": "1"},
            {"name": "Vegetable oil", "measure": "1/4 cup"},
            {"name": "Curry powder", "measure": "1 tsp"},
            {"name": "Seasoning cubes", "measure": "2"}
        ],
        ""
    ),

    # RECIPE 8: AKARA
    Recipe(
        "NG008",
        "Akara",
        "Snack",
        "Nigerian",
        "1. Soak beans and remove the outer skins.\n"
        "2. Blend the beans with pepper and onion.\n"
        "3. Add salt and mix until fluffy.\n"
        "4. Heat vegetable oil in a frying pan.\n"
        "5. Scoop the mixture into the hot oil.\n"
        "6. Fry until golden brown and cooked through.",
        [
            {"name": "Beans", "measure": "2 cups"},
            {"name": "Onion", "measure": "1"},
            {"name": "Pepper", "measure": "2"},
            {"name": "Salt", "measure": "1 tsp"},
            {"name": "Vegetable oil", "measure": "2 cups"}
        ],
        ""
    )
]


# This function searches our Nigerian recipe collection.
def search_nigerian_recipes(search_term):

    # Create an empty list for matching recipes.
    matching_recipes = []

    # Convert the search word to lowercase.
    search_term = search_term.lower().strip()

    # Go through every Nigerian recipe.
    for recipe in NIGERIAN_DISHES:

        # Check the recipe name, category and cuisine.
        if (search_term in recipe.name.lower()
                or search_term in recipe.category.lower()
                or search_term in recipe.cuisine.lower()):

            # Add the matching recipe.
            matching_recipes.append(recipe)

        else:

            # Search through the recipe ingredients.
            for ingredient in recipe.ingredients:

                # Check whether the search word matches an ingredient.
                if search_term in ingredient["name"].lower():

                    matching_recipes.append(recipe)

                    # Stop checking this recipe after a match.
                    break

    # Return all matching recipes.
    return matching_recipes


# This function returns all Nigerian recipes.
def get_nigerian_recipes():

    return NIGERIAN_DISHES