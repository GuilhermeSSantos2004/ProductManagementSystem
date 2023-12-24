# Product Management System

## Overview
This project is a simple Product Management System implemented in Python using SQLite for data storage. It allows users to perform basic operations such as adding, updating, deleting products, and viewing products that need to be bought.

## Features
1. **Add Product (Option 1):**
   - Users can add a new product to the system by providing details such as barcode, product name, price, amount, and alert level.

2. **Update Product (Option 2):**
   - Users can update the details of an existing product by specifying the barcode. They can change the product name, price, amount, and alert level.

3. **Show Products to Buy (Option 3):**
   - Displays a list of products that need to be bought, i.e., products with the alert level set to 2. Provides information such as product name, barcode, current amount, and price.

4. **Delete Product (Option 4):**
   - Allows users to delete a product from the system by entering the product's barcode.

5. **Exit (Option 5):**
   - Exits the application.

## Implementation Details
- The system uses SQLite as the database to store product information.
- Functions are defined to handle various operations such as adding, updating, deleting, and querying products from the database.
- Input validation is implemented to ensure data integrity and user-friendly interactions.

## How to Run
1. Ensure you have the required Python environment.
2. Run the script (`API.py`) in a Python environment.
3. Follow the on-screen instructions to perform various actions.

## Dependencies
- Python
- SQLite3

## Usage
- This system can be used by small businesses or individuals to manage their product inventory.
- It provides a simple and intuitive command-line interface for users to interact with the system.

## Future Enhancements
- Implement user authentication for secure access to the system.
- Add data validation for user inputs.
- Implement a graphical user interface (GUI) for a more user-friendly experience.
