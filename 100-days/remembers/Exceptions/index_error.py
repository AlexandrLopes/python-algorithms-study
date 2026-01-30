fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing. #erro de indice
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")

    except IndexError:
        print("Fruit Pie")

make_pie(4)



