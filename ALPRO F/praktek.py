import tkinter as tk

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Shop POS")

        # Create menu categories
        self.categories = ["Espresso based", "Manual Coffee", "Non Coffee", "Tea Based", "Sweet Treats", "Meals"]
        self.category_buttons = []

        # Create menu buttons
        for i, category in enumerate(self.categories):
            button = tk.Button(self.root, text=category, command=lambda c=category: self.select_category(c))
            button.grid(row=i, column=0)
            self.category_buttons.append(button)

        # Create "OPEN TICKET" and "BAYAR" buttons
        self.open_ticket_button = tk.Button(self.root, text="OPEN TICKET", command=self.open_ticket)
        self.open_ticket_button.grid(row=len(self.categories), column=0)

        self.bayar_button = tk.Button(self.root, text="BAYAR", command=self.bayar)
        self.bayar_button.grid(row=len(self.categories) + 1, column=0)


class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Shop POS")

        # Create menu categories and their items
        self.menu_items = {
            "Espresso based": [
                "Espresso",
                "Americano",
                "Cappuccino",
                "Cafe Latte",
                "Caramel Latte",
                "Vanilla Latte",
                "Hazelnut Latte",
                "Mocha"
            ],
            "Manual Coffee": [
                "V60",
                "Vietnam Drip",
                "Cold Brew",
                "Japanese Coffee",
                "French Press"
            ],
            "Non Coffee": [
                "Hot Chocolate",
                "Chocolate Milk",
                "Fresh Milk",
                "Matcha Latte"
            ],
            "Tea Based": [
                "Green Tea",
                "Black Tea",
                "Earl Grey",
                "Lemon Tea",
                "Thai Tea"
            ],
            "Sweet Treats": [
                "Ice Cream",
                "Brownies",
                "Cookies",
                "Pudding"
            ],
            "Meals": [
                "Nasi Goreng",
                "Mie Goreng",
                "Chicken Rice",
                "Beef Steak"
            ],
        }

        # Create frames for layout
        self.category_frame = tk.Frame(self.root)
        self.category_frame.grid(row=0, column=0, sticky="ns")
        
        self.items_frame = tk.Frame(self.root)
        self.items_frame.grid(row=0, column=1, sticky="nsew")

        # Create category buttons
        for i, category in enumerate(self.menu_items.keys()):
            button = tk.Button(self.category_frame, text=category, 
                             command=lambda c=category: self.select_category(c),
                             width=20)
            button.grid(row=i, column=0, pady=2)

        # Create "OPEN TICKET" and "BAYAR" buttons
        self.open_ticket_button = tk.Button(self.category_frame, text="OPEN TICKET", 
                                          command=self.open_ticket, width=20)
        self.open_ticket_button.grid(row=len(self.menu_items), column=0, pady=2)

        self.bayar_button = tk.Button(self.category_frame, text="BAYAR", 
                                    command=self.bayar, width=20)
        self.bayar_button.grid(row=len(self.menu_items) + 1, column=0, pady=2)

    def select_category(self, category):
        # Clear previous items
        for widget in self.items_frame.winfo_children():
            widget.destroy()

        # Display items for selected category
        for i, item in enumerate(self.menu_items[category]):
            button = tk.Button(self.items_frame, text=item, 
                             command=lambda x=item: self.select_item(x),
                             width=20)
            button.grid(row=i//3, column=i%3, padx=5, pady=5)

    def select_item(self, item):
        # Implement logic when an item is selected
        print(f"Selected item: {item}")

    def open_ticket(self):
        # Implement logic to open ticket
        print("Opening ticket...")

    def bayar(self):
        # Implement logic to process payment
        print("Processing payment...")


if __name__ == "__main__":
    root = tk.Tk()
    pos = POS(root)
    root.mainloop()