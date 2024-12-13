import os
class product:
    def __inti__(self):
       self.products = [
            {
                "name": "mobilnamn",
                "desc": "en fin mobil",
                "price": 100000,
                "quantity": 2
            },
            {
                "name": "dator",
                "desc": "en fin dator",
                "price": 200000,
                "quantity": 2
            }
            ]
    def view(self):
        return self.products

os.system("cls")
get_products = product()
products = get_products.view()

def list_inventory():
    for id in range(len(products)):
        print(products[id]["name"])

product