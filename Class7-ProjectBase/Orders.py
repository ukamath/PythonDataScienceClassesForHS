base_pizzas = {'Cheese':5, 'Chicken':7}
base_toppings = ['Onions', 'Peppers', 'Pineapple', 'Tomatoes']

customers_exist = True
prompt_username ='What is the Customer Name?'
prompt_pizza='Do you want Pizza or No?'
prompt_base = 'What base pizza do you want?'
prompt_quantity ='How many of the type'
prompt_toppings ='Do you want extra toppings or No?'
prompt_topping_name = 'Which topping will you like?'

while customers_exist:
    orders_not_done = True
    customer_name = input(prompt_username)
    order_list =[]
    while orders_not_done:
        pizza = input(prompt_pizza)
        if pizza == 'No':
            break
        else:
            print(base_pizzas.keys())
            input_base = input(prompt_base)
            input_quantity = input(prompt_quantity)
            toppings_done = False
            order_toppings = []
            while toppings_done== False:
                input_toppings = input(prompt_toppings)
                if(input_toppings == 'No'):
                    break
                else:
                    print(base_toppings)
                    topping = input(prompt_topping_name)
                    order_toppings.append(topping)
        order_item ={'Quantity': int(input_quantity), 'Pizza': {'Base': input_base, 'Toppings': order_toppings}}
        print(order_item)
        order_list.append(order_item)
    print('****** Receipt Start************')
    print("Order is completed for " + customer_name)
    order_element =1;
    total_cost=0

    for item in order_list:
        print(order_element)
        number_pizzas= item.get('Quantity')
        print('Number of Items :' + str(number_pizzas))
        pizzas = item.get('Pizza')
        base_value = base_pizzas.get(pizzas.get('Base'))
        print('Base :' + pizzas.get('Base'))
        cost = item.get('Quantity')*base_value
        toppings_pizza = pizzas.get('Toppings')
        toppings_number = len(toppings_pizza)
        print("Toppings : ")
        print(toppings_pizza)
        cost = cost + number_pizzas * toppings_number
        print('Total Cost for pizza : ' + str(cost))
        total_cost = total_cost + cost
        order_element += 1
    print('Total Cost :' + str(total_cost))
    print('****** Receipt Complete ************')












