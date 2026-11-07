# ==========================================
# SMART MEAL PLANNER
# Main application file
# ==========================================

# Import the libraries we need.
import tkinter as tk
from tkinter import messagebox, ttk
import threading

# Import our project classes and functions.
from mealdb_client import MealDBClient
from gemini_assistant import ask_gemini

from shopping_list import (
    generate_shopping_list,
    display_shopping_list
)

from meal_planner import (
    scale_ingredients,
    add_meal_to_plan,
    get_weekly_plan,
    weekly_plan,
    DAYS,
    MEAL_TYPES
)

from nigerian_recipes import (
    get_nigerian_recipes,
    search_nigerian_recipes
)

from file_manager import (
    save_weekly_plan,
    load_weekly_plan,
    export_shopping_list
)


# ==========================================
# SECTION 1: APPLICATION SETTINGS
# ==========================================

# Create the recipe database client.
meal_client = MealDBClient()

# This list stores the recipes currently displayed.
recipes = []

# Our recipes use 2 servings as the starting quantity.
original_servings = 2


# Load a previously saved weekly meal plan.
saved_plan = load_weekly_plan()

if saved_plan:
    weekly_plan.update(saved_plan)


# ==========================================
# SECTION 2: CREATE THE MAIN WINDOW
# ==========================================

root = tk.Tk()

root.title("Smart Meal Planner")
root.geometry("1000x900")
root.minsize(800, 500)


# ==========================================
# SECTION 3: MAKE THE WINDOW SCROLLABLE
# ==========================================

# Create a canvas to hold the application content.
main_canvas = tk.Canvas(root)

# Create a scrollbar for the canvas.
main_scrollbar = tk.Scrollbar(
    root,
    orient="vertical",
    command=main_canvas.yview
)

# Connect the scrollbar to the canvas.
main_canvas.configure(
    yscrollcommand=main_scrollbar.set
)

# Display the canvas and scrollbar.
main_scrollbar.pack(side="right", fill="y")
main_canvas.pack(side="left", fill="both", expand=True)

# Create the frame that will contain all application widgets.
content_frame = tk.Frame(main_canvas)

# Put the content frame inside the canvas.
canvas_window = main_canvas.create_window(
    (0, 0),
    window=content_frame,
    anchor="nw"
)


# Update the scrollable area whenever the content changes.
def update_scroll_region(event):
    main_canvas.configure(
        scrollregion=main_canvas.bbox("all")
    )


content_frame.bind(
    "<Configure>",
    update_scroll_region
)


# Make the content frame fit the width of the window.
def resize_content(event):
    main_canvas.itemconfigure(
        canvas_window,
        width=event.width
    )


main_canvas.bind(
    "<Configure>",
    resize_content
)


# Allow scrolling with the mouse wheel on Windows.
def scroll_with_mouse(event):
    main_canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


main_canvas.bind_all(
    "<MouseWheel>",
    scroll_with_mouse
)


# ==========================================
# SECTION 4: APPLICATION FUNCTIONS
# ==========================================

# ------------------------------------------
# FUNCTION 1: SEARCH FOR RECIPES
# ------------------------------------------

def search_recipe():

    # Get the user's search word.
    meal_name = search_entry.get().strip()

    if meal_name == "":
        messagebox.showwarning(
            "Empty Search",
            "Please enter a meal name."
        )
        return

    # Clear previous search results.
    results_listbox.delete(0, tk.END)
    details_text.delete("1.0", tk.END)

    status_label.config(
        text="Searching for recipes..."
    )

    # Search Nigerian recipes first.
    local_recipes = search_nigerian_recipes(meal_name)

    # Search the online recipe database.
    online_recipes = meal_client.search_by_name(meal_name)

    # Combine both results.
    global recipes
    recipes = local_recipes + online_recipes

    # Display the results.
    if recipes:

        for recipe in recipes:
            results_listbox.insert(
                tk.END,
                recipe.name
            )

        status_label.config(
            text=str(len(recipes)) + " recipe(s) found."
        )

    else:

        status_label.config(
            text="No recipes found."
        )

        messagebox.showinfo(
            "Search Results",
            "No recipes found. Try another search."
        )


# ------------------------------------------
# FUNCTION 2: DISPLAY NIGERIAN DISHES
# ------------------------------------------

