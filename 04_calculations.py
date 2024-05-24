import tkinter as tk
from tkinter import ttk, messagebox


class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        # Set style for white color scheme
        style = ttk.Style()
        style.configure('TFrame', background='#FFFFFF', font=('Trajan Pro', 12))
        style.configure('TLabel', background='#FFFFFF', font=('Trajan Pro', 12))
        style.configure('TButton', background='#FFFFFF', font=('Trajan Pro', 15, "bold"))

        # Conversion rates (replace with real-time rates)
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

        ttk.Button(frame, text="Convert", command=self.convert).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(frame, text="Help", command=self.show_help).grid(row=4, column=0, columnspan=2, pady=10)

    def convert(self):
        amount = float(self.amount.get())
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()

        result = amount * (self.rates[to_currency] / self.rates[from_currency])

        result_str = f"{amount} {from_currency} = {result:.2f} {to_currency}"
        messagebox.showinfo("Result", result_str)

    def show_help(self):
        help_text = "This is a currency converter.\n\n" \
                    "Enter the amount desired, select the 'From' and 'To' currencies from the dropdowns, " \
                    "and press 'Convert' to see the result."

        messagebox.showinfo("Help", help_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
