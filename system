import sqlite3

db = sqlite3.connect('products.db')
cursor = db.cursor()

def check_numbers():
    barcode = input("Enter the barcode: ")
    if len(barcode) == 13 and barcode.isdigit():
        return barcode
    else:
        print("Please enter a valid 13-digit number.")
        return check_numbers()

def insert_db(barcode, name, price, amount, amountmin):
    cursor.execute("INSERT INTO product (barcode, name, amountstock, price, amountmin) VALUES (?, ?, ?, ?, ?)", (barcode, name, amount, price, amountmin))
    db.commit()

def update_db(barcode, name, price, amount, amountmin):
    cursor.execute("UPDATE product SET barcode = ?, amountmin = ?, name = ?, price = ?, amount = ? WHERE barcode = ?",
                   (barcode, amountmin, name, price, amount, barcode))
    db.commit()

def delete_db(barcode):
    cursor.execute("DELETE FROM product WHERE barcode = ?", (barcode,))
    db.commit()

def select_by_amountmin(amountmin_value):
    cursor.execute("SELECT * FROM product WHERE amountmin = ?", (amountmin_value,))
    rows = cursor.fetchall()
    return rows

while True:
    print("\nChoose an action:")
    print("1. Add product")
    print("2. Update product")
    print("3. Show products to buy")
    print("4. Delete product")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        barcode = check_numbers()
        name = input("Product name: ")
        price = float(input("Price: "))
        amount = int(input("Amount: "))
        amountmin = int(input("Alert: "))
        insert_db(barcode, name, price, amount, amountmin)
        print("Product added successfully!")
    elif choice == '2':
        barcode = check_numbers()
        name = input("New product name: ")
        price = float(input("New price: "))
        amount = int(input("New amount: "))
        amountmin = int(input("New alert: "))
        update_db(barcode, name, price, amount, amountmin)
        print("Product updated successfully!")
    elif choice == '3':
        products_to_buy = select_by_amountmin(2)
        if products_to_buy:
            print("\nProducts to Buy:")
            for product in products_to_buy:
                barcode, name, amountstock, price, amountmin, *additional_columns = product
                print(f"Product: {name} (Barcode: {barcode})\n"
                      f"  Current Amount: {amountstock}\n"
                      f"  Price: ${price}\n"
                      f"  ---------------")
            print("Happy Shopping!")
        else:
            print("No products found to buy.")
    elif choice == '4':
        barcode = check_numbers()
        delete_db(barcode)
        print("Product deleted successfully!")
    elif choice == '5':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
