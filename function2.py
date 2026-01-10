
def display_invoice(username, amout, due_date):
    print(f"hello {username}")
    print(f"your bill of ${amout:.2f} is due: {due_date}")

display_invoice("kanika", 42.50, "10/01/2026")