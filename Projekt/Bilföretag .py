import csv 
import os
import locale
from time import sleep

def load_data(filename):
    products = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file) 
        for row in reader: 
            products.append({ 
                "id": int(row['id']), 
                "name": row['name'],
                "color": row['color'],
                "price": float(row['price']),
                "mileage": float(row['mileage']),
                "condition": row['condition'].strip()
            })
    return products

def save_data(filename, products):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "color", "price", "mileage", "condition"]) 
        writer.writeheader() 
        writer.writerows(products) 
    print(f"Förändringar har sparats i {filename}") 

def remove_product(products, id):
    temp_product = next((product for product in products if product["id"] == id)) 
    if temp_product: 
        products.remove(temp_product) 
        for index, product in enumerate(products, 1): product['id'] = index 
        return f"Produkt: {id} {temp_product['name']} togs bort"
    else:
        return f"Produkten med id {id} hittades inte"

def view_product(products, id):
    product = next((product for product in products if product["id"] == id)) 
    if product:
        return (f"Visar produkt: {product['name']} {product['color']} {product['price']} "f"{product['mileage']} {product['condition']}") 
    return "Produkten hittas inte"

def edit_product(product, name, color, price, mileage, condition):
    product['name'] = name
    product['color'] = color
    product['price'] = price
    product['mileage'] = mileage
    product['condition'] = condition
    return f"Ändrade produkten med id #{product['id']}"


def view_products(products):
    print("\n--- Meny ---")
    print(f"{'#':<3} {'ID':<5} {'Namn':<20} {'Färg':<10} {'Pris':<10} {'Mil':<8} {'Skick':<15}") #Skriver ut rubriker för tabellen och justerar texten för en snygg layout.
    print("-" * 70) #Skriver en avgränsningslinje under rubrikerna.
    for index, product in enumerate(products, 1): #Loopar igenom listan av produkter och ger varje produkt ett visningsindex som börjar från 1.

        print(f"{index:<3} {product['id']:<5} {product['name']:<20} {product['color']:<10} "f"{locale.currency(product['price'], grouping=True):<10} {product['mileage']:<8} {product['condition']:<15}")

def add_product(products, name, color, price, mileage, condition):
    max_id = max([p['id'] for p in products], default=0) 
    id = max_id + 1
    products.append({
        "id": id,
        "name": name,
        "color": color,
        "price": price,
        "mileage": mileage,
        "condition": condition
    })
    return f"Lade till produkt: {id}"

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8') 
os.system('cls' if os.name == 'nt' else 'clear') 

filename = 'Projekt/db_products.csv'
products = load_data(filename)

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(view_products(products))


        print("\n--- OPTIONS ---")
        choice = input("Lägg till produkt(1), Spara programmet(2), Ändra en produkt(3), Visa produkt(4), Ta bort produkt(5), Avsluta program(6)").strip().upper()

        if choice == "3":
            id = int(input("Ange produkt-ID: "))
            product = next((p for p in products if p["id"] == id))
            if product:
                name = input("Namn på fordon: ")
                color = input("Vad är bilens färg: ")
                price = float(input("Pris: "))
                mileage = int(input("Antal mil: "))
                condition = input("Beskriv fordonets skick: ")
                print(edit_product(product, name, color, price, mileage, condition))
            else:
                print("Produkten hittas inte")

        elif choice == "2":
            save_data(filename, products)
        
        elif choice == "6":
            print("avsluta programmet")
            break

        elif choice == "1":
            name = input("Namn på fordon: ")
            color = input("Vad är bilens färg: ")
            price = float(input("Pris: "))
            mileage = int(input("Antal mil: "))
            condition = input("Beskriv fordonets skick: ")
            print(add_product(products, name, color, price, mileage, condition))

        elif choice == "4":
            id = int(input("Ange produkt-ID: "))
            print(view_product(products, id))

        elif choice == "5":
            id = int(input("Ange produkt-ID: "))
            print(remove_product(products, id))

        else:
            print("Ogiltigt val. Försök igen.")

        input("Tryck på Enter för att fortsätta...")

    except ValueError:
        print("Vänligen ange ett giltigt produkt-ID i siffror.")
        sleep(0.5)

csv_file_path = "db_products.csv"

# Spara produktdata till en CSV-fil
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "color", "price", "mileage", "condition"])
    writer.writeheader()  # Skriv header-raden
    writer.writerows(products)  # Skriv produktdata

print(f"Data sparades framgångsrikt till {csv_file_path}")