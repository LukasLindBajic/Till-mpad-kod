import os


def numbered_list(list):     #parameter
    orderd_list = []
    
    for index, item in enumerate (list, 1):    #enumerate bryter ner namn och position
        orderd_list.append(f"{index} {item}")

    return "\n".join(orderd_list)
    
os.system("cls")
cars = ["Porsche", "Ferrari", "Lambo"]


    #return

os.system('cls' if os.name == 'nt' else 'clear')

print(numbered_list(cars))