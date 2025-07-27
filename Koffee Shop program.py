# drinks (name: price, type, total stock, id)
# books (name: genre, author, total stock, id(1,2,3))

drinks = {    
    'Latte': {
        "type": "",
        "total_stock": 0,
        "price": 2.50,
        "calories": 125,
        "id": 1
    },    
    "cappucino": {
        "type": "", 
        "total_stock": 25,
        "price": 3.00,
        "calories": 225,
        "id": 2
    }, 
    'espresso': {
        "type": "",
        "total_stock": 25,
        "price": 1.50,
        "calories": 25,
        "id": 3
    }
}

books = {
    "Lord of the Rings" : {
            "genre": "Thriller",
            "author": "J.R.R. Tolkien",
            "price": 8.99,
            "total_stock": 20,
            "Book ID": "BK100"
        },
        "A Brief History of Time": {
            "genre": "Science",
            "author": "Stephen Hawking",
            "price": 10.50,
            "total_stock": 15,
            "Book ID": "BK111"
        },
        "Pride and Prejudice": {
            "genre": "Romance",
            "author": "Jane Austen",
            "price": 6.75,
            "total_stock": 25,
            "Book ID": "BK112"
        }
}

sweets = {
    "Chocolate Chip Cookie": {
        "category": "Cookie",
        "price": 1.50,
        "flavour": "Chocolate Chip",
        "total_stock": 30,
        "calories": 180,
        "id": 1
    },
    "Fudge Brownie": {
        "category": "Brownie",
        "price": 2.00,
        "flavour": "Double Chocolate",
        "total_stock": 25,
        "calories": 250,
        "id": 2
    },
    "Classic Cinnamon Roll": {
        "category": "Cinnamon Roll",
        "price": 2.75,
        "flavour": "Cinnamon & Sugar",
        "total_stock": 20,
        "calories": 320,
        "id": 3
    }
}

# - Display a list of the menu and book items 
# Create function to display drink
# Create function to display books
# Create function to display sweets
# Create function to display all items like this (Name: , ID: )
all_menu = [sweets, drinks, books] # 3 Dictionaries in a list
select_menu = input("Select which menu: Sweets, Drinks, Books or All ")


print(f"Menu Selection: {select_menu}") # Prints out what the user inputted

if select_menu == 'All': # Prints out every item in every menu
    for menu in all_menu:
        for name, info in menu.items():
            print(f"Item Name: {name}")
elif select_menu == 'sweets': # Prints out just sweets
    for sweet, info in sweets.items():
        print(f"\nSweet: {sweet}")
        print(f"Price: {info['price']}")
        print(f"Category: {info['category']}")
        print(f"Flavour: {info['flavour']}")
        print(f"Total Stock: {info['total_stock']}")
elif select_menu == 'drinks':
    for drink, info in drinks.items():
        print(f"\nDrink: {drink}")
        print(f"Price: {info['price']}")
        print(f"Type: {info['type'] if info['type'] else 'N/A'}")
        print(f"Calories: {info['calories']}")
        print(f"Total Stock: {info['total_stock']}")
        print(f"ID: {info['id']}")
elif select_menu == 'books':
    for book, info in books.items():
        print(f"\nBook: {book}")
        print(f"Author: {info['author']}")
        print(f"Genre: {info['genre']}")
        print(f"Price: {info['price']}")
        print(f"Total Stock: {info['total_stock']}")
        print(f"Book ID: {info['Book ID']}")

# The Koffee Shop

# Your client has a range of functionality they require in their app:
# - Allow customers to order food, drinks, and books - Task
# Let the customer choose what they want
# How much they want and then minus that from total stock
# If stock == 0  then say unavailable, would you like to order something else
# Return receipt - Total Cost, All Items, Price, Quantity
# Remove stuff from receipt

# While 
# IF item is not in menu then say not in menu 
# IF item total stock = 0 then out of stock
# 1 - Input - What do you want to order:
# 2 - Append to order_list and deduct from total_stock
# 3 - Would you like anything else?

available_items = [] # Basically append all items with stock > 0 into this list
unavailable_items = []

print("\nThis is for everything")
for menu in all_menu:
    for name, info in menu.items():
        print(f"Item Name: {name}")
        print(f"Total Stock: {info['total_stock']}")
        if info["total_stock"] > 0:
            available_items.append(name)
        else:
            unavailable_items.append(name)

# Customer Order
combined_order = [] 

for item in available_items:
    print(f"These are the items available today: {item}")

# 2 Issues
# Total Stock not updating

while combined_order != 'done': # Keep on asking customer to add item until they 'done'
    enter_item = input("What would you like today? ") # Enter what you want
    if enter_item in available_items:
        combined_order.append(enter_item) # Add each item to receipt list
        print(combined_order)
    else:
        print(f"{enter_item} not available")
        print("If order finished, enter 'done'")

### example_receipt = {
   # "espresso":
   # {
  #      "quantity ordered": # entered_quantity 
   #     "total price": # quantity * price
 #   },
    
 #   "Chocolate Chip Cookie":
##    {
  #      "quantity ordered": # entered_quantity
 #       "total price": # quantity * price
#    }
#}

      
