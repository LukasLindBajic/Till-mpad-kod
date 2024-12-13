import csv
import os
import locale


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
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products
    
def remove_products(products, id):
   temp_product = None
   for product in products:
        if products('id') ==id:
            temp_product = product
            break
   if temp_product:
       products.remove(temp_product)
       return f"{temp_product['name']} togs bort"
   else:
       return f"Kunde inte hitta produkt"

def view_products(products):
    product_list = []
     #TODO: gör en nummerlista med enumerate (att använda id kommer inte fungera i längden)
     
    for product in products:
        product_info = f"(#{product['id']}) {product['name']} \t {product['desc']} \t {locale.currency(product['price'], grouping=True)}"
        product_list.append(product_info)
    
    return "\n".join(product_list)


#TODO: skriv en funktion som returnerar en specifik produkt med hjälp av id
#TODO: skriv en funktion som tar bort en specifik produkt med hjälp av id



locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

while True:
    os.system('cls')
    products = load_data('p2-opendb/db_products.csv')
    print(view_products(products))

    id = int(input("Vilken produkt vill du visa? "))

    if id >= 1 and id <= len(products):
        selected_product = products[id - 1]

    id = selected_product['id']

    print(remove_products(products, id))
