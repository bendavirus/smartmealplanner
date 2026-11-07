# mealdb_client.py

# Import the requests library.
# We use it to communicate with online APIs.
import requests

# Import our Recipe class.
from recipe import Recipe


# This class handles all communication with TheMealDB API.
class MealDBClient:

    # TheMealDB API address.
    BASE_URL = "https://www.themealdb.com/api/json/v1/1/"

    # This method searches for a meal using its name.
    def search_by_name(self, meal_name):

        # Build the API address.
        url = self.BASE_URL + "search.php"

        # Send the meal name as a search parameter.
        parameters = {"s": meal_name}

        try:
            # Send a GET request to the API.
            response = requests.get(
                url,
                params=parameters,
                timeout=15
            )

            # Check whether the request was successful.
            response.raise_for_status()

            # Convert the API response into Python data.
            data = response.json()

            # Get the list of meals from the response.
            meals = data.get("meals")

            # Check whether any meals were found.
            if not meals:
                print("Sorry, no recipe was found.")
                return []

            # Create an empty list to store Recipe objects.
            recipes = []

            # Go through every meal returned by the API.
            for meal in meals:

                # Create an empty list for the ingredients.
                ingredients = []

                # TheMealDB stores ingredients in numbered fields.
                # For example: strIngredient1, strIngredient2, etc.
                for number in range(1, 21):

                    ingredient_name = meal.get(
                        f"strIngredient{number}"
                    )

                    ingredient_measure = meal.get(
                        f"strMeasure{number}"
                    )

                    # Check that the ingredient name is not empty.
                    if ingredient_name and ingredient_name.strip():

                        # Add the ingredient and its measurement.
                        ingredients.append({
                            "name": ingredient_name.strip(),
                            "measure": (ingredient_measure or "").strip()
                        })

                # Create a Recipe object using the API information.
                recipe = Recipe(
                    recipe_id=meal.get("idMeal"),
                    name=meal.get("strMeal"),
                    category=meal.get("strCategory"),
                    cuisine=meal.get("strArea"),
                    instructions=meal.get("strInstructions"),
                    ingredients=ingredients,
                    image=meal.get("strMealThumb")
                )

                # Add the recipe object to our recipes list.
                recipes.append(recipe)

            # Return all the recipes found.
            return recipes

        except requests.exceptions.Timeout:
            print("The request took too long. Please try again.")
            return []

        except requests.exceptions.RequestException as error:
            print("API connection error:", error)
            return []

        except ValueError:
            print("The API returned an invalid response.")
            return []