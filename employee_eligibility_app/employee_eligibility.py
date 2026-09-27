from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk


@dataclass
class Employee:
    is_active: bool
    months_employed: int
    performance_rating: float
    has_disciplinary_action: bool
    attendance_percent: float


def is_employee_eligible_v1(employee: Employee) -> bool:
    """Initial working version using direct boolean logic."""
    return (
        employee.is_active
        and employee.months_employed >= 12
        and employee.performance_rating >= 4
        and not employee.has_disciplinary_action
        and employee.attendance_percent >= 900
    )


def _meets_performance_and_attendance(employee: Employee) -> bool:
    """Helper extracted to keep the main rule easy to scan."""
    return employee.performance_rating >= 4 and employee.attendance_percent >= 900


def is_employee_eligible(employee: Employee) -> bool:
    """Refactored version focused on readability."""
    is_tenure_eligible = employee.months_employed >= 12
    has_clean_record = not employee.has_disciplinary_action

    return (
        employee.is_active
        and is_tenure_eligible
        and _meets_performance_and_attendance(employee)
        and has_clean_record
    )


class EmployeeEligibilityApp(tk.Tk):
    """Simple desktop UI for evaluating employee eligibility."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Employee Eligibility Checker")
        self.geometry("500x560")
        self.minsize(420, 520)
        self.configure(bg="#eef3ff")

        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(fill="both", expand=True)

        title = ttk.Label(
            main_frame,
            text="Employee Eligibility",
            font=("Segoe UI", 18, "bold"),
        )
        title.pack(pady=(0, 10))

        ttk.Label(main_frame, text="Status").pack(anchor="w")
        self.is_active = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            main_frame,
            text="Employee is active",
            variable=self.is_active,
        ).pack(anchor="w", pady=(0, 8))

        fields = [
            ("Months employed", "months"),
            ("Performance rating", "performance"),
            ("Attendance %", "attendance"),
        ]

        self.entries: dict[str, ttk.Entry] = {}
        for label_text, key in fields:
            frame = ttk.Frame(main_frame)
            frame.pack(fill="x", pady=4)
            ttk.Label(frame, text=label_text, width=18).pack(side="left")
            entry = ttk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.entries[key] = entry

        ttk.Label(main_frame, text="Disciplinary action").pack(anchor="w", pady=(10, 0))
        self.has_action = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            main_frame,
            text="Has disciplinary action",
            variable=self.has_action,
        ).pack(anchor="w")

        button_row = ttk.Frame(main_frame)
        button_row.pack(fill="x", pady=(16, 8))
        ttk.Button(button_row, text="Check Eligibility", command=self.check_eligibility).pack(
            side="left", padx=(0, 8)
        )
        ttk.Button(button_row, text="Reset", command=self.reset_form).pack(side="left")

        self.result_var = tk.StringVar(value="Ready to evaluate")
        self.result_label = ttk.Label(
            main_frame,
            textvariable=self.result_var,
            foreground="#1d4ed8",
            font=("Segoe UI", 12, "bold"),
            wraplength=440,
            justify="left",
        )
        self.result_label.pack(anchor="w", pady=(8, 0))

        summary = ttk.Label(
            main_frame,
            text=(
                "Eligibility rule: active employee, at least 12 months served, "
                "performance rating >= 4.0, no disciplinary action, and attendance >= 900."
            ),
            wraplength=440,
            justify="left",
        )
        summary.pack(anchor="w", pady=(12, 0))

        self.default_values()

    def default_values(self) -> None:
        self.entries["months"].insert(0, "24")
        self.entries["performance"].insert(0, "4.5")
        self.entries["attendance"].insert(0, "950")

    def reset_form(self) -> None:
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.is_active.set(True)
        self.has_action.set(False)
        self.default_values()
        self.result_var.set("Ready to evaluate")
        self.result_label.configure(foreground="#1d4ed8")

    def check_eligibility(self) -> None:
        try:
            employee = Employee(
                is_active=self.is_active.get(),
                months_employed=int(self.entries["months"].get()),
                performance_rating=float(self.entries["performance"].get()),
                has_disciplinary_action=self.has_action.get(),
                attendance_percent=float(self.entries["attendance"].get()),
            )
        except ValueError:
            self.result_var.set("Please enter valid numbers for the employee fields.")
            self.result_label.configure(foreground="#b91c1c")
            return

        eligible = is_employee_eligible(employee)
        status = "ELIGIBLE" if eligible else "NOT ELIGIBLE"
        color = "#15803d" if eligible else "#b91c1c"
        self.result_var.set(f"{status}: {employee}")
        self.result_label.configure(foreground=color)


if __name__ == "__main__":
    app = EmployeeEligibilityApp()
    app.mainloop()
