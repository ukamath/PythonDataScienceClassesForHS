class Item:

    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity


class User:

    def __init__(self, name,role):
        self.name = name
        self.role = role


class OnlineShopping:

    def __init__(self):
        self.inventory=[]

    def add_items(self, item, user):
        if user.role == 'provider':
            print('Provider with user name ' + user.name + ' wants to add ' + item.name + ' to the current inventory')
            self.inventory.append(item)

    def shopping(self, user):
        not_completed = True
        shopping_cart = []
        print('Shopping Process for ' + user.name + ' has begun')
        while not_completed:
            shopping = input('Do you want to purchase items, yes or no?')
            if shopping == 'yes':
                item_name = self.display_and_get_item()
                print('Selected ' + item_name)
                for item in self.inventory:
                    if item.name == item_name:
                        shopping_cart.append({'name':item_name, 'cost':item.cost})
                        print(shopping_cart)
                        item.quantity = item.quantity-1
            else:
                not_completed = False
        self.print_receipt(shopping_cart, user)

    def show_inventory(self, user):
        if user.role == 'admin':
            print('Admin with user name ' + user.name + ' wants to see current inventory')
            for item in self.inventory:
                if item.quantity > 0:
                    print('Item Name : ' + item.name + ' Cost: ' + str(item.cost) + ' Quantity: '+ str(item.quantity))

    def display_and_get_item(self):
         for item in self.inventory:
             if item.quantity > 0:
                print('Item Name : ' + item.name + ' Cost: ' + str(item.cost))
         item_name = input('Type the item name: ')
         return item_name

    def print_receipt(self, shopping_cart, customer):
        total_cost =0
        print('The Receipt for the Customer - ' + customer.name)
        for item in shopping_cart:
            print('Item Name : ' + item['name'] + ' Cost: ' + str(item['cost']))
            total_cost = total_cost + item['cost']
        print('The total cost = ' + str(total_cost))

# create Amazon instance
amazon = OnlineShopping()

# create items
laptop = Item('Laptop',2000, 20)
chair = Item('Chair',20, 2000)


# create provider
provider1 = User('John','provider')

# provider adds items to Amazon inventory
amazon.add_items(laptop, provider1)
amazon.add_items(chair, provider1)

# Manager of Inventory
manager = User('Manager', 'admin')
# Prints the current list
amazon.show_inventory(manager)
# New Customer wants to sho
uday = User('Uday','customer')
amazon.shopping(uday)
# Prints the inventory
amazon.show_inventory(manager)