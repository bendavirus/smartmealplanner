
# shopping_list.py

# Generate a shopping list from selected recipes.
def generate_shopping_list(selected_recipes):

    # This list will contain all the ingredients.
    shopping_list = []

    # Go through each selected recipe.
    for recipe in selected_recipes:

        # Go through the ingredients in that recipe.
        for ingredient in recipe.ingredients:

            # Get the ingredient measurement.
            measure = ingredient["measure"]

            # Get the ingredient name.
            name = ingredient["name"]

            # Create a readable shopping list item.
            item = measure + " " + name

            # Add the item to our shopping list.
            shopping_list.append(item)

    # Return the completed shopping list.
    return shopping_list


# Display the shopping list in a readable format.
def display_shopping_list(shopping_list):

    # Start with a shopping list heading.
    result = "========== SHOPPING LIST ==========\n"

    # Add each ingredient as a numbered item.
    for number, item in enumerate(shopping_list, start=1):

        result += str(number) + ". " + item + "\n"

    # Return the completed text.
    return result
