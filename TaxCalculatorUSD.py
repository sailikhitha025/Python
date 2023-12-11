import tkinter as tk
from tkinter import ttk

def calculate_tax():
    try:
        age = int(age_entry.get())
        salary_bruto_y = float(salary_entry.get())
        
        if age < 0 or salary_bruto_y < 0:
            raise ValueError("Age and salary must be non-negative numbers.")

        rebate = 16425
        if age >= 65:
            rebate += 9000
        if age >= 75:
            rebate += 2997

        time_frame = time_frame_var.get()
        if time_frame == 'Monthly':
            salary_bruto_y *= 12

        tax_y = 0
        tax_bracket = 'n/n'

        brackets = [
            (1731601, 45),
            (817601, 41),
            (641401, 39),
            (488701, 36),
            (353101, 31),
            (226001, 26),
            (1, 18),
        ]

        for bracket, rate in brackets:
            if salary_bruto_y >= bracket:
                bracket_amount = salary_bruto_y - bracket
                bracket_tax = bracket_amount * (rate / 100)
                tax_y += bracket_tax
                salary_bruto_y -= bracket_amount
                if tax_bracket == 'n/n':
                    tax_bracket = str(rate)
                tax_output.insert(tk.END, f'Tax amount for {rate}% bracket: USD{bracket_tax:.2f}\n')

        tax_y -= rebate
        if tax_y < 0:
            tax_y = 0

        salary_bruto_m = salary_bruto_y / 12
        tax_m = tax_y / 12
        salary_net_y = salary_bruto_y - tax_y
        salary_net_m = salary_bruto_m - tax_m
        tax_perc = (tax_y / (salary_bruto_y + 0.0001)) * 100

        result_text = (
            
            f'Your yearly income tax\t\t\t\tUSD{tax_y:.2f}\n'
            f'Your net income after tax is\t\t\tUSD{salary_net_y:.2f} yearly\n\n'
            f'Your monthly income before tax is\t\tUSD{salary_bruto_m:.2f}\n'
            f'Your monthly income tax is\t\t\tUSD{tax_m:.2f}\n'
            f'Your net monthly income after tax is\t\tUSD{salary_net_m:.2f} monthly\n\n'
            f'Your tax bracket:\t\t\t\t{tax_bracket}%\n'
            f'The tax you pay is equal to:\t\t\t{tax_perc:.2f}%\n'
        )

        result_label.config(text=result_text)

    except ValueError as e:
        result_label.config(text=str(e))
    except Exception as e:
        result_label.config(text="An unexpected error occurred.")

def reset_fields():
    age_entry.delete(0, tk.END)
    time_frame_combobox.set("Annually")
    salary_entry.delete(0, tk.END)
    tax_output.delete(1.0, tk.END)
    result_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("Income Tax Calculator")

# Style
style = ttk.Style()
style.configure("TFrame", background="#ececec")
style.configure("TLabel", background="#ececec", font=("Arial", 11))
style.configure("TButton", background="#4caf50", foreground="white", font=("Arial", 11))
style.configure("TEntry", font=("Arial", 11))
style.configure("TText", font=("Arial", 10))

# Create and place widgets
main_frame = ttk.Frame(window, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

age_label = ttk.Label(main_frame, text="Enter your age:")
age_label.grid(row=0, column=0, pady=10, sticky=tk.W)
age_entry = ttk.Entry(main_frame)
age_entry.grid(row=0, column=1, pady=10, sticky=tk.W)

time_frame_label = ttk.Label(main_frame, text="Select time frame:")
time_frame_label.grid(row=1, column=0, pady=10, sticky=tk.W)
time_frame_var = tk.StringVar()
time_frame_combobox = ttk.Combobox(main_frame, textvariable=time_frame_var, values=["Annually", "Monthly"])
time_frame_combobox.grid(row=1, column=1, pady=10, sticky=tk.W)
time_frame_combobox.current(0)

salary_label = ttk.Label(main_frame, text="Enter your salary (USD):")
salary_label.grid(row=2, column=0, pady=10, sticky=tk.W)
salary_entry = ttk.Entry(main_frame)
salary_entry.grid(row=2, column=1, pady=10, sticky=tk.W)

calculate_button = ttk.Button(main_frame, text="Calculate", command=calculate_tax)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

reset_button = ttk.Button(main_frame, text="Reset", command=reset_fields)
reset_button.grid(row=3, column=1, columnspan=2, pady=20, sticky=tk.E)

tax_output = tk.Text(main_frame, height=8, width=40)
tax_output.grid(row=4, column=0, columnspan=2, pady=10)

result_label = ttk.Label(main_frame, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the GUI event loop
window.mainloop()
