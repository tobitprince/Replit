"""
There's no place like Rome...Or Napoli, Milan, possibly even New York if you must.
Just not the dodgy 2am 'round bread with suspicious toppings' merchants that I definitely
do not visit on my
way home from a night out.
That's right, you're opening a pizza shop! Try not to get anchovy on your keyboard.
Man that stuff never
washes out.
Regardless, your program today must:
1. Prompt the user to input the quantity and size of pizzas.
2. Multiply the two inputs together to calculate the cost of the pizzas.
3. Store that in a 2D list with the user's name.
4. Use try.... except for two reasons:
1. Include auto-save and auto-load. Use it with the auto-load.
2. When casting the quantity of pizzas to an integer. Avoid the user crashing the program by typing
'three' instead of '3'. Or any other non-integer input. If they do, then prompt them to try again
"""
import os
import time
import ast

orderPizza = []
try:
    with open("order_pizza.txt","r", encoding="utf8") as file:
        content = ast.literal_eval(file.read())
        for row in content:
            orderPizza.append(row)
except FileNotFoundError:
    print("File not found")
    time.sleep(1)

def add_pizza():
    """Add a pizza order
    """
    name = input("Your Name: ")
    topping = input("Toppings: ")
    size = input("Size(small/medium/large): ").lower()
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("It should be a number")
    cost = 0
    if size[0] == "s":
        cost = 500
    elif size[0] == "m":
        cost = 700
    elif size[0] == "l":
        cost = 1000
    total = quantity * cost
    total = round(total, 2)
    print(f"Thanks {name.title()}.Your {quantity} {size} pizza(s) will cost {total}")
    row = [name, topping, size, quantity,total]
    orderPizza.append(row)
    time.sleep(2)

def view_pizza():
    """View the pizza orders
    """
    name = "Name"
    topping = "Topping"
    size = "Size"
    quantity = "Quantity"
    total = "Total"
    print(f"{name:^10}{topping:^10}{size:^10}{quantity:^10}{total:^10}")
    for row in orderPizza:
        print(f"{row[0].title():^10}{row[1].title():^10}{row[2].title():^10}{row[3]:^10}{row[4]:^10}")
    time.sleep(2)

while True:
    os.system("cls")
    print("Welcome to Chimi's Pizzaria".center(53,"-"))
    option = int(input("1.Add Pizza\n2. View Orders\nEnter selection: "))
    if option == 1:
        add_pizza()
    elif option == 2:
        view_pizza()
    else:
        print("Invalid input.Try again! ")
        break
    time.sleep(2)
    with open("order_pizza.txt", "w",encoding="utf8") as file:
        file.write(str(orderPizza))