def show_nigerian_dishes():

    global recipes

    # Get all Nigerian recipes.
    recipes = get_nigerian_recipes()

    # Clear previous results.
    results_listbox.delete(0, tk.END)
    details_text.delete("1.0", tk.END)

    # Display Nigerian recipe names.
    for recipe in recipes:
        results_listbox.insert(
            tk.END,
            recipe.name
        )

    status_label.config(
        text="Nigerian dishes: "
        + str(len(recipes))
        + " recipes available."
    )


# ------------------------------------------
# FUNCTION 3: DISPLAY RECIPE DETAILS
# ------------------------------------------

def show_recipe(event=None):

    selected_position = results_listbox.curselection()

    if not selected_position:
        return

    # Get the selected recipe.
    recipe_index = selected_position[0]
    selected_recipe = recipes[recipe_index]

    # Clear the details area.
    details_text.delete("1.0", tk.END)

    # Display the recipe name.
    details_text.insert(
        tk.END,
        "RECIPE: " + selected_recipe.name + "\n\n"
    )

    # Display the category.
    details_text.insert(
        tk.END,
        "Category: " + str(selected_recipe.category) + "\n"
    )

    # Display the cuisine.
    details_text.insert(
        tk.END,
        "Cuisine: " + str(selected_recipe.cuisine) + "\n\n"
    )

    # Display the ingredients.
    details_text.insert(
        tk.END,
        "INGREDIENTS:\n"
    )

    for ingredient in selected_recipe.ingredients:

        details_text.insert(
            tk.END,
            "- " + ingredient["measure"]
            + " " + ingredient["name"] + "\n"
        )

    # Display cooking instructions.
    details_text.insert(
        tk.END,
        "\nCOOKING INSTRUCTIONS:\n"
    )

    details_text.insert(
        tk.END,
        str(selected_recipe.instructions)
    )

    status_label.config(
        text="Displaying " + selected_recipe.name
    )


# ------------------------------------------
# FUNCTION 4: CHANGE RECIPE SERVINGS
# ------------------------------------------

def change_servings():

    # Check whether a recipe has been selected.
    selected = results_listbox.curselection()

    if not selected:

        messagebox.showwarning(
            "No Recipe Selected",
            "Please select a recipe first."
        )
        return

    # Get the new serving size.
    try:

        new_servings = int(servings_entry.get())

        if new_servings <= 0:

            messagebox.showwarning(
                "Invalid Servings",
                "Please enter a number greater than zero."
            )
            return

    except ValueError:

        messagebox.showwarning(
            "Invalid Input",
            "Please enter a whole number, such as 4 or 6."
        )
        return

    # Get the selected recipe.
    selected_index = selected[0]
    selected_recipe = recipes[selected_index]

    # Calculate the adjusted ingredient quantities.
    updated_ingredients = scale_ingredients(
        selected_recipe.ingredients,
        original_servings,
        new_servings
    )

    # Clear the details area.
    details_text.delete("1.0", tk.END)

    # Display the recipe information.
    details_text.insert(
        tk.END,
        "RECIPE: " + selected_recipe.name + "\n"
    )

    details_text.insert(
        tk.END,
        "Cuisine: " + str(selected_recipe.cuisine) + "\n"
    )

    details_text.insert(
        tk.END,
        "Servings: " + str(new_servings) + "\n"
    )

    # Display the adjusted ingredients.
    details_text.insert(
        tk.END,
        "\nADJUSTED INGREDIENTS:\n"
    )

    for ingredient in updated_ingredients:

        details_text.insert(
            tk.END,
            "- " + ingredient["measure"]
            + " " + ingredient["name"] + "\n"
        )

    # Display the cooking instructions.
    details_text.insert(
        tk.END,
        "\nCOOKING INSTRUCTIONS:\n"
    )

    details_text.insert(
        tk.END,
        str(selected_recipe.instructions)
    )

    status_label.config(
        text="Ingredients adjusted for "
        + str(new_servings)
        + " servings."
    )


# ------------------------------------------
# FUNCTION 5: SAVE A MEAL TO THE WEEKLY PLAN
# ------------------------------------------

def save_weekly_meal():

    selected_day = day_choice.get()
    selected_meal = meal_choice.get()
    recipe_name = weekly_recipe_entry.get().strip()

    # Add the meal to the weekly plan.
    success = add_meal_to_plan(
        selected_day,
        selected_meal,
        recipe_name
    )

    if success:

        messagebox.showinfo(
            "Meal Saved",
            recipe_name + " has been added to "
            + selected_day + " " + selected_meal + "."
        )

        weekly_recipe_entry.delete(0, tk.END)

    else:

        messagebox.showwarning(
            "Invalid Information",
            "Please enter a recipe name and select a valid day and meal."
        )


