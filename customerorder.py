 
# Import the dictionaries from another file that contain our menu items
from menudictionary import drinks, books, sweets
# Combine all individual menus (sweets, drinks, and books) into one list for easy iteration
all_menu = [sweets, drinks, books]
# This is where we'll store the items that the customer adds to their basket
basket = []
# This dictionary will store the mapping of item numbers to the actual items
numbered_items = {}
# 📋 Function to show all available items (those that are in stock)
def show_all_items():
    print("\n📋 Available Items:")  # Title for the available items list
    numbered_items.clear()  # Clear the previous mapping to avoid duplication
    count = 1  # Initialize the item number (1 for the first item)
    # Loop through each menu (sweets, drinks, and books)
    for menu in all_menu:
        # Loop through each item in the menu
        for item, info in menu.items():
            if info['total_stock'] > 0:  # Check if the item is in stock (not sold out)
                numbered_items[str(count)] = (item, info)  # Store the item and its details
                # Display the item with its price and the corresponding number
                print(f"{count}. {item} (${info['price']:.2f})")
                count += 1  # Increment the number for the next item
# ➕ Function to add an item to the basket based on its number
def add_to_basket(item_number):
    if item_number in numbered_items:  # Check if the entered number corresponds to an item
        item_name, info = numbered_items[item_number]  # Get the item name and details
        
        # Find the menu (sweets, drinks, or books) where this item is located and reduce stock
        for menu in all_menu:
            if item_name in menu:  # If the item is found in the current menu
                menu[item_name]['total_stock'] -= 1  # Reduce the stock by 1
                break
        
        # Add the item to the basket with its name and price
        basket.append({'name': item_name, 'price': info['price']})
        return True  # Indicate the item was added successfully
    return False  # Indicate the item number was invalid or out of stock
# 🧾 Function to display the basket contents and show the total price
def show_receipt():
    print("\n🧾 Your Receipt:")  # Title for the receipt
    total = 0  # Initialize the total price of the order
    
    # Loop through each item in the basket
    for item in basket:
        # Print the name and price of each item
        print(f"- {item['name']}: ${item['price']:.2f}")
        total += item['price']  # Add the price to the total sum
    
    # Show the total price at the end of the receipt
    print(f"\n💰 Total: ${total:.2f}")
    return total  # Return the total so we can use it for discount later
# 🔐 Function to verify employee credentials and apply a discount
def apply_employee_discount(total):
    print("\n🔐 Employee Discount Verification")  # Ask for employee credentials
    
    # Prompt for username and password
    username = input("Username: ").strip().lower()  # Input username, make lowercase to ignore case
    password = input("Password: ").strip()  # Input password
    
    # Verify the credentials (hardcoded for this example)
    if username == 'tobias' and password == 'bode':  # Check if both username and password are correct
        while True:
            try:
                # Ask the employee how much discount they want to apply (up to 50%)
                discount_input = float(input("Enter discount percentage (max 50%): "))
                if 0 <= discount_input <= 50:  # Check if the discount is valid (between 0 and 50%)
                    discount_amount = total * (discount_input / 100)  # Calculate the discount amount
                    new_total = total - discount_amount  # Subtract the discount from the total
                    print(f"\n✅ Discount applied: {discount_input:.0f}% off")  # Confirm the discount
                    print(f"💳 New Total: ${new_total:.2f}")  # Show the new total after discount
                    return  # Exit the function once the discount is applied
                else:
                    print("❌ Discount must be between 0% and 50%")  # Error if discount is out of range
            except ValueError:  # Handle invalid input if the employee doesn't enter a valid number
                print("❌ Please enter a valid number.")  # Error message for invalid input
    else:
        print("❌ Invalid employee credentials. No discount applied.")  # Error if credentials are wrong
# 🛒 Main function that runs the order flow
def take_order():
    # Show all available items (those in stock) with their item number
    show_all_items()
    # Keep allowing the customer to pick items until they type 'done'
    while True:
        item_number = input("\nEnter item number to add to basket (or type 'done'): ").strip()
        if item_number.lower() == 'done':  # If the customer types 'done', stop adding items
            break
        elif add_to_basket(item_number):  # If the item is valid, add it to the basket
            item_name = numbered_items[item_number][0]  # Get the item name from the lookup
            print(f"✅ {item_name} added to your basket.")  # Confirm the item was added
        else:
            print("❌ Invalid selection or item is out of stock.")  # Error if item number is invalid or out of stock
    # Show the final receipt and get the total price
    total = show_receipt()
    # Ask if the customer wants to apply an employee discount
    apply = input("\nApply employee discount? (yes/no): ").strip().lower()
    if apply == 'yes':  # If the customer wants to apply a discount
        apply_employee_discount(total)  # Apply the discount and show the updated total
    else:
        print("👋 Thank you for your order!")  # If no discount, thank the customer for their order
# Run the order function only if this file is executed directly (not imported)
if __name__ == "__main__":
    take_order()  # Start the order process when the script is run
 
 