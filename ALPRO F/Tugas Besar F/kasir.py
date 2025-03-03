import tkinter as tk
from tkinter import messagebox
from menu_data import menu_items

class POS:
    def __init__(self, root):
        self.root = root
        self.root.title("Kedai Kopi TAPOPS")
        self.root.attributes('-fullscreen', False)  # Set fullscreen mode
        self.root.configure(bg="#f5f5f5")

        # Inisialisasi keranjang dan total
        self.cart = []
        self.total = 0

        # Buat frame
        self.category_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.category_frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        self.items_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.items_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.cart_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.cart_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        # Buat tombol kategori
        for i, category in enumerate(menu_items.keys()):
            button = tk.Button(self.category_frame, text=category, 
                             command=lambda c=category: self.select_category(c),
                             width=20, height=3, bg="#4CAF50", fg="white", font=("Arial", 16))
            button.grid(row=i, column=0, sticky="ew", pady=5)

        # Buat tampilan keranjang
        self.cart_label = tk.Label(self.cart_frame, text="Shopping Cart", bg="#f5f5f5", font=("Arial", 24))
        self.cart_label.pack()

        self.cart_listbox = tk.Listbox(self.cart_frame, width=40, height=20, font=("Arial", 14))
        self.cart_listbox.pack(pady=5)

        self.total_label = tk.Label(self.cart_frame, text="Total: Rp 0", bg="#f5f5f5", font=("Arial", 18))
        self.total_label.pack()

        # Buat tombol kontrol
        self.remove_item_button = tk.Button(self.cart_frame, text="Hapus Pilihan", 
                                          command=self.remove_from_cart, bg="#f44336", fg="white", font=("Arial", 16))
        self.remove_item_button.pack(fill=tk.X, pady=5)

        self.clear_cart_button = tk.Button(self.cart_frame, text="Clear Cart", 
                                         command=self.clear_cart, bg="#ff9800", fg="white", font=("Arial", 16))
        self.clear_cart_button.pack(fill=tk.X, pady=5)

        self.pay_button = tk.Button(self.cart_frame, text="Bayar", 
                                  command=self.process_payment, bg="#2196F3", fg="white", font=("Arial", 16))
        self.pay_button.pack(fill=tk.X, pady=5)

        # Configure grid weights for responsive design
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)
        self.root.grid_columnconfigure(2, weight=1)

    def select_category(self, category):
        # Hapus item sebelumnya
        for widget in self.items_frame.winfo_children():
            widget.destroy()

        # Tampilkan item untuk kategori yang dipilih
        for i, (item, price) in enumerate(menu_items[category].items()):
            button_text = f"{item}\nRp {price:,}"
            button = tk.Button(self.items_frame, text=button_text, 
                             command=lambda x=item, p=price : self.add_to_cart(x, p),
                             width=20, height=3, bg="#2196F3", fg="white", font=("Arial", 14))
            button.grid(row=i//3, column=i%3, padx=5, pady=5, sticky="ew")

    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        self.cart_listbox.insert(tk.END, f"{item} - Rp {price:,}")
        self.total += price
        self.total_label.config(text=f" Total: Rp {self.total:,}")

    def remove_from_cart(self):
        try:
            index = self.cart_listbox.curselection()[0]
            item, price = self.cart.pop(index)
            self.cart_listbox.delete(index)
            self.total -= price
            self.total_label.config(text=f"Total: Rp {self.total:,}")
        except IndexError:
            messagebox.showerror("Error", "Pilih item yang ingin dihapus!")

    def clear_cart(self):
        self.cart = []
        self.cart_listbox.delete(0, tk.END)
        self.total = 0
        self.total_label.config(text="Total: Rp 0")

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
        
        tk.Label(payment_window, text="Jumlah Uang:").pack()
        payment_entry = tk.Entry(payment_window)
        payment_entry.pack()
        
        ipor=tk.Button(payment_window,text="KONFIRMASI PEMBAYARAN",command=self)
        ipor.pack()
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = POS(root)
    root.mainloop()