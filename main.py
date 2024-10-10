
# ### 1. Easy Challenge: **Shopping Cart Total**
# Write a program that allows a user to add items to a shopping cart and calculate the total price. 
# store = {
#     'Basket' : 100,
#     'Shoes' : 50,
#     'Jeans' : 10,
#     'Hat' : 50,
#      }

# total_cart_value = 0
    
# def add_item_to_cart(choices):
#     return store[choices]

# while True:
        
#     for k,v in store.items():
#         print(f"{k}: ${v}")
#     choices = input("What items do you want to add to your cart?").title()


#     if choices in store:
#         print(f"Great news, {choices} is available. It has been added to your cart.")
#         total_cart_value += add_item_to_cart(choices)
#     else: 
#         print(f"Unfortunatley {choices} is not in stock")


#     print("Current value of cart: $", total_cart_value)

# - Create a function called `add_item_to_cart(item)` that takes an item and its price and **returns** the item price.
# - In the main loop, add up the return values from `add_item_to_cart(item)` to calculate the **total cart value**.

# Hints:
# - Use a dictionary to store items and their prices.
# - Call `add_item_to_cart(item)` and **store the result** to update the cart total.


# ### 2. Intermediate Challenge: **Savings Account Deposits**
# Simulate a savings account where a user can make deposits over time. Your goal is to:

# balance = 0

# def deposit(amount):
#     return amount

# while True:

#     amount = int(input("Please enter deposit amount"))

    
#     if amount > 0:
#         balance += deposit(amount)
#         print("$",balance)

# - Write a function `deposit(amount)` that takes a deposit amount and **returns** the new balance to be added.
# - In the main part of the program, repeatedly ask the user for deposit amounts and keep adding to a **global balance** using the return value from `deposit(amount)`.

# Hints:
# - You need to **keep track of the total balance** by updating it with the **returned value** from `deposit(amount)`.
# - Think about how you only update the balance if the deposit is valid (e.g., positive value).


# ### 3. Advanced Challenge: **Project Budget Tracker**
# Imagine you're managing a project and need to track the budget. The goal is to:



# - Write two functions:
#   - **`spend_funds(project, amount)`**: Checks if the current project budget can cover the amount. If yes, **returns the spent amount**; otherwise, return zero.
#   - **`allocate_funds(project, amount)`**: Adds funds to the project and **returns the updated allocation**.
# - Track multiple projects, each with a different budget, and allow the user to **allocate** and **spend** funds for specific projects.

# Hints:
# - Use a dictionary to manage **project budgets**.
# - When spending or allocating funds, use the **returned value** to adjust the overall project budgets.
# - Handle conditions like **insufficient funds** or **invalid allocations** properly.

# ### General Advice
# - In each problem, make sure you **return values** from your functions that represent **updates** or **results**.
# - Assign the return values in the main code to the appropriate variables to **update** them globally.

# Try these exercises, and let me know if any particular part confuses you or if you need more hints!

tracker = {'Project A' : 4000}

def add_project(name, budget=0):
    tracker[name] = budget

while True:
    
    choice = str(input("What would you like to do? Choices: 'view', 'add', 'allocate', 'spend'?, 'exit' \n")).lower()

    if choice == 'view':
        for k,v in tracker.items(): print(f"{k}: ${v}")
    elif choice == 'add':
        name = input('Please enter project name').title()
        add_project(name)
    elif choice == 'allocate':
        pass
    elif choice == 'spend':
        pass
    elif choice == 'exit':
        break
    else: print("Sorry, didn't understand your input")

