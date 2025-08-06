import csv
from datetime import datetime
import os

# Define the CSV file path
FILE_NAME = 'expenses.csv'

# Create the file and headers if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Amount', 'Category', 'Description'])

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter amount spent: ₹"))
        category = input("Enter category (e.g., Food, Travel, Bills): ").strip()
        description = input("Enter a short description: ").strip()
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Append to CSV
        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date_time, amount, category, description])

        print("✅ Expense logged successfully.")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

# Main loop
def main():
    while True:
        print("\n1. Add Expense")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            print("👋 Exiting. Your expenses are saved in 'expenses.csv'.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == '__main__':
    main()
