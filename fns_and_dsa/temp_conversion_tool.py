global FAHRENHEIT_TO_CELCIUS_FACTOR 
global CELCIUS_TO_FAHRENHEIT_FACTOR 

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)  + 32


def main():
    temp = float(input ("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celcius or Fahrenheit? (C/F): " ).strip().upper()

    if choice == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")

    elif choice == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")


    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main() 