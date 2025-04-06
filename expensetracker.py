#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD) or leave empty for today: ") or datetime.today().strftime('%Y-%m-%d')

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    print("✅ Expense added!\n")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    total = 0
    print("\n--- All Expenses ---")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} - ₹{row[1]} - {row[2]}")
            total += float(row[1])
    print(f"\n💰 Total Spent: ₹{total:.2f}\n")

def filter_by_category():
    category = input("Enter category to filter: ")
    found = False
    total = 0

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2].lower() == category.lower():
                print(f"{row[0]} - ₹{row[1]}")
                total += float(row[1])
                found = True

    if found:
        print(f"\nTotal spent in '{category}': ₹{total:.2f}\n")
    else:
        print("No expenses in this category.\n")

def main():
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()


# In[ ]:


import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD) or leave empty for today: ") or datetime.today().strftime('%Y-%m-%d')

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    print("✅ Expense added!\n")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found.")
        return

    total = 0
    print("\n--- All Expenses ---")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} - ₹{row[1]} - {row[2]}")
            total += float(row[1])
    print(f"\n💰 Total Spent: ₹{total:.2f}\n")

def filter_by_category():
    category = input("Enter category to filter: ")
    found = False
    total = 0

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2].lower() == category.lower():
                print(f"{row[0]} - ₹{row[1]}")
                total += float(row[1])
                found = True

    if found:
        print(f"\nTotal spent in '{category}': ₹{total:.2f}\n")
    else:
        print("No expenses in this category.\n")

def main():
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()

    


# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Example training data
descriptions = ["Starbucks coffee", "Uber ride", "Electric bill", "Netflix subscription"]
categories = ["Food", "Travel", "Utilities", "Entertainment"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(descriptions)

model = MultinomialNB()
model.fit(X, categories)

# Predict category
desc = ["Pizza Hut"]
desc_vector = vectorizer.transform(desc)
predicted_category = model.predict(desc_vector)[0]

print(predicted_category)  # Output: "Food"


# In[ ]:


give me a 

