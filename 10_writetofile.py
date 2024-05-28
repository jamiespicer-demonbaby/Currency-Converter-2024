import tkinter as tk
from tkinter import ttk, messagebox
import re


class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        # Set style for green and white color scheme
        style = ttk.Style()
        style.configure('TFrame', background='#D1E2D2', font=('Trajan Pro', 12))  # Light green
        style.configure('TLabel', background='#D1E2D2', font=('Trajan Pro', 12))  # Light green
        style.configure('TButton', background='#4CAF50', font=('Trajan Pro', 12, "bold"))  # Green background

        # Conversion rates (replace with real-time rates)
        self.rates = {'USD': 1, 'CAD': 1.25, 'NZD': 1.38}

        # Variables
        self.from_currency = tk.StringVar(value='USD')
        self.to_currency = tk.StringVar(value='USD')
        self.amount = tk.StringVar()

        # History list
        self.history = []

        # GUI Components
        self.create_main_tab()

    def create_main_tab(self):
        frame = ttk.Frame(self.master, padding=(20, 10))
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Header
        ttk.Label(frame, text=" CURRENCY CONVERTER ", font=('Trajan Pro', 16, 'bold')).grid(row=0, column=0,
                                                                                            columnspan=3, padx=10,
                                                                                            pady=10)

        ttk.Label(frame, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(frame, textvariable=self.amount).grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(frame, text="From Currency:").grid(row=2, column=0, padx=10, pady=10)
        from_currency_combobox = ttk.Combobox(frame, textvariable=self.from_currency, values=list(self.rates.keys()))
        from_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(frame, text="To Currency:").grid(row=3, column=0, padx=10, pady=10)
        to_currency_combobox = ttk.Combobox(frame, textvariable=self.to_currency, values=list(self.rates.keys()))
        to_currency_combobox.grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(frame, text="Convert", command=self.validate_and_convert).grid(row=4, column=0, columnspan=2, pady=10)

        ttk.Button(frame, text="Help", command=self.show_help).grid(row=5, column=0, pady=10)
        ttk.Button(frame, text="History", command=self.open_history_tab).grid(row=5, column=1, pady=10)

    def create_history_tab(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("CONVERSION HISTORY")
        history_window.configure(bg='white')  # White background

        history_frame = ttk.Frame(history_window, padding=(20, 10), style='TFrame')
        history_frame.pack()

        history_label = ttk.Label(history_frame, text="CONVERSION HISTORY:", font=('Trajan Pro', 16, 'bold'),
                                  style='TLabel')
        history_label.grid(row=0, column=0, columnspan=2, pady=10)

        history_listbox = tk.Listbox(history_frame, width=50, font=('Trajan Pro', 12), bg='white')
        history_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        for item in self.history:
            history_listbox.insert(tk.END, item)

        # Add "Write to File" button
        ttk.Button(history_frame, text="Write to File", command=self.write_to_file).grid(row=2, column=0, columnspan=2, pady=10)

    def write_to_file(self):
        try:
            with open("conversion_history.txt", "w") as file:
                file.write("Conversion History:\n")
                for item in self.history:
                    file.write(item + '\n')
            messagebox.showinfo("Success", "Conversion history written to file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def validate_and_convert(self):
        try:
            amount = self.amount.get()
            if not amount:
                raise ValueError("Please enter a value for conversion.")
            if not re.match(r'^-?\d+(?:\.\d+)?$', amount):
                raise ValueError("Please enter a valid number for the amount.")
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Please enter a value greater than 0 for conversion.")

            from_currency = self.from_currency.get()
            to_currency = self.to_currency.get()

            if from_currency == to_currency:
                raise ValueError("Please select different currencies for conversion.")

            result = amount * (self.rates[to_currency] / self.rates[from_currency])

            result_str = f"{amount} {from_currency} = {result:.2f} {to_currency}"
            messagebox.showinfo("Result", result_str)

            # Add to history
            self.history.append(result_str)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def show_help(self):
        help_text = "This is a simple currency converter.\n\n" \
                    "Enter the amount, select the 'From' and 'To' currencies from the dropdowns, " \
                    "and click 'Convert' to see the result."

        messagebox.showinfo("Help", help_text)

    def open_history_tab(self):
        self.create_history_tab()


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
