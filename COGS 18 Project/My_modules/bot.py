import order_menu

class Bot():
    """Identifies the Bot's name. Able to start and quit chat. Allow customers to view the menu, order and confirm food items.
    """
    
    #Attribute
    name = 'Maki'
    menu = order_menu.Menu('menu.json')
    
    #Method
    #Initialize
    def __init__(self, name, path):
        self.name = name
        self.menu = order_menu.Menu(path)
    
    def is_quit(self, user_input):
        output = False
        keywords = ['no', 'quit', 'bye', 'leave', 'exit', 'done', 'back']
        if any(word in user_input for word in keywords):
            output = True
    
        return output
    
    def confirm_order(self, food_name):
        self.menu.print_food_info(food_name)
        print ('\nWould you like to order this item?')
        ordering = True
        while ordering:
            user_input = input("Enter: (Yes) / (No)").lower()
            if self.is_quit(user_input):
                print ('You have not ordered this food yet :(')
                ordering = False
            elif 'yes' in user_input:
                self.menu.order_food(food_name)
                ordering = False
            else:
                print ('Invalid input, please try again!')
            
    def order_food(self):
        ordering = True
        while ordering:
            print ("\nEnter the item name(s) only. (Or enter 'done' to return to the previous step.)")

            user_input = input('Enter:')
            lower_input = user_input.lower()
            if self.is_quit(lower_input):
                ordering = False
            elif user_input in self.menu.food_menu:
                self.confirm_order(user_input)
                ordering = False
            elif 'menu' in lower_input:
                self.menu.print_menu()
            elif 'categories' in lower_input or 'category' in lower_input:
                self.menu.print_categories()
            else:
                print('Invalid input, plese try again!')
    
    def start_menu(self):
        self.menu.print_menu()
        self.order_food()
    
    def start_categories(self):
        self.menu.print_categories()
        selecting = True
        while selecting:
            print ("\nPlease select a category from the list or enter 'back' for returning to the previous step.")
            user_input = input('Enter: ')
            lower_input = user_input.lower()
            if 'back' in lower_input:
                selecting = False
            elif(self.menu.print_food_list(user_input)):
                self.order_food()
                
    def start_recommendation(self):
        selecting = True
        while selecting:
            random_food = self.menu.recommendation()
            print("Would you like this food?('Yes' or 'No')")
            user_input = input('Enter:')
            user_input = user_input.lower()
            
            if 'yes' in user_input:
                self.menu.order_food(random_food)
            
            print ('Do you need more recommendation?')
            user_input = input('Enter:').lower()
            if 'no' in user_input:
                selecting = False
    
    def start_viewing(self):
        viewing = True
        while viewing:
            self.menu.view_order()
         
            print("If you would like to remove an ordered item, please enter the corresponding name. Else please enter 'back' for returning to the previous step or enter 'check' to complete the order.")
            
            user_input = input('Enter:')
            lower_input = user_input.lower()
            
            if user_input in self.menu.total_order:
                self.menu.remove_food(user_input)
            elif self.is_quit(lower_input):
                viewing = False
            elif 'check' in lower_input:
                print('Thank you~ Your order has been placed and will be ready soon ;)')
                return False
            else:
                print('Invalid input, please try again!\n')
            
            return True
            
    
    #Start Chat
    def start_chat(self):
        chat = True
        
        print ('Hello! Welcome to Makino Restaurant.')
        print ('My name is ', self.name, '.')
        
        while chat :
            print ('\nWhat can I do for you?' )
            #tranfer the user input to lowercase
            user_input = input('Enter :' ).lower()
            user_input = user_input.lower()
            print ('\n')
            
            #endchat if the user say 'no'
            if self.is_quit(user_input):
                print ('Bye~ Thank you for coming! Have a great day ;)')
                chat = False
            elif 'menu' in user_input:
                self.start_menu()
            elif 'categories' in user_input or 'category' in user_input:
                self.start_categories()
            elif 'recommend' in user_input or 'recommendation' in user_input:
                self.start_recommendation()
            elif 'view' in user_input or 'take a look' in user_input or 'see' in user_input:
                chat = self.start_viewing()
             