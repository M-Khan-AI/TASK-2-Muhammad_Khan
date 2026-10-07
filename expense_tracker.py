total = 0

while True:
    expense = input("Enter expense (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    if expense.strip() == "":
        print("Please enter an expense amount.")
        continue

    total += float(expense)

print("Total Spent:", total)