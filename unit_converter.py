
import tkinter as tk
from tkinter import ttk, messagebox

def convert():
    try:
        value = float(entry_value.get())
        category = category_cb.get()
        from_unit = from_cb.get()
        to_unit = to_cb.get()

        if category == "Length":
            conversions = {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000}
        elif category == "Weight":
            conversions = {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274}
        elif category == "Time":
            conversions = {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400}
        elif category == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            else:
                result = value
            result_label.config(text=f"Result: {result:.2f} {to_unit}")
            return
        else:
            messagebox.showerror("Error", "Select valid category")
            return

        result = value * (conversions[to_unit] / conversions[from_unit])
        result_label.config(text=f"Result: {result:.2f} {to_unit}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def update_units(event):
    category = category_cb.get()
    if category == "Length":
        units = ["Meter", "Kilometer", "Centimeter", "Millimeter"]
    elif category == "Weight":
        units = ["Kilogram", "Gram", "Pound", "Ounce"]
    elif category == "Time":
        units = ["Second", "Minute", "Hour", "Day"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    else:
        units = []
    
    from_cb["values"] = units
    to_cb["values"] = units
    from_cb.current(0)
    to_cb.current(1)


root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")

tk.Label(root, text="Enter Value:").pack()
entry_value = tk.Entry(root)
entry_value.pack()

tk.Label(root, text="Category:").pack()
category_cb = ttk.Combobox(root, values=["Length", "Weight", "Time", "Temperature"])
category_cb.pack()
category_cb.bind("<<ComboboxSelected>>", update_units)

tk.Label(root, text="From Unit:").pack()
from_cb = ttk.Combobox(root)
from_cb.pack()

tk.Label(root, text="To Unit:").pack()
to_cb = ttk.Combobox(root)
to_cb.pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)
result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
