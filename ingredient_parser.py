
# ingredient_parser.py

# This function converts a fraction into a decimal number.
def convert_fraction(value):

    # Check whether the value contains a fraction.
    if "/" in value:

        # Separate the numerator and denominator.
        numerator, denominator = value.split("/")

        # Convert the fraction into a decimal.
        return float(numerator) / float(denominator)

    # If it is not a fraction, convert it directly.
    return float(value)


# This function separates an ingredient into its parts.
def parse_ingredient(ingredient_text):

    # Remove unnecessary spaces.
    parts = ingredient_text.strip().split()

    # Return empty information if nothing was entered.
    if not parts:
        return {
            "quantity": "",
            "unit": "",
            "name": ""
        }

    quantity = 0
    unit = ""
    name = ""

    try:
        # Check whether the first part is a number or fraction.
        quantity = convert_fraction(parts[0])

        # Check whether the next part is also a number.
        if len(parts) > 1:

            try:
                # This handles quantities such as 1 1/2.
                second_number = convert_fraction(parts[1])

                quantity = quantity + second_number

                # The unit comes after both numbers.
                if len(parts) > 2:
                    unit = parts[2]

                # The ingredient name comes after the unit.
                if len(parts) > 3:
                    name = " ".join(parts[3:])

            except ValueError:

                # If the second part is not a number,
                # it is the measurement unit.
                unit = parts[1]

                if len(parts) > 2:
                    name = " ".join(parts[2:])

        return {
            "quantity": quantity,
            "unit": unit,
            "name": name
        }

    except ValueError:

        # If the ingredient does not begin with a number,
        # treat the entire text as its name.
        return {
            "quantity": "",
            "unit": "",
            "name": ingredient_text.strip()
        }
