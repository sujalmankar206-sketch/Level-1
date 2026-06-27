def convert_temperature():
    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").strip().upper()
        
        if unit == 'C':
            # Celsius to Fahrenheit conversion
            converted = (temp * 9/5) + 32
            print(f"{temp}°C is equal to {converted:.2f}°F")
        elif unit == 'F':
            # Fahrenheit to Celsius conversion
            converted = (temp - 32) * 5/9
            print(f"{temp}°F is equal to {converted:.2f}°C")
        else:
            print("Invalid unit! Please enter 'C' or 'F'.")
    except ValueError:
        print("Please enter a valid numeric value for temperature.")

# Run the program
convert_temperature()