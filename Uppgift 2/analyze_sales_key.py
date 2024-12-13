import csv
import os
import locale
from collections import Counter

def analyze_sales_data(filename):
    products = {}
    all_products = []
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

    # Hitta den mest sålda produkten
    product_count = Counter(all_products)
    most_common_product = product_count.most_common(1)[0]

    # Hitta den mest lukerativa produkten
    most_lucrative_product = max(products, key=products.get)
    
    # Genomsnittlig försäljning per produkt
    average_sales = sum(products.values()) / len(products)
        
    print(f"Mest sålda produkt: {most_common_product[0]}, Antal: {most_common_product[1]}")
    print(f"Mest lukrativa produkt: \"{most_lucrative_product}\" med försäljning på {locale.currency(products[most_lucrative_product],grouping=True)}")
    print(f"Genomsnittlig försäljning per produkt: {locale.currency(average_sales, grouping=True)}")


# Sätt språkinställning till svenska (Sverige)
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')

os.system('cls')
analyze_sales_data('sales_data.csv')