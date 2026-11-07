
# file_manager.py

# Import modules for working with files and JSON.
import json
import os
import csv


# Create the location where our weekly plan will be stored.
DATA_FOLDER = os.path.join(
    os.path.dirname(__file__),
    "data"
)

# Set the name of our JSON file.
WEEKLY_PLAN_FILE = os.path.join(
    DATA_FOLDER,
    "weekly_plan.json"
)


# Save the weekly meal plan.
def save_weekly_plan(weekly_plan):

    try:
        # Create the data folder if it does not exist.
        os.makedirs(DATA_FOLDER, exist_ok=True)

        # Open the JSON file in write mode.
        with open(WEEKLY_PLAN_FILE, "w", encoding="utf-8") as file:

            # Convert the Python dictionary into JSON.
            json.dump(
                weekly_plan,
                file,
                indent=4
            )

        return True

    except (OSError, TypeError) as error:

        # Display the error in the terminal.
        print("Error saving weekly plan:", error)

        return False


# Load the saved weekly meal plan.
def load_weekly_plan():

    try:
        # Open the saved JSON file.
        with open(WEEKLY_PLAN_FILE, "r", encoding="utf-8") as file:

            # Convert the JSON data back into a Python dictionary.
            weekly_plan = json.load(file)

        return weekly_plan

    except FileNotFoundError:

        # If no saved plan exists, return an empty dictionary.
        return {}

    except (OSError, json.JSONDecodeError) as error:

        # Display an error if the file cannot be read.
        print("Error loading weekly plan:", error)

        return {}

# Export a shopping list to a CSV file.
def export_shopping_list(shopping_list):

    # Create the exports folder inside the project.
    export_folder = os.path.join(
        os.path.dirname(__file__),
        "exports"
    )

    try:
        # Create the folder if it does not exist.
        os.makedirs(export_folder, exist_ok=True)

        # Set the CSV file location.
        csv_file = os.path.join(
            export_folder,
            "shopping_list.csv"
        )

        # Open the file in write mode.
        with open(csv_file, "w", newline="", encoding="utf-8") as file:

            # Create a CSV writer.
            writer = csv.writer(file)

            # Write the column headings.
            writer.writerow(["No.", "Ingredient"])

            # Write each shopping list item.
            for number, item in enumerate(shopping_list, start=1):
                writer.writerow([number, item])

        return csv_file

    except OSError as error:

        # Display the error in the terminal.
        print("Error exporting shopping list:", error)

        return None
