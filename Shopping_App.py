def main():
    print("Welcome to the Demo Marketplace")

    # User login
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users_db and users_db[username] == password:
        print("User login successful.")
        user_functionalities()
    elif username in admins_db and admins_db[username] == password:
        print("Admin login successful.")
        admin_functionalities()
    else:
        print("Invalid username or password")

def user_functionalities():
    while True:
        print("\nUser Functionalities:")
        print("1. View Catalog")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Catalog:")
            for product in products_catalog:
                print(f"{product['product_id']}. {product['name']} - {product['price']}")
        elif choice == '2':
            product_id = int(input("Enter product ID to add to cart: "))
            quantity = int(input("Enter quantity: "))
            add_to_cart(product_id, quantity)
        elif choice == '3':
            product_id = int(input("Enter product ID to remove from cart: "))
            remove_from_cart(product_id)
        elif choice == '4':
            print("Your Cart:")
            for item in user_cart:
                product = get_product_by_id(item['product_id'])
                print(f"{product['name']} - Quantity: {item['quantity']}")
        elif choice == '5':
            checkout()
        elif choice == '6':
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_functionalities():
    while True:
        print("\nAdmin Functionalities:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Add Category")
        print("4. Remove Category")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            category_id = input("Enter category ID: ")
            price = float(input("Enter product price: "))
            add_product(product_id, name, category_id, price)
        elif choice == '2':
            product_id = int(input("Enter product ID to remove: "))
            remove_product(product_id)
        elif choice == '3':
            category_id = input("Enter category ID: ")
            category_name = input("Enter category name to add: ")
            add_category(category_id, category_name)
        elif choice == '4':
            category_id = input("Enter category ID to remove: ")
            remove_category(category_id)
        elif choice == '5':
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

# Dummy database for users and admins
users_db = {
    'user1': 'password1',
    'user2': 'password2'
}

admins_db = {
    'admin1': 'adminpassword1'
}

# Sample product catalog
products_catalog = [
    {'product_id': 1, 'name': 'Boots', 'category_id': 'footwear', 'price': 50},
    {'product_id': 2, 'name': 'Coats', 'category_id': 'clothing', 'price': 100},
    {'product_id': 3, 'name': 'Jackets', 'category_id': 'clothing', 'price': 80},
    {'product_id': 4, 'name': 'Caps', 'category_id': 'accessories', 'price': 20}
]

user_cart = []

def add_to_cart(product_id, quantity):
    product = get_product_by_id(product_id)
    if product:
        user_cart.append({'product_id': product_id, 'quantity': quantity})
        print(f"{quantity} {product['name']}(s) added to your cart.")
    else:
        print("Product not found.")

def remove_from_cart(product_id):
    for item in user_cart:
        if item['product_id'] == product_id:
            user_cart.remove(item)
            print("Product removed from your cart.")
            return
    print("Product not found in your cart.")

def get_product_by_id(product_id):
    for product in products_catalog:
        if product['product_id'] == product_id:
            return product
    return None

def add_product(product_id, name, category_id, price):
    products_catalog.append({'product_id': product_id, 'name': name, 'category_id': category_id, 'price': price})
    print(f"Product '{name}' added successfully.")

def remove_product(product_id):
    for product in products_catalog:
        if product['product_id'] == product_id:
            products_catalog.remove(product)
            print(f"Product with ID {product_id} removed successfully.")
            return
    print("Product not found in the catalog.")

def add_category(category_id, category_name):
    # Check if category already exists
    for product in products_catalog:
        if product['category_id'] == category_id:
            print(f"Category '{category_id}' already exists.")
            return
    # Add category to the catalog
    products_catalog.append({'product_id': -1, 'name': category_name, 'category_id': category_id, 'price': 0})
    print(f"Category '{category_name}' added successfully.")

def remove_category(category_id):
    for product in products_catalog:
        if product['category_id'] == category_id:
            products_catalog.remove(product)
    print(f"Category with ID {category_id} removed successfully.")

def checkout():
    print("\nCheckout Options:")
    print("1. Net banking")
    print("2. PayPal")
    print("3. UPI")
    print("4. Back to main menu")

    choice = input("Select payment option: ")

    if choice == '1':
        print("Your order is successfully placed. You will receive payment instructions via email.")
    elif choice == '2':
        print("You will be shortly redirected to the PayPal portal to make a payment.")
    elif choice == '3':
        print("You will be shortly redirected to the portal for Unified Payment Interface to make a payment.")
    elif choice == '4':
        print("Returning to main menu.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
