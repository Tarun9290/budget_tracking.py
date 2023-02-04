#Budget tracking app-
#Create a simple app for tracking your personal or business finances.

import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect("budget.db")
cursor = conn.cursor()

# Create the expenses table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
)
""")

# Function to add an expense
def add_expense(category, amount, date):
    cursor.execute("""
    INSERT INTO expenses (category, amount, date)
    VALUES (?, ?, ?)
    """, (category, amount, date))
    conn.commit()

# Function to view all expenses
def view_expenses():
    cursor.execute("""
    SELECT * FROM expenses
    """)
    return cursor.fetchall()

# Function to delete an expense
def delete_expense(expense_id):
    cursor.execute("""
    DELETE FROM expenses
    WHERE id=?
    """, (expense_id,))
    conn.commit()

# Example usage
add_expense("Food", 20.0, "2022-01-01")
add_expense("Transportation", 30.0, "2022-01-02")
print(view_expenses())
delete_expense(1)
print(view_expenses())

# Close the database connection
conn.close()


#This code uses SQLite as a database to store expenses with categories, amounts, and dates. It has functions for adding expenses, viewing all expenses, and deleting expenses.

#You can build upon this code to add more features and functionality to your budget tracking app, such as handling income, generating reports, or adding user authentication.




