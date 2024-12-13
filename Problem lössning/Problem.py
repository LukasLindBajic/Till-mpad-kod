
def celsius_to_fahrenheit():
    celsius = float(input("Skriv temperatur i Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C är lika med {fahrenheit}°F")

def fahrenheit_to_celsius():
    fahrenheit = float(input("Skriv temperatur i Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F är lika med {celsius}°C")

def kelvin_to_celsius():
    kelvin = float(input("Skriv temperatur i Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin}K är lika med {celsius}°C")

def celsius_to_kelvin():
    celsius = float(input("Skriv temperatur i Celsius: "))
    kelvin = celsius + 273.15
    print(f"{celsius}°C är lika med {kelvin}K")

celsius_to_fahrenheit()
fahrenheit_to_celsius()
kelvin_to_celsius()
celsius_to_kelvin()