# ------------------------------------------
# FUNCTION 6: DISPLAY THE WEEKLY PLAN
# ------------------------------------------

def display_weekly_plan():

    plan = get_weekly_plan()

    details_text.delete("1.0", tk.END)
    details_text.insert(tk.END, plan)

    status_label.config(
        text="Your weekly meal plan is displayed."
    )


# ------------------------------------------
# FUNCTION 7: SAVE THE WEEKLY PLAN
# ------------------------------------------

def save_plan_to_file():

    successful = save_weekly_plan(weekly_plan)

    if successful:

        messagebox.showinfo(
            "Saved",
            "Your weekly meal plan has been saved!"
        )

    else:

        messagebox.showerror(
            "Save Error",
            "The weekly meal plan could not be saved."
        )


# ------------------------------------------
# FUNCTION 8: FIND RECIPES IN THE WEEKLY PLAN
# ------------------------------------------

def get_recipes_from_weekly_plan():

    # Get all Nigerian recipes.
    available_recipes = get_nigerian_recipes()

    # Include recipes from the current search results.
    available_recipes = available_recipes + recipes

    # Create a dictionary for finding recipes by name.
    recipe_dictionary = {}

    for recipe in available_recipes:
        recipe_dictionary[recipe.name.lower()] = recipe

    selected_recipes = []
    added_names = []

    # Go through every day and meal.
    for day in DAYS:

        for meal_type in MEAL_TYPES:

            recipe_name = weekly_plan[day][meal_type]

            if recipe_name != "":

                recipe_key = recipe_name.lower()

                # Avoid adding the same recipe twice.
                if recipe_key not in added_names:

                    recipe = recipe_dictionary.get(recipe_key)

                    if recipe is not None:

                        selected_recipes.append(recipe)
                        added_names.append(recipe_key)

    return selected_recipes


# ------------------------------------------
# FUNCTION 9: GENERATE A SHOPPING LIST
# ------------------------------------------

def generate_weekly_shopping_list():

    # Find the recipes in the weekly plan.
    selected_recipes = get_recipes_from_weekly_plan()

    if not selected_recipes:

        messagebox.showwarning(
            "No Recipes Found",
            "Your weekly plan does not contain any recognised recipes."
        )
        return

    # Generate the shopping list.
    shopping_items = generate_shopping_list(
        selected_recipes
    )

    # Format the shopping list.
    shopping_text = display_shopping_list(
        shopping_items
    )

    # Display the shopping list.
    details_text.delete("1.0", tk.END)
    details_text.insert(tk.END, shopping_text)

    status_label.config(
        text="Shopping list generated from your weekly meal plan."
    )


# ------------------------------------------
# FUNCTION 10: EXPORT THE SHOPPING LIST
# ------------------------------------------

def export_weekly_shopping_list():

    # Get the recipes in the weekly plan.
    selected_recipes = get_recipes_from_weekly_plan()

    if not selected_recipes:

        messagebox.showwarning(
            "Empty Shopping List",
            "Please add recognised recipes to your weekly plan first."
        )
        return

    # Generate the shopping list.
    shopping_items = generate_shopping_list(
        selected_recipes
    )

    # Export it to a CSV file.
    file_path = export_shopping_list(
        shopping_items
    )

    if file_path:

        messagebox.showinfo(
            "Export Successful",
            "Your shopping list has been exported!\n\n"
            + str(file_path)
        )

    else:

        messagebox.showerror(
            "Export Failed",
            "Could not export your shopping list."
        )


# ------------------------------------------
# FUNCTION 11: DISPLAY GEMINI'S ANSWER
# ------------------------------------------

def display_ai_answer(answer):

    ai_answer_text.delete("1.0", tk.END)
    ai_answer_text.insert(tk.END, answer)

    # Allow the user to ask another question.
    ai_ask_button.config(state="normal")


# ------------------------------------------
# FUNCTION 12: RUN GEMINI IN THE BACKGROUND
# ------------------------------------------

def get_ai_answer(question):

    try:

        answer = ask_gemini(question)

    except Exception as error:

        answer = (
            "Sorry, something went wrong: "
            + str(error)
        )

    # Update the Tkinter window safely.
    root.after(
        0,
        display_ai_answer,
        answer
    )


