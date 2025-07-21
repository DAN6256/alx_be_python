FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp = input("Enter the temperature to convert: ")
try:
    temp = float(temp)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    match unit:
        case "C":
            converted_value = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_value}°F")
        case "F":
            converted_value = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_value}°C")
        case _:
            print("I do not understand this unit")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
