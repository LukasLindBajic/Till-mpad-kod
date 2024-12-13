import os

def convert_temperature(temperature, from_to_unit): #funktion som tar emot parametrar
    if from_to_unit == 1:            # Celsius to Fahrenheit            
        result = (temperature * 9/5) + 32
        return f"{temperature}°C är lika med {result:.2f}°F"
    
    elif from_to_unit == 2:          # Fahrenheit to Celsius
        result = (temperature - 32) * 5/9
        return f"{temperature}°F är lika med {result:.2f}°C"
    
    elif from_to_unit == 3:               # Kelvin to Celsius
        result = temperature - 273.15
        return f"{temperature}°K är lika med {result:.2f}°C"

    elif from_to_unit == 4:               # Celsius to Kelvin
        result = temperature + 273.15
        return f"{temperature}°C är lika med {result:.2f}°K"

while True:
    os.system('cls')
    
    temp = float(input("Ange temperatur i valfri enhet: "))
    to_unit = int(input("""1) C till F
2) F till C
3) K till C
4) C till K """))

    print(convert_temperature(temp, to_unit))

    input("\nTryck ENTER")