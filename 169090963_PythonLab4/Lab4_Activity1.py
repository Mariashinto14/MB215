import random

# Activity 1: Customizable Dice Simulator
def roll_dice(num_dice, num_sides):
    total = 0
    for _ in range(num_dice):
        total += random.randint(1, num_sides)
    return total


# Activity 2: Temperature Converter
def convert_temperature(temp, unit):
    if unit.upper() == "C":
        return (temp * 9/5) + 32   # Celsius to Fahrenheit
    elif unit.upper() == "F":
        return (temp - 32) * 5/9   # Fahrenheit to Celsius
    else:
        return "Invalid unit"


# Activity 3: Generate a Single Random Number
def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val)


# Activity 4: Investment Simulator
def simulate_investment(amount, years, rate_min, rate_max):
    for _ in range(years):
        rate = random.uniform(rate_min, rate_max)
        amount += amount * rate
    return amount


# Demonstrate the results
if __name__ == "__main__":

    # Dice Simulation
    print("Rolling 3 dice with 6 sides each:", roll_dice(3, 6))

    # Temperature Conversion
    print("Converting 100F to Celsius:", convert_temperature(100, "F"))
    print("Converting 0C to Fahrenheit:", convert_temperature(0, "C"))

    # Generate a Single Random Number
    random_number = generate_random_number(1, 100)
    print(f"The generated random number is: {random_number}")

    # Investment Simulation
    final_amount = simulate_investment(1000, 5, 0.03, 0.07)
    print(f"Final investment value after 5 years: ${final_amount:.2f}")
