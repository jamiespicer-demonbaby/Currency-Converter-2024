import tkinter as tk
from tkinter import ttk


class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        # Set style for color scheme
        style = ttk.Style()
        style.configure('TFrame', background='#FFFFFF', font=('Trajan Pro', 12))
        style.configure('TLabel', background='#FFFFFF', font=('Trajan Pro', 12))
        style.configure('TButton', background='#FFFFFF', font=('Trajan Pro', 15, "bold"))

        # Conversion rates (maybe later replace with an external library with the)
        self.rates = {'USD': 1, 'CAD': 1.25, 'NZD': 1.38}

        # Variables
        self.from_currency = tk.StringVar(value='USD')
        self.to_currency = tk.StringVar(value='USD')
        self.amount = tk.DoubleVar()

        # GUI Components
        frame = ttk.Frame(master, padding=(20, 10))
        frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(frame, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(frame, textvariable=self.amount).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(frame, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
        from_currency_combobox = ttk.Combobox(frame, textvariable=self.from_currency, values=list(self.rates.keys()))
        from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
        to_currency_combobox = ttk.Combobox(frame, textvariable=self.to_currency, values=list(self.rates.keys()))
        to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(frame, text="Convert").grid(row=3, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
