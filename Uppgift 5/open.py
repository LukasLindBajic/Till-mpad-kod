import csv
import os
import locale
from time import sleep


def load_data(filename): 
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(        #list
                {                    #dictionary
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

#gör en funktion som hämtar en produkt

    
def remove_product(products, id):
    temp_product = None
    
    for product in products:
        if product["id"] == id:
            temp_product = product
            break  # Avsluta loopen så snart produkten hittas

    if temp_product:
        products.remove(temp_product)
        return f"Product: {id} {temp_product['name']} was removed"
    else:
        return f"Product with id {id} not found"


def view_product(products, id):
    # Go through each product in the list
    for product in products:
        # Check if the product's id matches the given id
        if product["id"] == id:
            # If it matches, return the product's name and description
            return f"Visar produkt: {product['name']} {product['desc']}"
    
    # If no matching product is found, return this message
    return "Produkten hittas inte"

def edit_product(product, name, desc, price, quantity):
    products['name'] = name
    products['desc'] = desc
    products['price'] = price
    products['quantity'] = quantity

    return f"Ändra producten med id #{product['id']}"

def view_products(products):
    product_list = []
    for index, product in enumerate(products,1 ):
        product_info = f"{index}) (#{product['id']}) {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)

def add_product(products, name, desc, price, quantity):
    max_id = max(products, key=lambda x: x['id']) #Lambda är en lite funktion utan namn som hämtar nyckelns värde fån dictionary

    id_value = max_id['id']

    id = id_value + 1
    products.append(
        {
            "id": id,
            "name" : name,
            "desc" : desc,
            "price" : price,
            "quantity": quantity
        }
    )

    return f"lade till produkt: {id}"
    

#TODO: gör om så du slipper använda global-keyword (flytta inte "product = []")
#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls' if os.name == 'nt' else 'clear')
products = load_data('db_products.csv')

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(view_products(products))  # Show ordered list of products

        choice = input("Vill du (L)ägga till produkt,(Ä)ndra en produkt, (V)isa eller (T)a bort en produkt? ").strip().upper()

        if choice == "Ä":
            index = int(input("Enter product ID: "))
            product = products[index-1]
            print(f"ändra på med id: (products{'id'})")
            name = input("name på product:")
            desc = input("beskrivning")
            price = float (input("price: "))
            quantity = int (input("antal: "))
            
            print(edit_product(product, name, desc ,price, quantity))
            print(view_product(products, id))
            
    

        if choice == "L":
            name = input("Namn på produkt: ")
            desc = input("beskrivning: ")
            price = float(input("pris: "))
            quantity = int(input("Antal: "))
           
            print(add_product(products, name, desc, price, quantity))

        elif choice in ["V", "T"]:
            index = int(input("Enter product ID: "))
            
            if choice == "V":   #visa
                if 1 <= index <= len(products):  # Ensure the index is within the valid range
                    selected_product = products[index - 1]  # Get the product using the list index
                    id = selected_product['id']  # Extract the actual ID of the product
                    print(view_product(products, id))  # Remove product using the actual ID
                    done = input()
                    
                else:
                    print("Ogiltig produkt")
                    sleep(0.3)

            elif choice == "T": #ta bort
                if 1 <= index <= len(products):  # Ensure the index is within the valid range
                    selected_product = products[index - 1]  # Get the product using the list index
                    id = selected_product['id']  # Extract the actual ID of the product

                    print(remove_product(products, id))  # Remove product using the actual ID
                    sleep(0.5)            

                else:
                    print("Ogiltig produkt")
                    sleep(0.3)
        
    except ValueError:
        print("Välj en produkt med siffor")
        sleep(0.5)

# Define the CSV file path
csv_file_path = "db_products.csv"

# Write the products data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "description", "price", "quantity"])
    writer.writeheader()  # Write the header row
    writer.writerows(products)  # Write the product data

print(f"Data successfully saved to {csv_file_path}")