# ------------------------------------------
# FUNCTION 13: ASK THE AI ASSISTANT
# ------------------------------------------

def ask_ai_assistant():

    question = ai_question_entry.get().strip()

    if question == "":

        display_ai_answer(
            "Please enter a question first."
        )
        return

    # Display a waiting message.
    ai_answer_text.delete("1.0", tk.END)

    ai_answer_text.insert(
        tk.END,
        "Thinking... Please wait."
    )

    # Prevent repeated clicks.
    ai_ask_button.config(state="disabled")

    # Start the request in a background thread.
    ai_thread = threading.Thread(
        target=get_ai_answer,
        args=(question,),
        daemon=True
    )

    ai_thread.start()


# ==========================================
# SECTION 5: APPLICATION HEADING
# ==========================================

header_frame = tk.Frame(
    content_frame,
    pady=15
)

header_frame.pack(fill="x")

title_label = tk.Label(
    header_frame,
    text="SMART MEAL PLANNER",
    font=("Arial", 20, "bold")
)

title_label.pack()

subtitle_label = tk.Label(
    header_frame,
    text="Search for recipes and discover delicious meals",
    font=("Arial", 10)
)

subtitle_label.pack()


# ==========================================
# SECTION 6: RECIPE SEARCH AREA
# ==========================================

search_frame = tk.Frame(
    content_frame,
    pady=10
)

search_frame.pack(
    fill="x",
    padx=20
)

search_label = tk.Label(
    search_frame,
    text="Enter meal name:",
    font=("Arial", 11)
)

search_label.pack(side="left")

search_entry = tk.Entry(
    search_frame,
    width=35,
    font=("Arial", 11)
)

search_entry.pack(
    side="left",
    padx=10
)

search_button = tk.Button(
    search_frame,
    text="Search",
    command=search_recipe,
    bg="green",
    fg="white",
    font=("Arial", 10, "bold")
)

search_button.pack(side="left")

nigerian_button = tk.Button(
    search_frame,
    text="Nigerian Dishes",
    command=show_nigerian_dishes,
    bg="orange",
    fg="black",
    font=("Arial", 10, "bold")
)

nigerian_button.pack(
    side="left",
    padx=5
)


# ==========================================
# SECTION 7: SEARCH RESULTS
# ==========================================

results_label = tk.Label(
    content_frame,
    text="SEARCH RESULTS",
    font=("Arial", 12, "bold")
)

results_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

results_frame = tk.Frame(content_frame)

results_frame.pack(
    fill="x",
    padx=20
)

results_listbox = tk.Listbox(
    results_frame,
    height=6,
    font=("Arial", 11)
)

results_listbox.pack(
    side="left",
    fill="both",
    expand=True
)

results_scrollbar = tk.Scrollbar(
    results_frame,
    command=results_listbox.yview
)

results_scrollbar.pack(
    side="right",
    fill="y"
)

results_listbox.config(
    yscrollcommand=results_scrollbar.set
)

# Display recipe details when a recipe is selected.
results_listbox.bind(
    "<<ListboxSelect>>",
    show_recipe
)


# ==========================================
# SECTION 8: SERVING-SIZE CALCULATOR
# ==========================================

servings_frame = tk.LabelFrame(
    content_frame,
    text="Serving-Size Calculator",
    padx=10,
    pady=10
)

servings_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

servings_label = tk.Label(
    servings_frame,
    text="Number of servings:"
)

servings_label.pack(
    side="left",
    padx=5
)

servings_entry = tk.Entry(
    servings_frame,
    width=8,
    font=("Arial", 12)
)

servings_entry.pack(
    side="left",
    padx=7
)

servings_entry.insert(0, "2")

servings_button = tk.Button(
    servings_frame,
    text="Calculate Ingredients",
    command=change_servings,
    bg="green",
    fg="white",
    font=("Arial", 10, "bold")
)

servings_button.pack(
    side="left",
    padx=5
)


# ==========================================
# SECTION 9: WEEKLY MEAL PLANNER
# ==========================================

weekly_frame = tk.LabelFrame(
    content_frame,
    text="Weekly Meal Planner",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)

weekly_frame.pack(
    fill="x",
    padx=10,
    pady=8
)

# Select a day.
day_choice = ttk.Combobox(
    weekly_frame,
    values=DAYS,
    state="readonly",
    width=12
)

