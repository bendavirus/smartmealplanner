# recipe.py

# This class is a blueprint for storing recipe information.

class Recipe:

    # The constructor runs whenever we create a new Recipe object.
    #the __init__ is a constructor method that automatically runs
    #when we create a new object (Recipe)
    def __init__(self, recipe_id, name, category, cuisine,
                 instructions, ingredients, image):

        # Store the recipe information inside the object.

        #The word self refers to the particular recipe object #
        # being created.
        self.recipe_id = recipe_id
        self.name = name
        self.category = category
        self.cuisine = cuisine
        self.instructions = instructions
        self.ingredients = ingredients
        self.image = image

    # This method displays the recipe information.
    def display_recipe(self):

        print("\n========== RECIPE DETAILS ==========")

        print("Recipe Name:", self.name)
        print("Category:", self.category)
        print("Cuisine:", self.cuisine)

        print("\nIngredients:")

        # Go through each ingredient and its measurement.
        #This loop goes through the ingredients one by one 
        # #and displays their measurements and names.
        for ingredient in self.ingredients:
            print("-", ingredient["measure"], ingredient["name"])

        print("\nCooking Instructions:")
        print(self.instructions)

        print("====================================")