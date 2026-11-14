import json
from statistics import mean
from datetime import date
from math import isfinite
from time import sleep
# The class that is responsible for the expense factors(adding, viewing, deleting, etc.)
class ExpenseTracker:
    # Initialized variables that will be used in this class
    def __init__(self):
        self.expenses = []
    # The function that adds a new expense into the expenses list
    def add_expense(self, function):
        try:
            expense = function("expense that you would like to add")
            category = function(f"category of {expense}")
            amount = int(function(f"amount of {expense}(s) you got"))
            if amount <= 0:
                print("\nEnter a positive amount.")
                return
            price = float(function(f"price of one {expense}"))
            # Checks if the price is a valid value that can be parsed in a JSON structure
            if not isfinite(price) or 0 >= price:
                print("\nEnter a valid positive price that isn't NaN or infinite.")
                return  
            expense_date = date.fromisoformat(function(f"date of when you bought {expense} in this format: (YYYY-MM-DD)"))
            # Checks if the date input has not bypassed the current date
            if expense_date > date.today():
                print(f"\nEnter a date that isn't after the date {date.today()}.")
                return
            print(f"\n{amount} {expense}(s) has been added.(ID: {len(self.expenses)+1})")
            self.expenses.append({"ID": len(self.expenses)+1, "Expense": expense, "Amount": amount, "Price": amount*price, "Category": category, "Date": expense_date})
        except (ValueError, OverflowError) as e:
            print(f"\n{e}")
    # The function that displays the expenses
    def display_expenses(self, parameter, parameter_value):
        # Checks if data even exists in the expenses list
        if not self.expenses:
            print("\nNo data found to proceed.")
            return
        if parameter_value == True:
            print("\nExpenses: ")
            print("\nID | Expense | Amount | Price | Category | Date")
            for expense_info in self.expenses:
                print(f"{expense_info['ID']})   {expense_info['Expense']}     {expense_info['Amount']}      {expense_info['Price']:.2f}    {expense_info['Category']}   {expense_info['Date']}")
            return
        print(f"\nExpenses({parameter} -> {parameter_value}): ")
        print("\nID | Expense | Amount | Price | Category | Date")
        for expense_info in self.expenses:
            if expense_info[parameter] == parameter_value:
                print(f"{expense_info['ID']})   {expense_info['Expense']}     {expense_info['Amount']}      {expense_info['Price']:.2f}    {expense_info['Category']}   {expense_info['Date']}")
    # The function that deletes an expense by getting the ID input
    def delete_expense(self, function):
        if not self.expenses:
            print("\nNo data found to proceed.")
            return
        self.display_expenses(None, True)
        expense_id = function(self.expenses)
        for expense_info in self.expenses:
            if expense_info["ID"] == expense_id:
                print(f"\nThe expense with the ID {expense_info['ID']} has been deleted from the expenses.")
                self.expenses.remove(expense_info)
                self.reload_ids()
                break
    # The function that clears the expenses
    def clear_expenses(self, function):
        if not self.expenses:
            print("\nNo data found to proceed.")
            return
        if function() == 'y':
            print("\nThe expenses has been cleared.")
            self.expenses.clear()
            return
        print("\nOk we will proceed as usual.")
    # The function that can edit an expense's specific attribute such as it's name, price, category, etc.
    def edit_expense(self, function, function2, function3, text: str):
        categories = {
            "Expense": str,
            "Amount": int, 
            "Price": float,
            "Date": date.fromisoformat,
            "Category": str
        }
        if not self.expenses:
            print("\nNo data found to proceed.")
            return
        self.display_expenses(None, True)
        expense_id = function(self.expenses)
        edit_option = function2()
        for expense_info in self.expenses:
            if expense_info["ID"] != expense_id:
                continue
            initial_value, final_value = expense_info[edit_option], categories[edit_option](function3(text))
            if type(final_value) is int and final_value <= 0:
                print("\nEnter a valid positive amount.")
                break
            if type(final_value) is float and (final_value <= 0 or not isfinite(final_value)):
                print("\nEnter a valid positive price that isn't NaN or infinite.")
                break
            if initial_value == final_value:
                print("\nThe value is already the same.")
                break
            if type(final_value) is date and date.today() < final_value:
                print(f"\nEnter a date that isn't after {date.today()}")
                break
            if type(final_value) is int:
                expense_info["Price"] /= initial_value
                expense_info["Price"] *= final_value
                expense_info["Amount"] = final_value
            else:
                expense_info[edit_option] = final_value
            print(f"\nThe {edit_option} of the expense with the ID {expense_id} has been edited.")
            break
    # The function that searches an expense according to a name
    def search_expenses(self, function):
        if not self.expenses:
            print("\nNo data found to proceed.")
            return
        expense = function("expense name")
        if all(expense != expense_info["Expense"] for expense_info in self.expenses):
            print("\nNo such expense found.")
            return
        self.display_expenses("Expense", expense)
    # The function that displays the statistics such as the most expensive, the cheapest, the average and the total cost
    def display_statistics(self):
        print("\nStatistics: ")
        # Checks if data even exists in the expenses list
        if not self.expenses:
            print("\nNo data found.")
            return
        print(f"""
        \nMost expensive expense: {max(expense_info['Price'] for expense_info in self.expenses):.2f}
Cheapest expense: {min(expense_info['Price'] for expense_info in self.expenses):.2f}
Total expense cost: {sum(expense_info["Price"] for expense_info in self.expenses):.2f}
Average expense cost: {mean(expense_info['Price'] for expense_info in self.expenses):.2f}
        """)
    # The function that reloads the ID's
    def reload_ids(self):
        for index, expense_info in enumerate(self.expenses, start=1):
            expense_info["ID"] = index