day_choice.set("Monday")
day_choice.pack(
    side="left",
    padx=5
)

# Select a meal type.
meal_choice = ttk.Combobox(
    weekly_frame,
    values=MEAL_TYPES,
    state="readonly",
    width=12
)

meal_choice.set("Breakfast")
meal_choice.pack(
    side="left",
    padx=5
)

# Enter a recipe name.
weekly_recipe_entry = tk.Entry(
    weekly_frame,
    width=20,
    font=("Arial", 10)
)

weekly_recipe_entry.pack(
    side="left",
    padx=5
)

# Add a meal to the plan.
save_meal_button = tk.Button(
    weekly_frame,
    text="Save Meal",
    command=save_weekly_meal,
    bg="green",
    fg="white",
    font=("Arial", 9, "bold")
)

save_meal_button.pack(
    side="left",
    padx=5
)

# Display the weekly plan.
view_plan_button = tk.Button(
    weekly_frame,
    text="View Weekly Plan",
    command=display_weekly_plan,
    bg="blue",
    fg="white",
    font=("Arial", 9, "bold")
)

view_plan_button.pack(
    side="left",
    padx=5
)

# Save the weekly plan.
save_plan_button = tk.Button(
    weekly_frame,
    text="Save Weekly Plan",
    command=save_plan_to_file,
    bg="purple",
    fg="white",
    font=("Arial", 9, "bold")
)

save_plan_button.pack(
    side="left",
    padx=5
)


# ==========================================
# SECTION 10: SHOPPING LIST
# ==========================================

shopping_frame = tk.Frame(content_frame)

shopping_frame.pack(
    fill="x",
    padx=10,
    pady=5
)

shopping_button = tk.Button(
    shopping_frame,
    text="Generate Shopping List",
    command=generate_weekly_shopping_list,
    bg="orange",
    fg="black",
    font=("Arial", 9, "bold")
)

shopping_button.pack(
    side="left",
    padx=5
)

export_button = tk.Button(
    shopping_frame,
    text="Export Shopping List",
    command=export_weekly_shopping_list,
    bg="darkgreen",
    fg="white",
    font=("Arial", 9, "bold")
)

export_button.pack(
    side="left",
    padx=5
)


# ==========================================
# SECTION 11: AI RECIPE ASSISTANT
# ==========================================

ai_frame = tk.LabelFrame(
    content_frame,
    text="AI Recipe Assistant",
    padx=20,
    pady=20
)

ai_frame.pack(
    fill="x",
    padx=25,
    pady=20
)

ai_heading = tk.Label(
    ai_frame,
    text="Ask questions about food, recipes and meal planning.",
    font=("Arial", 10)
)

ai_heading.pack(anchor="w")

ai_question_entry = tk.Entry(
    ai_frame,
    font=("Arial", 12)
)

ai_question_entry.pack(
    fill="x",
    pady=5
)

ai_ask_button = tk.Button(
    ai_frame,
    text="Ask AI",
    command=ask_ai_assistant,
    bg="blue",
    fg="white"
)

ai_ask_button.pack(
    anchor="w",
    pady=8
)

ai_answer_text = tk.Text(
    ai_frame,
    height=10,
    wrap="word",
    font=("Arial", 10)
)

ai_answer_text.pack(
    fill="x",
    pady=10
)


# ==========================================
# SECTION 12: RECIPE DETAILS
# ==========================================

details_label = tk.Label(
    content_frame,
    text="RECIPE DETAILS",
    font=("Arial", 12, "bold")
)

details_label.pack(
    anchor="w",
    padx=20,
    pady=10
)

details_frame = tk.Frame(content_frame)

details_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=5
)

details_text = tk.Text(
    details_frame,
    height=15,
    font=("Arial", 10),
    wrap="word"
)

details_text.pack(
    side="left",
    fill="both",
    expand=True
)

details_scrollbar = tk.Scrollbar(
    details_frame,
    command=details_text.yview
)

details_scrollbar.pack(
    side="right",
    fill="y"
)

details_text.config(
    yscrollcommand=details_scrollbar.set
)


# ==========================================
# SECTION 13: STATUS MESSAGE
# ==========================================

status_label = tk.Label(
    content_frame,
    text="Ready to search for recipes.",
    font=("Arial", 9),
    fg="blue"
)

status_label.pack(pady=10)


# ==========================================
# SECTION 14: START THE APPLICATION
# ==========================================

# Keep the application window running.
root.mainloop()
