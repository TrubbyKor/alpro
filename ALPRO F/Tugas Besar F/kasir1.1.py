import tkinter as tk
from tkinter import ttk, messagebox
from menu_data import menu_items

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Kedai Kopi TAPOPS")
        self.root.attributes('-fullscreen', False)  # Set fullscreen mode
        self.root.configure(bg="#f5f5f5")
    

        # Create menu categories and their items with prices
        self.menu_items = menu_items

        # Initialize cart and total
        self.cart = []
        self.total = 0

        # Create main frames
        self.category_frame = tk.Frame(self.root,bg="#f5f5f5")
        self.category_frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        self.items_frame = tk.Frame(self.root,bg="#f5f5f5")
        self.items_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        self.cart_frame = tk.Frame(self.root,bg="#f5f5f5")
        self.cart_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        # Create category buttons
        for i, category in enumerate(self.menu_items.keys()):
            button = tk.Button(self.category_frame, text=category, 
                             command=lambda c=category: self.select_category(c),
                            width=20,bg="#4CAF50", fg="white", font=("Arial", 16))
            button.grid(row=i, column=0, sticky="ew", pady=5)

        # Create cart display
        self.cart_label = tk.Label(self.cart_frame, text="Shopping Cart", bg="#f5f5f5", font=("Arial", 24))
        self.cart_label.pack()

        self.cart_listbox = tk.Listbox(self.cart_frame, width=40, height=20,font=("Arial", 14))
        self.cart_listbox.pack(pady=5)

        self.total_label = tk.Label(self.cart_frame, text="Total: Rp 0",bg="#f5f5f5", font=("Arial", 18))
        self.total_label.pack()

        # Create control buttons
        self.remove_item_button = tk.Button(self.cart_frame, text="Hapus Pilihan", 
                                          command=self.remove_from_cart, bg="#f44336", fg="white", font=("Arial", 16))
        self.remove_item_button.pack(pady=5)

        self.clear_cart_button = tk.Button(self.cart_frame, text="Clear Cart", 
                                         command=self.clear_cart, bg="#ff9800", fg="white", font=("Arial", 16))
        self.clear_cart_button.pack(pady=5)

        self.pay_button = tk.Button(self.cart_frame, text="Bayar", 
                                  command=self.process_payment, bg="#2196F3", fg="white", font=("Arial", 16))
        self.pay_button.pack(pady=5)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        self.root.grid_columnconfigure(2, weight=1)

    def select_category(self, category):
        # Clear previous items
        for widget in self.items_frame.winfo_children():
            widget.destroy()

        # Display items for selected category
        for i, (item, price) in enumerate(self.menu_items[category].items()):
            button_text = f"{item}\nRp {price:,}"
            button = tk.Button(self.items_frame, text=button_text, 
                             command=lambda x=item, p=price: self.add_to_cart(x, p),
                             width=20, height=3,bg="#2196F3", fg="white", font=("Arial", 14))
            button.grid(row=i//3, column=i%3, padx=5, pady=5,sticky="ew")

    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        self.cart_listbox.insert(tk.END, f"{item} - Rp {price:,}")
        self.total += price
        self.update_total()

    def remove_from_cart(self):
        try:
            selection = self.cart_listbox.curselection()
            if selection:
                index = selection[0]
                removed_item = self.cart.pop(index)
                self.cart_listbox.delete(index)
                self.total -= removed_item[1]
                self.update_total()
        except IndexError:
            messagebox.showerror("Error", "Pilih Menu Yang Akan Di Hapus")

    def clear_cart(self):
        self.cart = []
        self.cart_listbox.delete(0, tk.END)
        self.total = 0
        self.update_total()

    def update_total(self):
        self.total_label.config(text=f"Total: Rp {self.total:,}")

    def process_payment(self):
        if not self.cart:
            messagebox.showerror("Error", "Cart is empty")
            return

        # Create payment window
        payment_window = tk.Toplevel(self.root)
        payment_window.title("Pembayaran")
        
        # Payment amount entry
        tk.Label(payment_window, text="Total Harga:").pack()
        tk.Label(payment_window, text=f"Rp {self.total:,}").pack()
        
        tk.Label(payment_window, text="Jumlah Pembayaran:").pack()
        payment_entry = tk.Entry(payment_window)
        payment_entry.pack()

        def confirm_payment():
            try:
                payment = int(payment_entry.get())
                if payment < self.total:
                    messagebox.showerror("Error", "Jumlah pembayaran tidak mencukupi")
                    return
                
                change = payment- self.total
                messagebox.showinfo("Success", 
                                  f"Pembayaran Berhasil!\nKembalian: Rp {change:,}")
                payment_window.destroy()
                self.clear_cart()
            except ValueError:
                messagebox.showerror("Error", "Silakan masukkan jumlah yang valid")

        tk.Button(payment_window, text="Konfirmasi Pembayaran", 
                 command=confirm_payment).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    pos = POS(root)
    root.mainloop()