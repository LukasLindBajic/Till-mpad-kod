import csv
import os
import locale
from collections import Counter 

def analyze_sales_data(filename):
    products = {}
    all_products =[]

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])
            
            all_products.append(product)

            if product in products:
                products[product] += sales
            else:
                products[product] = sales
    
    #TODO: Hitta den mest sålda produkten (TIPS! Använd Counter från collections)
    
    # Hitta den mest lukrativa produkten
    most_sold = Counter(all_products).most_common(1)[0]

    most_lucrative_product = max(products, key=products.get)
    
    # Genomsnittlig försäljning per produkt
    average_sales = sum(products.values()) / len(products)

    print(f"Mest sålda produkt: {most_sold[0]} Antal: {most_sold[1]}")  #FIXME: Redovisa mest sålda produkt här
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {locale.currency(products[most_lucrative_product],grouping=True)}")
    print(f"Genomsnittlig försäljning per produkt: {locale.currency(average_sales, grouping=True)}")


# Sätt språkinställning till svenska (Sverige) används för att skriva ut formaterad valuta
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')
analyze_sales_data('sales_data.csv')
