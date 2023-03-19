available_pizzas = ["margherita", "calzone", "four cheese", "pepperoni", "napoli"]

pizza_order = []
total_price = 0
print("Hello! here is the menu today:")
for i, pizza in enumerate(available_pizzas):
    print(str(i) + ". " + pizza)

continue_ordering = True
while continue_ordering:
    answer = input("do you want to add a pizza (yes/no)?")
    if answer == "yes":
        valid_pizza_choice = False
        while not valid_pizza_choice:
            pizza_choice = int(input(
                "what pizza do you want provide a number "))
            # (data validation) validate user input here:
            if (pizza_choice >= 0) and \
                    (pizza_choice <= len(available_pizzas) - 1):
                pizza_order.append(available_pizzas[pizza_choice])
                print("adding " + available_pizzas[pizza_choice] + \
                      " pizza to the order")
                total_price += 10
                valid_pizza_choice = True
            else:
                print("please provide a correct number")
    else:
        continue_ordering = False

print("you have ordered ")
print(pizza_order)
print("you have to pay " + str(total_price) + "£.")
valid_tip = False
while not valid_tip:
    tip = float(input("what tip do you want to leave (0-25%)? "))
    if (tip >= 0) and (tip <= 25):
        valid_tip = True
    else:
        print("please provide a correct number")

total_price += total_price * tip / 100
print("thank you! the price is now " + str(total_price) + \
      ". pizzas are on the way")
