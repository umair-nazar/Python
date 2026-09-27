import tkinter as tk
from tkinter import messagebox, ttk


def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * (tax_rate / 100)


def calculate_net_salary(gross_salary, tax_amount):
    return gross_salary - tax_amount


def build_app():
    root = tk.Tk()
    root.title("Employee Salary Calculator")
    root.geometry("720x460")
    root.minsize(640, 420)
    root.configure(bg="#f5f7f8")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("App.TFrame", background="#f5f7f8")
    style.configure("Title.TLabel", background="#f5f7f8", foreground="#1f2d3d", font=("Segoe UI", 20, "bold"))
    style.configure("Body.TLabel", background="#f5f7f8", foreground="#334155", font=("Segoe UI", 10))
    style.configure("Card.TFrame", background="#ffffff", relief="flat")
    style.configure("CardTitle.TLabel", background="#ffffff", foreground="#0f766e", font=("Segoe UI", 13, "bold"))
    style.configure("Field.TLabel", background="#ffffff", foreground="#334155", font=("Segoe UI", 10))
    style.configure("Result.TLabel", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 11, "bold"))
    style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), padding=(12, 8))

    main = ttk.Frame(root, style="App.TFrame", padding=24)
    main.pack(fill="both", expand=True)

    ttk.Label(main, text="Employee Salary Calculator", style="Title.TLabel").pack(anchor="w")
    ttk.Label(main, text="Enter the employee details and calculate gross, tax, and net salary.", style="Body.TLabel").pack(anchor="w", pady=(4, 18))

    content = ttk.Frame(main, style="App.TFrame")
    content.pack(fill="both", expand=True)

    form_card = ttk.Frame(content, style="Card.TFrame", padding=18)
    form_card.pack(side="left", fill="both", expand=True, padx=(0, 12))

    result_card = ttk.Frame(content, style="Card.TFrame", padding=18)
    result_card.pack(side="right", fill="both", expand=True, padx=(12, 0))

    ttk.Label(form_card, text="Employee Details", style="CardTitle.TLabel").pack(anchor="w", pady=(0, 12))

    employee_name_var = tk.StringVar()
    basic_salary_var = tk.StringVar()
    allowance_var = tk.StringVar()
    tax_rate_var = tk.StringVar()

    def add_field(parent, label_text, variable):
        field_frame = ttk.Frame(parent, style="Card.TFrame")
        field_frame.pack(fill="x", pady=7)
        ttk.Label(field_frame, text=label_text, style="Field.TLabel").pack(anchor="w")
        entry = ttk.Entry(field_frame, textvariable=variable)
        entry.pack(fill="x", pady=(4, 0))
        return entry

    add_field(form_card, "Employee name", employee_name_var)
    add_field(form_card, "Basic salary", basic_salary_var)
    add_field(form_card, "Allowance", allowance_var)
    add_field(form_card, "Tax rate (%)", tax_rate_var)

    result_title = ttk.Label(result_card, text="Results", style="CardTitle.TLabel")
    result_title.pack(anchor="w", pady=(0, 12))

    gross_result_var = tk.StringVar(value="Gross Salary: -")
    tax_result_var = tk.StringVar(value="Tax Amount: -")
    net_result_var = tk.StringVar(value="Net Salary: -")

    ttk.Label(result_card, textvariable=gross_result_var, style="Result.TLabel").pack(anchor="w", pady=8)
    ttk.Label(result_card, textvariable=tax_result_var, style="Result.TLabel").pack(anchor="w", pady=8)
    ttk.Label(result_card, textvariable=net_result_var, style="Result.TLabel").pack(anchor="w", pady=8)

    def calculate():
        try:
            employee_name = employee_name_var.get().strip()
            basic_salary = float(basic_salary_var.get())
            allowance = float(allowance_var.get())
            tax_rate = float(tax_rate_var.get())

            if not employee_name:
                raise ValueError("Employee name is required.")
            if basic_salary < 0 or allowance < 0 or tax_rate < 0:
                raise ValueError("All numeric values must be zero or greater.")

            gross_salary = calculate_gross_salary(basic_salary, allowance)
            tax_amount = calculate_tax(gross_salary, tax_rate)
            net_salary = calculate_net_salary(gross_salary, tax_amount)

            gross_result_var.set(f"Gross Salary: {gross_salary:.2f}")
            tax_result_var.set(f"Tax Amount: {tax_amount:.2f}")
            net_result_var.set(f"Net Salary: {net_salary:.2f}")
        except ValueError as error:
            messagebox.showerror("Invalid input", str(error))

    button_row = ttk.Frame(form_card, style="Card.TFrame")
    button_row.pack(fill="x", pady=(18, 0))
    ttk.Button(button_row, text="Calculate", style="Accent.TButton", command=calculate).pack(side="left")

    def clear_form():
        employee_name_var.set("")
        basic_salary_var.set("")
        allowance_var.set("")
        tax_rate_var.set("")
        gross_result_var.set("Gross Salary: -")
        tax_result_var.set("Tax Amount: -")
        net_result_var.set("Net Salary: -")

    ttk.Button(button_row, text="Clear", command=clear_form).pack(side="left", padx=10)

    return root


def main():
    app = build_app()
    app.mainloop()


if __name__ == "__main__":
    main()