# The class that is responsible for the CLI commands which are mostly user inputs
class ExpenseTrackerCLI:
    # Initialized classes that will be used in this class
    def __init__(self):
        self.expense_tracker = ExpenseTracker()
        self.data = ExpenseTrackerJSON()
    # The function that asks for an input such as the expenses name, price, category, etc.
    def ask_input(self, text: str) -> str:
        while True:
            user_input = input(f"Enter the {text} ->: ").capitalize().strip()
            if user_input:
                return user_input
            print("Enter a valid input.")
    # The function that asks the user for an ID input
    def id_input(self, storage: list) -> int | None:
        while True:
            try:
                expense_id = int(input("Enter the ID ->: "))
                if 0 < expense_id <= len(storage):
                    return expense_id
                print('Invalid ID.')
            except ValueError:
                print("Enter a valid ID.")
    # The function that asks the user what they want to edit
    def edit_attribute_input(self) -> str:
        print("\nDISCLAIMER: EDITING THE PRICE DOESN'T CHANGE THE INDIVIDUAL PRICE BUT CHANGES THE TOTAL PRICE\n")
        while True:
            user_input = input(f"Enter the attribute that you would like to change(Expense, Price, Amount, Date, Category) ->: ").capitalize().strip()
            if user_input in ("Expense", "Category", "Date", "Price", "Amount"):
                return user_input
            print("Enter a valid option.(Options: Expense, Price, Amount, Date, Category)")
    # The function that checks if the user really wants to clear the entire expenses list
    def clear_expenses_input(self) -> str:
        while True:
            user_input = input("Are you sure you want to clear the entire expenses?(y/n) ->: ").lower().strip()
            if user_input in ("y", "n"):
                return user_input
            print('Enter a valid option.(Options: y, n)')
    # The function that displays the options
    def display_options(self):
        print("""
1. Add an expense\n2. View expenses\n3. Delete an expense\n4. Clear all expenses\n5. Edit an expense\n6. View expenses according to a specific category\n7. View expenses according to a specific date\n8. Search for an expense\n9. View statistics\n10. Exit
        """)
    # The function that runs the program
    def run_program(self):
        print("--- EXPENSE TRACKER ---")
        self.expense_tracker.expenses = self.data.read_file()
        while True:
            self.display_options()
            option = input("Enter your option(1-10) ->: ").strip()
            if option == '1':
                self.expense_tracker.add_expense(self.ask_input)
            elif option == '2':
                self.expense_tracker.display_expenses(None, True)
            elif option == '3':
                self.expense_tracker.delete_expense(self.id_input)
            elif option == '4':
                self.expense_tracker.clear_expenses(self.clear_expenses_input)
            elif option == '5':
                self.expense_tracker.edit_expense(self.id_input, self.edit_attribute_input, self.ask_input, "new version")
            elif option == '6':
                category = self.ask_input("category to display the expenses")
                if all(category != expense_info["Category"] for expense_info in self.expense_tracker.expenses):
                    print("\nNo such category found.")
                    continue
                self.expense_tracker.display_expenses("Category", category)
            elif option == '7':
                try:
                    date_input = date.fromisoformat(self.ask_input("date to display the expenses"))
                    if date_input > date.today():
                        print(f"\nEnter a date that isn't after the date {date.today()}")
                        continue
                    if all(date_input != expense_info["Date"] for expense_info in self.expense_tracker.expenses):
                        print(f"\nNo such expense found with the date {date_input}.")
                        continue
                    self.expense_tracker.display_expenses("Date", date_input)
                except ValueError as e:
                    print(f'{e}')
            elif option == '8':
                self.expense_tracker.search_expenses(self.ask_input)
            elif option == '9':
                self.expense_tracker.display_statistics()
            elif option == '10':
                print("Ok wait a moment...")
                sleep(1.5)
                print("Saving data...")
                self.data.write_file(self.expense_tracker.expenses)
                sleep(2)
                print("Exiting...")
                sleep(1.5)
                break
            else:
                print("\nInvalid option.")
