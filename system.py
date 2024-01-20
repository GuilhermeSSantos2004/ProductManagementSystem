import sqlite3

# import API
import urllib.request
import json
import pprint

db = sqlite3.connect('products.db')
cursor = db.cursor()

def check_numbers():
    barcode = input("Enter the barcode: ")
    if len(barcode) == 13 and barcode.isdigit():
        return barcode
    else:
        print("Please enter a valid 13-digit number.")
        return check_numbers()

def api_barcode(barcode):
    code = barcode
    #7791969016036
    api_key = "ip5fvgl79ztt3yfu3u60jhzio4qh8g"
    url = f"https://api.barcodelookup.com/v3/products?barcode={code}&formatted=y&key=" + api_key


    try:
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())

        barcode = data["products"][0]["barcode_number"]
        #print ("Barcode Number: ", barcode, "\n")
        name = data["products"][0]["title"]
        #print ("Title: ", name, "\n")
        img = data["products"][0]["images"]
        #print ("Link to img: ", img, "\n")
        #print ("Entire Response:")
        #pprint.pprint(data)

        return barcode, name
    except:
        return print("HTTP Error 404: Not Found")

def insert_db(barcode, name, price, amount, amountmin):
    cursor.execute("INSERT INTO product (barcode, name, amountstock, price, amountmin) VALUES (?, ?, ?, ?, ?)", (barcode, name, amount, price, amountmin))
    db.commit()

def update_db(amount, barcode):
    # Obtenha a quantidade atual
    cursor.execute("SELECT amountstock FROM product WHERE barcode = ?", (barcode,))
    current_amount = cursor.fetchone()

    if current_amount is not None:
        current_amount = current_amount[0]  # Extrair o valor do resultado

        # Verifique se a quantidade a ser atualizada é válida
        if current_amount + amount >= 0:
            # Atualize a quantidade no banco de dados
            new_amount = current_amount + amount
            cursor.execute("UPDATE product SET amountstock = ? WHERE barcode = ?", (new_amount, barcode))
            db.commit()
            print("Product updated successfully!")
        else:
            print("Error: Cannot update to a negative amount!")
    else:
        print("Product not found.")

def update_db_fast(barcode):
    # Obtenha a quantidade atual
    cursor.execute("SELECT amountstock FROM product WHERE barcode = ?", (barcode,))
    current_amount = cursor.fetchone()

    if current_amount is not None:
        current_amount = current_amount[0]  # Extrair o valor do resultado

        # Verifique se a quantidade a ser atualizada é válida
        if current_amount - 1 >= 0:
            # Atualize a quantidade no banco de dados
            new_amount = current_amount - 1
            cursor.execute("UPDATE product SET amountstock = ? WHERE barcode = ?", (new_amount, barcode))
            db.commit()
            print("Product updated successfully!")
        else:
            print("Error: Cannot update to a negative amount!")
    else:
        print("Product not found.")

def delete_db(barcode):
    cursor.execute("DELETE FROM product WHERE barcode = ?", (barcode,))
    db.commit()

def select_by_amountmin(amountmin_value):
    cursor.execute("SELECT * FROM product WHERE amountmin = ?", (amountmin_value,))
    rows = cursor.fetchall()
    return rows

def select_all_products():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    return rows

# Seu código principal
while True:
    print("\nChoose an action:")
    print("1. Add product")
    print("2. Update product")
    print("3. Remove fast")
    print("4. Show products to buy")
    print("5. all_products")
    print("6. Delete product")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        barcode = check_numbers()
        code = api_barcode(barcode)
        print("JSON: ", code)

        try:
            name = code[1]
            price = float(input("Price: "))
            amount = int(input("Amount: "))
            amountmin = int(input("Alert: "))
            insert_db(barcode, name, price, amount, amountmin)
            print("Product added successfully!")

        except TypeError as e:
            print(f"TypeError: {e} - 'NoneType' object is not subscriptable.")

    elif choice == '2':
        barcode = check_numbers()
        amount = int(input("New amount: "))
        update_db(amount, barcode)
        print("Product updated successfully!")

    elif choice == '3':
        barcode = check_numbers()
        update_db_fast(barcode)
        print("Product updated successfully!")

    elif choice == '4':
        products_to_buy = select_by_amountmin(2)
        print("Products to Buy:", products_to_buy)
        if products_to_buy:
            print("\nProducts to Buy:")
            for product in products_to_buy:
                barcode, name, amountstock, amountmin, price, *additional_columns = product
                print(f"Product: {name} (Barcode: {barcode})\n"
                      f"  Current Amount: {amountstock}\n"
                      f"  Price: ${price}\n"
                      f"  ---------------")
            print("Happy Shopping!")
        else:
            print("No products found to buy.")

    elif choice == '5':
        all_products = select_all_products()
        print("All Products:", all_products)
        if all_products:
            print("\nAll Products in Stock:")
            for product in all_products:
                barcode, name, amountstock, amountmin, price, *additional_columns = product
                print(f"Product: {name} (Barcode: {barcode})\n"
                      f"  Current Amount: {amountstock}\n"
                      f"  Price: ${price}\n"
                      f"  ---------------")
            print("Listed all products.")
        else:
            print("No products found.")

    elif choice == '6':
        barcode = check_numbers()
        delete_db(barcode)
        print("Product deleted successfully!")

    elif choice == '7':
        print("Exiting the application.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")


