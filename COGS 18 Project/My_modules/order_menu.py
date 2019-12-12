import json
import random

class Menu():
    """Organizes and categorizes the menu. Customers are able to add, remove, and calculate the total price of the order. This class also includes a randomized recommendation option for customers.
    """

    #attribute
    categories = {}
    food_menu = {}
    total_order = []
    total_price = 0

    def __init__(self, path):
        with open(path) as file:
            data = json.load(file)

        self.categories = data['Category']
        for c in self.categories:
            for food in self.categories[c]:
                self.food_menu[food] = self.categories[c][food]


    #print all categories
    def print_categories(self):
        #check if categories is empty
        if len(self.categories) == 0:
            print('Error: no category found!')
            return False

        for c in self.categories:
            print(c)

        return True

    #print the food list for a special category
    def print_food_list(self, category):
        
        #check if the category is not in categories
        if category not in self.categories:
            print('Error: empty food list!')
            return False

        foodlist = self.categories[category]

        for food in foodlist:
            print(food)

        return True

    #print the food's name, price and description or preparation
    def print_food_info(self, food_name):
        
        #check if the food's name is not in the food menu
        if food_name not in self.food_menu:
            print('Error: cannot find this food!')
            return False
            
        food = self.food_menu[food_name]

        price = food['Price']
        print( food_name, '\t$ ', price)

        if 'Preparation' not in food:
            description = food['Description']
            print( 'Description :')
            print(description)
        else:
            preparation = ''
            print( 'Preparation :')
            for p in food['Preparation']:
                preparation = preparation + '"' + p +'"  ' 
            print(preparation)
                    
        return True


    def order_food(self, food_name):
        
        #check if the food's name is not in the food menu
        if food_name not in self.food_menu:
            print('Sorry, we do not have this food yet')
            return False

        str = 'You ordered "'+ food_name + '"'
        if 'Preparation' in self.food_menu[food_name]:
            preparation = 'What preparation would you like?('
            for p in self.food_menu[food_name]['Preparation']:
                preparation = preparation + '"' + p +'"  ' 
            preparation += ')'
            print(preparation)
            user_input = input('Enter:')
            if(user_input in self.food_menu[food_name]['Preparation']):
                str = str + ' with the preparation "' + user_input +'"'
            else: 
                print('Sorry, we do not have this preparation yet')
                return False

        self.total_order.append(food_name)
        self.total_price += float(self.food_menu[food_name]['Price'])
        print(str)
        return True
    
    def remove_food(self,food_name):
        
        #check if the food's name is in the food menu
        if food_name in self.total_order:
            print ('This iten has been removed from your order.')
            self.total_price -= float(self.food_menu[food_name]['Price'])
            self.total_order.remove(food_name)
            return True
        else:
            print ('You have not ordered this item yet.')
            return False       

    def menu_format(self, food_name, price, length):
        food_name_length = len(food_name)
        price_length = len(price)
        if price_length is 4 :
            price = ' ' + price

        retval = food_name + ' '
        for i in range(0, length -  food_name_length - 5):
            retval = retval + '*'

        retval = retval + ' $ ' + price
        return retval
    
    #print all foods' names and prices
    def print_menu(self):     
        #check if the food_menu is empty
        if not self.food_menu:
            print('Error: menu is empty!')
            return False

        for food in self.food_menu:
            print(self.menu_format(food, self.food_menu[food]['Price'], 70))

        return True

    #random food from food menu and expect the food in the order list
    def recommendation(self):
        local_menu = self.food_menu.copy()
        for food in self.total_order:
            if food in local_menu.keys():
                del local_menu[food]
        random_food = random.choice(list(local_menu.keys()))
        self.print_food_info(random_food)
        return random_food
    
    def view_order(self):
        print('You have ordered:')
        for food in self.total_order:
            print (food)

        print ('The total price is $ ' + str(self.total_price))