# The class that is repsonsible for the JSOn data saving/parsing
class ExpenseTrackerJSON:
    # The function that validates the JSON structure of a file
    def validate_json(self, storage: list) -> bool:
        if type(storage) is not list:
            return False
        for index, expense_info in enumerate(storage, start=1):
            if type(expense_info) is not dict:
                return False
            if set(expense_info.keys()) != {"ID", "Expense", "Price", "Amount", "Category", "Date"}:
                return False
            if type(expense_info["ID"]) is not int or type(expense_info["Expense"]) is not str or type(expense_info["Price"]) not in (float, int) or not isfinite(expense_info["Price"]) or type(expense_info["Amount"]) is not int or type(expense_info["Category"]) is not str or type(expense_info["Date"]) is not str or expense_info["Price"] <= 0 or expense_info["Amount"] <= 0:
                return False
            if expense_info["ID"] != index:
                return False
        return True
    # The function that reads the data from the file and loads it into the program
    def read_file(self) -> list:
        try:
            with open("expense_tracker.json", encoding="utf-8") as f:
                data = json.load(f)
                if self.validate_json(data):
                    for expense_info in data:
                        expense_info["Date"] = date.fromisoformat(expense_info["Date"])
                    return data
                return []
        except FileNotFoundError:
            return []
        except OSError as e:
            print(f"\n{e}")
            return []
        except json.JSONDecodeError as e:
            print(f"\n{e}\nIt seems that the file has corrupted JSON data, this could occur if the creator of this program has updated the structure of the JSON parsing.\nTherefore the expenses will be reset.\nWe thank you for your understanding.\n")
            return []
        except ValueError as e:
            print(f"{e}")
            return []
    # The function that retireves the data from the program and writes it into the file
    def write_file(self, storage: list):
        try:
            with open("expense_tracker.json", "w", encoding="utf-8") as f:
                for expense_info in storage:
                    expense_info["Date"] = date.isoformat(expense_info["Date"])
                json.dump(storage, f, ensure_ascii=False, sort_keys=True, indent=4, allow_nan=False)
        except OSError as e:
            print(f"\n{e}")
ExpenseTrackerCLI().run_program()
