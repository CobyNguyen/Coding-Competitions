import random
import math
#contestant id = 

class Pizzas:
   def getValue(self, price, count): #While these two methods use camelCase as made by the judges/prompt, I use snake case for my variables
      return price * count #SC3 method: calculates the total inventory cost (price * pizza count). 
   def toString(self, menu_code, menu_name, count, price, total_cost):
        pizza_string = f"{menu_code} - {menu_name} - {count} - ${price:.2f} - ${total_cost:.2f}"
        print(pizza_string)
        return pizza_string #SC4 method returns each value from the methods and formates them separated by dashes. 
      #SC5 This same method formates the value into US currency while retainin decimals withou using any cents
########################
########################
#DRIVER SECTION
   #Enter your code below
   def __init__(self): #Each value is printed into a list, in case multiple pizzas are made
      self.menu_codes = []
      self.menu_names = []
      self.pizza_counts = []
      self.prices = []
      self.total_costs = []

      self.get_number_of_pizzas()
      self.create_menu_codes()
      self.pizza_name_entry()
      self.get_storage_quantity()
      self.print_pizzas()

   def get_number_of_pizzas(self):
      while True:
         try:
            self.number_of_pizzas = int(input("How many simulated frozen pizzas do you want to create? You must enter between 1 and 10.\n"))
            if self.number_of_pizzas not in range(1, 11):
               print("WARNING! You entered too low or too high for the quantity. Try again please.")
            else:
               break
         except ValueError:
            print("You can not enter in letters. Try again.")

   def create_menu_codes(self): #SC8 This method allows the for menu code of the pizza to be entered. It makes sure the amount of letters is equal to exactly 3, otherwise prints error and retires
      for index in range(self.number_of_pizzas):
         while True:
            menu_code = input(f"Enter a three-character menu code for pizza {index + 1}: ")
            if len(menu_code) == 3: 
               self.menu_codes.append(menu_code)
               break
            else:
               print("Error: Menu code must be exactly three characters. Try again.")  


   def pizza_name_entry(self): #SC9 Asks for the name of the specific pizza
      for index in range(self.number_of_pizzas):
         self.menu_names.append(input(f"Enter the name for pizza {index + 1}: "))

   def get_storage_quantity(self): #SC10 Uses try/except to get the inventory count. Once again it makes sure it is a number. If it is not a number, it returns error and tries again.
      for index in range(self.number_of_pizzas):
         while True:
            try:
               count = int(input(f"Please enter the total inventory count of this pizza to keep in the freezer for pizza {index + 1}: "))
               self.pizza_counts.append(count)
               break
            except ValueError:
               print("You can not enter in letters. Try again.")

   def generate_prices(self): #SC2 Generates a random integer from 10-20 using the random library
      for index in range(self.number_of_pizzas):
         self.prices.append(random.randint(10, 20))

   def calculate_costs(self): 
      for price, count in zip(self.prices, self.pizza_counts):
         self.total_costs.append(self.getValue(price, count))

   def print_pizzas(self): #SC12 This method prints all of the pizzas, including their associated objects
      self.generate_prices()
      self.calculate_costs()
      print("\nFinal List of Pizzas:")
      print("Menu Code - Menu Name - Count - Price - Total Cost")
      for index in range(self.number_of_pizzas):
         print(self.toString(self.menu_codes[index], self.menu_names[index], self.pizza_counts[index], self.prices[index], self.total_costs[index]))

if __name__ == "__main__": #SC11 Runs the program and constructs the objects🤰
    pizza = Pizzas()