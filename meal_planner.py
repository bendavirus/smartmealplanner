
# meal_planner.py

# Import the ingredient parser we created earlier.
from ingredient_parser import parse_ingredient


# Convert calculated quantities into readable numbers.
def format_quantity(quantity):

    # If the number is a whole number, remove the decimal.
    if quantity == int(quantity):
        return str(int(quantity))

    # Otherwise, show up to 2 decimal places.
    return str(round(quantity, 2))


# Calculate new ingredient quantities for a different
# number of servings.
def scale_ingredients(ingredients, original_servings, new_servings):

    # Make sure the serving numbers are valid.
    if original_servings <= 0 or new_servings <= 0:
        return []

    # Calculate how much the recipe needs to increase or decrease.
    multiplier = new_servings / original_servings

    # This list will store the adjusted ingredients.
    updated_ingredients = []

    # Go through every ingredient in the recipe.
    for ingredient in ingredients:

        # Get the original measurement and ingredient name.
        measure = ingredient["measure"]
        name = ingredient["name"]

        # Use the ingredient parser to separate the measurement.
        parsed = parse_ingredient(measure + " " + name)

        # Check whether the measurement contains a quantity.
        if parsed["quantity"] == "":
            # Keep ingredients without a number unchanged.
            updated_ingredients.append({
                "quantity": "",
                "unit": "",
                "name": name,
                "measure": measure
            })

        else:
            # Multiply the original quantity by the multiplier.
            new_quantity = float(parsed["quantity"]) * multiplier

            # Make the new quantity easier to read.
            new_quantity = format_quantity(new_quantity)

            # Save the updated ingredient.
            updated_ingredients.append({
                "quantity": new_quantity,
                "unit": parsed["unit"],
                "name": parsed["name"],
                "measure": new_quantity + " " + parsed["unit"]
            })

    # Return all the adjusted ingredients.
    return updated_ingredients

# The seven days available in our weekly meal planner.
DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

# The three meal types for each day.
MEAL_TYPES = ["Breakfast", "Lunch", "Dinner"]


# Create an empty weekly meal plan.
# Each day starts with three empty meal slots.
weekly_plan = {}

for day in DAYS:
    weekly_plan[day] = {
        "Breakfast": "",
        "Lunch": "",
        "Dinner": ""
    }


# Add a recipe to a particular day and meal type.
def add_meal_to_plan(day, meal_type, recipe_name):

    # Check that the selected day is valid.
    if day not in DAYS:
        return False

    # Check that the selected meal type is valid.
    if meal_type not in MEAL_TYPES:
        return False

    # Check that a recipe name was provided.
    if recipe_name.strip() == "":
        return False

    # Save the recipe in the correct position.
    weekly_plan[day][meal_type] = recipe_name

    return True


# Create a readable version of the weekly meal plan.
def get_weekly_plan():

    # Start with the title.
    plan_text = "========== WEEKLY MEAL PLAN ==========\n"

    # Go through each day of the week.
    for day in DAYS:

        plan_text += "\n" + day + "\n"

        # Display breakfast, lunch and dinner.
        for meal_type in MEAL_TYPES:

            # Get the recipe saved for this meal.
            recipe_name = weekly_plan[day][meal_type]

            # Display an empty message if no recipe is saved.
            if recipe_name == "":
                recipe_name = "Not planned"

            plan_text += meal_type + ": " + recipe_name + "\n"

    return plan_text
