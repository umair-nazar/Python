import unittest

from employee_eligibility import Employee, is_employee_eligible, is_employee_eligible_v1


class TestEmployeeEligibility(unittest.TestCase):
    def assert_both_versions(self, employee: Employee, expected: bool) -> None:
        self.assertEqual(is_employee_eligible_v1(employee), expected)
        self.assertEqual(is_employee_eligible(employee), expected)

    def test_normal_eligible_case(self) -> None:
        employee = Employee(
            is_active=True,
            months_employed=24,
            performance_rating=4.5,
            has_disciplinary_action=False,
            attendance_percent=950,
        )
        self.assert_both_versions(employee, True)

    def test_boundary_values_pass(self) -> None:
        employee = Employee(
            is_active=True,
            months_employed=12,
            performance_rating=4.0,
            has_disciplinary_action=False,
            attendance_percent=900,
        )
        self.assert_both_versions(employee, True)

    def test_fails_when_inactive(self) -> None:
        employee = Employee(
            is_active=False,
            months_employed=24,
            performance_rating=5.0,
            has_disciplinary_action=False,
            attendance_percent=1000,
        )
        self.assert_both_versions(employee, False)

    def test_fails_when_tenure_below_minimum(self) -> None:
        employee = Employee(
            is_active=True,
            months_employed=11,
            performance_rating=5.0,
            has_disciplinary_action=False,
            attendance_percent=1000,
        )
        self.assert_both_versions(employee, False)

    def test_fails_when_performance_below_minimum(self) -> None:
        employee = Employee(
            is_active=True,
            months_employed=24,
            performance_rating=3.99,
            has_disciplinary_action=False,
            attendance_percent=1000,
        )
        self.assert_both_versions(employee, False)

    def test_fails_when_has_disciplinary_action(self) -> None:
        employee = Employee(
            is_active=True,
            months_employed=24,
            performance_rating=5.0,
            has_disciplinary_action=True,
            attendance_percent=1000,
        )
        self.assert_both_versions(employee, False)

    def test_fails_when_attendance_below_minimum(self) -> None:
        employee = Employee(
            is_active=True,
            months_employed=24,
            performance_rating=5.0,
            has_disciplinary_action=False,
            attendance_percent=899.99,
        )
        self.assert_both_versions(employee, False)


if __name__ == "__main__":
    unittest.main()
