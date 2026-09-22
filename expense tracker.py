# Important modules
from datetime import date, datetime
from pathlib import Path
from statistics import mean
import json
# Unimportant module
from time import sleep
# Creating the class that is responsible for the main critical points about the expense tracker(adding, viewing, deleting, etc.)
class ExpenseTracker:
    # Initializing each variable thats gonna be used in this class
    def __init__(self):
        self.expense = None
        self.amount = 0
        self.price = 0.0
        self.category = None
        self.date = None
        self.expense_info = {}
        self.expenses = []
        self.budget = 0.0
        # This variable is for the ExpenseTrackerCLI class
        self.option = None
    # Creating the function that adds a new expense into the expense tracker
    def add_new_expense(self):
        # Asking for the expense while checking if its valid or not
        while True:
            self.expense = input("Enter the expense that you want to add into the expense tracker ->: ").capitalize()
            if not self.expense:
                print("Enter a valid expense")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.expense}(Food, Transportation, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the amount while checking if its valid or not
        while True:
            try:
                self.amount = int(input(f"Enter the amount of {self.expense}s you bought ->: "))
                if self.amount <= 0:
                    print("Enter a valid amount that is bigger than 0")
                else:
                    break
            except ValueError:
                print("Invalid amount")
        # Asking for the singular price while checking if its valid or not
        while True:
            try:
                self.price = float(input(f"Enter the price of one {self.expense} ->: "))
                if self.price <= 0:
                    print("Enter a valid price that is bigger than 0")
                else:
                    break
            except ValueError:
                print("Invalid price")
        # Asking for the date while checking if its valid or not
        while True:
            try:
                self.date = date.fromisoformat(input(f"Enter the date of when {self.amount} {self.expense}(s) were bought in this format(YYYY-MM-DD) ->: ").strip())
                # Checking if the date is in the future or not
                if datetime.now().date() < self.date:
                    print(f"Enter a date that isn't in the future(Todays date: {datetime.now().date()})")
                else:
                    break
            except ValueError:
                print("Invalid date parameters therefore we will start over")
        self.expense_info = {"Expense": self.expense, "Amount": self.amount, "Price": self.amount*self.price, "Category": self.category, "Date": self.date}
        # Check if the expense information exists
        if any(self.expense == expense_info["Expense"] and self.category == expense_info["Category"] and self.date == expense_info["Date"] for expense_info in self.expenses):
            print("\nExpense information already found(Edit the amount or price)")
        else:
            self.expenses.append(self.expense_info)
            print(f"\n{self.amount} {self.expense}(s) has been added into the expense tracker")
    # Creating the function that displays all the expenses
    def display_all_expenses(self):
        print("\nExpenses: ")
        # Check if expense tracker data exists
        if not self.expenses:
            print("\nNo data found to proceed")
        else:
            # Looping through each expense information
            for expense_info in self.expenses:
                print() # <- this is for clearer structure to seperate each expense information one by one
                for expense_info_key, expense_info_value in expense_info.items():
                    if expense_info_key == "Price":
                        print(f"{expense_info_key} -> {expense_info_value:.2f}")
                    else:
                        print(f"{expense_info_key} -> {expense_info_value}")
    # Creating the function that deletes an expense
    def delete_expense(self):
        # Asking for the expense while checking if its valid or not
        while True:
            self.expense = input("Enter the expense that you would like to delete ->: ").capitalize()
            if not self.expense:
                print("Enter a valid expense")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.expense}(Food, Transportation, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the date while checking if its valid or not
        while True:
            try:
                self.date = date.fromisoformat(input(f"Enter the date of when {self.expense} was bought in this format(YYYY-MM-DD) ->: ").strip())
                # Checking if the date is in the future or not
                if datetime.now().date() < self.date:
                    print(f"Enter a date that isn't in the future(Todays date: {datetime.now().date()})")
                else:
                    break
            except ValueError:
                print("Invalid date parameters therefore we will start over")
        # Check if the expense information exists
        if not any(self.expense == expense_info["Expense"] and self.category == expense_info["Category"] and self.date == expense_info["Date"] for expense_info in self.expenses):
            print("\nNo such expense information found")
        else:
            # Looping through each expense information
            for expense_info in self.expenses:
                if expense_info["Expense"] == self.expense and expense_info["Category"] == self.category and expense_info["Date"] == self.date:
                    self.expenses.remove(expense_info)
                    print(f"\n{expense_info['Amount']} {self.expense} has been deleted alongisde its information")
                    break
                else:
                    continue
    # Creating the function that clears all expenses
    def clear_all_expenses(self):
        # Check if expense tracker data exists
        if not self.expenses:
            print("\nNo data found to proceed")
        else:
            self.expenses.clear()
            print("\nThe expense tracker has been cleared")
    # Creating the function that edits an expenses attribute
    def edit_expense_attribute(self):
        # Asking for the expense while checking if its valid or not
        while True:
            self.expense = input("Enter the expense whose attribute you would like to edit ->: ").capitalize()
            if not self.expense:
                print("Enter a valid expense")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.expense} ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the date while checking if its valid or not
        while True:
            try:
                self.date = date.fromisoformat(input(f"Enter the date of when {self.expense} was bought in this format(YYYY-MM-DD) ->: ").strip())
                # Checking if the date is in the future or not
                if datetime.now().date() < self.date:
                    print(f"Enter a date that isn't in the future(Todays date: {datetime.now().date()})")
                else:
                    break
            except ValueError:
                print('Invalid date parameters therefore we will start over')
        # Check if the expense information exists 
        if not any(self.expense == expense_info["Expense"] and self.category == expense_info["Category"] and self.date == expense_info["Date"] for expense_info in self.expenses):
            print("\nNo such expense information found")
        else:
            # Looping through each expense information
            for expense_info in self.expenses:
                if expense_info["Expense"] == self.expense and expense_info["Category"] == self.category and expense_info["Date"] == self.date:
                    self.option = input(f"Enter the attribute of {self.expense} that you would like to edit(Enter N for Name, C for Category, A for Amount, P for Price, D for Date) ->: ").upper().strip()
                    if self.option == 'N':
                        # Asking for the expense while checking if its valid or not
                        while True:
                            self.expense = input(f"Enter the new version of {expense_info['Expense']} ->: ").capitalize()
                            if not self.expense:
                                print("Enter a valid expense")
                            elif expense_info["Expense"] == self.expense:
                                print("\nThe expense name is already the same")
                                break
                            else:
                                print(f"\nThe expense {expense_info['Expense']} has been edited into {self.expense}")
                                expense_info["Expense"] = self.expense
                                break
                        break
                    elif self.option == "C":
                        # Asking for the category while checking if its valid or not
                        while True:
                            self.category = input(f"Enter the new category of {self.expense}(Food, Transportation, etc.) ->: ").capitalize()
                            if not self.category:
                                print("Enter a valid category")
                            elif expense_info["Category"] == self.category:
                                print("\nThe category name is already the same")
                                break
                            else:
                                print(f"\nThe expense {expense_info['Expense']}'s category {expense_info['Category']} has been edited into {self.category}")
                                expense_info["Category"] = self.category
                                break
                        break
                    elif self.option == 'A':
                        # Setting the total price to the original singular price to do the calculations after the new input
                        self.price = expense_info["Price"] / expense_info["Amount"]
                        # Asking for the new amount while checking if its valid or not
                        while True:
                            try:
                                self.amount = int(input(f"Enter the new amount of {self.expense} you have bought ->: "))
                                if self.amount <= 0:
                                    print("Enter a valid amount that is bigger than 0")
                                elif expense_info["Amount"] == self.amount:
                                    print("\nThe amount is already the same")
                                    break
                                else:
                                    print(f"\nThe amount of {self.expense}s bought has been edited from {expense_info['Amount']} into {self.amount} alongside its total price")
                                    expense_info["Amount"] = self.amount
                                    expense_info["Price"] = self.price*expense_info["Amount"]
                                    break
                            except ValueError:
                                print("Invalid amount")
                        break
                    elif self.option == "P":
                        # Asking for the new singular price while checking if its valid or not
                        while True:
                            try:
                                self.price = float(input(f"Enter the new price of one {self.expense} ->: "))
                                if self.price <= 0:
                                    print("Enter a valid price")
                                elif self.price == expense_info["Price"] / expense_info["Amount"]:
                                    print("\nThe singular price is already the same")
                                    break
                                else:
                                    print(f"\nThe total price of {self.expense} has been edited from {expense_info['Price']:.2f} into {expense_info['Amount']*self.price:.2f}")
                                    expense_info["Price"] = expense_info["Amount"]*self.price
                                    break
                            except ValueError:
                                print("Invalid price")
                        break
                    elif self.option == "D":
                        # Asking for the date while checking if its valid or not
                        while True:
                            try:
                                self.date = date.fromisoformat(input(f"Enter the date of when {self.expense} was bought in this format(YYYY-MM-DD) ->: ").strip())
                                if self.date == expense_info["Date"]:
                                    print("\nThe date is already the same")
                                    break
                                elif datetime.now().date() < self.date:
                                    print(f"Enter a date that isn't in the future(Todays date: {datetime.now().date()})")
                                else:
                                    print(f"\nThe date of the expense {self.expense} has been edited from {expense_info['Date']} into {self.date}")
                                    expense_info["Date"] = self.date
                                    break
                            except ValueError:
                                print("Invalid date parameters therefore we will start over")
                        break
                    else:
                        print("\nInvalid option")
                else:
                    continue
    # Creating the function that displays specific expenses
    def search_expense(self):
        # Asking for the expense while checking if its valid or found
        while True:
            self.expense = input("Enter the expense that you would like to search ->: ").capitalize()
            if not self.expense:
                print("Enter a valid expense")
            elif all(self.expense != expense_info["Expense"] for expense_info in self.expenses):
                print("\nNo such expense found")
                break
            else:
                print(f"\nExpenses with the name {self.expense}: ")
                # Looping through each expense information
                for expense_info in self.expenses:
                    if expense_info["Expense"] == self.expense:
                        print()
                        # Looping through the keys and values
                        for expense_info_key, expense_info_value in expense_info.items():
                            if expense_info_key == "Price":
                                print(f"{expense_info_key} -> {expense_info_value:.2f}")
                            else:
                                print(f"{expense_info_key} -> {expense_info_value}")
                    else:
                        continue
            break
    # Creating the function that displays the expenses according to a specific category
    def display_expenses_category(self):
        # Asking for the category while checking if its valid or found
        while True:
            self.category = input("Enter the category(Food, Transportation, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            elif all(self.category != expense_info["Category"] for expense_info in self.expenses):
                print("\nNo such category found")
                break
            else:
                print(f"Expenses({self.category}): ")
                # Looping through each expense information
                for expense_info in self.expenses:
                    if expense_info["Category"] == self.category:
                        print()
                        # Looping through the keys and values
                        for expense_info_key, expense_info_value in expense_info.items():
                            if expense_info_key == "Price":
                                print(f"{expense_info_key} -> {expense_info_value:.2f}")
                            else:
                                print(f"{expense_info_key} -> {expense_info_value}")
                    else:
                        continue
            break
    # Creating the function that displays the expenses according to a specific date
    def display_expenses_date(self):
        # Asking for the date while checking if its valid or not
        while True:
            try:
                self.date = date.fromisoformat(input(f"Enter the date in this format(YYYY-MM-DD) ->: ").strip())
                if all(self.date != expense_info["Date"] for expense_info in self.expenses):
                    print("\nNo such date found")
                else:
                    print(f"\nExpenses(Date: {self.date})")
                    # Looping through each expense information
                    for expense_info in self.expenses:
                        if expense_info["Date"] == self.date:
                            print()
                            # Looping through the keys and values
                            for expense_info_key, expense_info_value in expense_info.items():
                                if expense_info_key == "Price":
                                    print(f"{expense_info_key} -> {expense_info_value:.2f}")
                                else:
                                    print(f"{expense_info_key} -> {expense_info_value}")
                        else:
                            continue
                    break
                break
            except ValueError:
                print("Invalid date parameters therefore we will start over")
    # Creating the function that displays the total price
    def display_total_price(self):
        # Check if expense tracker data exists
        if not self.expenses:
            print("\nNo data found to proceed")
        else:
            print(f"\nTotal price spent: \n{sum(expense_info['Price'] for expense_info in self.expenses):.2f}")
    # Creating the function that displays the total price according to a specific category
    def display_total_price_category(self):
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input("Enter the category to display how much was spent(Food, Transportation, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            elif all(self.category != expense_info["Category"] for expense_info in self.expenses):
                print("\nNo such category found")
                break
            else:
                print(f"\nTotal price spent({self.category}): {sum(expense_info['Price'] for expense_info in self.expenses if expense_info['Category'] == self.category):.2f}")
                break
    # Creating the function that displays the average expense price
    def display_average_price(self):
        # Check if expense tracker data exists
        if not self.expenses:
            print("\nNo data found to proceed")
        else:
            print(f"\nAverage price spent: {mean(expense_info['Price'] for expense_info in self.expenses):.2f}")
    # Creating the function that displays the most expensive expense price
    def display_most_expensive_price(self):
        # Check if expense tracker data exists
        if not self.expenses:
            print("\nNo data found to proceed")
        else:
            # Looping through each expense information
            for expense_info in self.expenses:
                if expense_info['Price'] == max(expense_info['Price'] for expense_info in self.expenses):
                    print(f"\nThe most expensive expense and it's price:\n{expense_info['Expense']}: {expense_info['Price']:.2f}")
                else:
                    continue
    # Creating the function that displays the cheapest expense price
    def display_cheapest_price(self):
        # Check if expense tracker data exists
        if not self.expenses:
            print("\nNo data found to proceed") 
        else:
            # Looping through each expense information
            for expense_info in self.expenses:
                if expense_info['Price'] == min(expense_info['Price'] for expense_info in self.expenses):
                    print(f"\nThe cheapest expense and it's price:\n{expense_info['Expense']}: {expense_info['Price']:.2f}")
                else:
                    continue
    # Creating the function that sets a budget and checks if its eligible with the expenses
    def set_budget_and_check(self):
        # Check if expense tracker data exists
        if not self.expenses:
            print("\nNo data found to proceed")
        else:
            # Asking for the budget while checking if its valid or not
            while True:
                try:
                    self.budget = float(input("Enter the budget ->: "))
                    if self.budget <= 0:
                        print("Enter a valid budget that is bigger than 0")
                    elif self.budget < sum(expense_info['Price'] for expense_info in self.expenses):
                        print("\nThe budget is not enough you can enter a new one")
                        # Looping through each expense information
                        for expense_info in self.expenses:
                            if sum(expense_info['Price'] for expense_info in self.expenses) - expense_info["Price"] < self.budget:
                                print(f'or you can remove {expense_info["Expense"]} which will be enough for your budget and have {self.budget - (sum(expense_info["Price"] for expense_info in self.expenses) - expense_info["Price"]):.2f} leftover')
                            elif sum(expense_info['Price'] for expense_info in self.expenses) - expense_info["Price"] == self.budget:
                                print(f'or you can remove {expense_info["Expense"]} but have nothing leftover')
                            else:
                                continue
                        break
                    elif self.budget == sum(expense_info['Price'] for expense_info in self.expenses):
                        print("\nThe budget is enough but you won't have any change leftover")
                        break
                    else:
                        print(f"\nThe budget is enough and you will have {self.budget - sum(expense_info['Price'] for expense_info in self.expenses):.2f} leftover")
                        break
                except ValueError:
                    print("Invalid budget")
# Creating the class that is responsible for the CLI commands while inheriting most of the variables from the ExpenseTracker class to avoid AttributeError's
class ExpenseTrackerCLI(ExpenseTracker):
    # Creating the function that displays the options and asks the user what they want
    def display_menu(self):
        ExpenseTrackerData.read_data(self)
        print("--- Expense Tracker ---")
        while True:
            print("\n1. Add a new expense")
            print("2. View all expenses")
            print("3. Delete an expense")
            print("4. Clear all expenses")
            print("5. Edit an expense's attribute(Name/Category/Price/Amount/Date)")
            print("6. Search a specific expense")
            print("7. View expenses according to a specific category")
            print("8. View expenses according to a specific date")
            print("9. View total price spent")
            print("10. View total price spent according to a specific category")
            print("11. View average price")
            print("12. View the most expensive expense")
            print("13. View the cheapest expense")
            print("14. Set a budget and check")
            print("15. Exit")
            self.option = input("Enter your option(1-15) ->: ")
            if self.option == '1':
                ExpenseTracker.add_new_expense(self)
            elif self.option == '2':
                ExpenseTracker.display_all_expenses(self)
            elif self.option == '3':
                ExpenseTracker.delete_expense(self)
            elif self.option == '4':
                ExpenseTracker.clear_all_expenses(self)
            elif self.option == '5':
                ExpenseTracker.edit_expense_attribute(self)
            elif self.option == '6':
                ExpenseTracker.search_expense(self)
            elif self.option == '7':
                ExpenseTracker.display_expenses_category(self)
            elif self.option == '8':
                ExpenseTracker.display_expenses_date(self)
            elif self.option == '9':
                ExpenseTracker.display_total_price(self)
            elif self.option == '10':
                ExpenseTracker.display_total_price_category(self)
            elif self.option == '11':
                ExpenseTracker.display_average_price(self)
            elif self.option == '12':
                ExpenseTracker.display_most_expensive_price(self)
            elif self.option == '13':
                ExpenseTracker.display_cheapest_price(self)
            elif self.option == '14':
                ExpenseTracker.set_budget_and_check(self)
            elif self.option == '15':
                print("Ok wait a moment...")
                sleep(1.5)
                print('Saving data...')
                ExpenseTrackerData.write_data(self)
                sleep(2)
                print('Exiting...')
                sleep(1.5)
                break
            else:
                print("\nInvalid option")
# Creating the class that is responsible for the data saving
class ExpenseTrackerData:
    # Initializing one variable thats gonna be used in this class
    def __init__(self):
        self.expenses = []
    # Creating the function that reads the data from the file and writes it into the program
    def read_data(self):
        # Check if the file exists
        if Path("expense_tracker.json").is_file():
            with open("expense_tracker.json", "r") as f:
                # Loading the data before converting the strings into datetime objects
                self.expenses = json.load(f)
                # Looping through each expense information
                for expense_info in self.expenses:
                    # Looping through the keys and values
                    for expense_info_key, expense_info_value in expense_info.items():
                        if expense_info_key == "Date":
                            expense_info[expense_info_key] = date.fromisoformat(expense_info_value)
    # Creating the function that reads the data from the program and writes it into the file
    def write_data(self):
        with open("expense_tracker.json", "w") as f:
            # Looping through each expense information
            for expense_info in self.expenses:
                # Looping through the keys and values
                for expense_info_key, expense_info_value in expense_info.items():
                    if expense_info_key == "Date":
                        expense_info[expense_info_key] = date.isoformat(expense_info_value)
            # Saving the data after converting the datetime objects into strings to avoid TypeError's
            json.dump(self.expenses, f)
expense_tracker = ExpenseTrackerCLI().display_menu()