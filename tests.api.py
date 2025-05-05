import unittest


def solve_quadratic(a, b, c):
    """Решает квадратное уравнение ax² + bx + c = 0."""
    if a == 0:
        if b == 0:
            return "Бесконечно много решений" if c == 0 else "Нет решений"
        return [-c / b]

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return "Нет действительных корней"
    elif discriminant == 0:
        return [-b / (2 * a)]
    else:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        return sorted([x1, x2])


class TestQuadraticSolver(unittest.TestCase):

    def test_all_zero_coefficients(self):
        self.assertEqual(solve_quadratic(0, 0, 0), "Бесконечно много решений")

    def test_zero_a_and_b_but_nonzero_c(self):
        self.assertEqual(solve_quadratic(0, 0, 5), "Нет решений")

    def test_zero_a_linear_equation(self):
        self.assertEqual(solve_quadratic(0, 2, 4), [-2.0])

    def test_zero_b_quadratic_equation(self):
        self.assertEqual(solve_quadratic(1, 0, -4), [-2.0, 2.0])

    def test_zero_c_quadratic_equation(self):
        self.assertEqual(solve_quadratic(1, 2, 0), [-2.0, 0.0])

    def test_zero_b_and_c(self):
        self.assertEqual(solve_quadratic(3, 0, 0), [0.0])

    def test_no_real_roots(self):
        self.assertEqual(solve_quadratic(1, 0, 1), "Нет действительных корней")

    def test_regular_quadratic(self):
        self.assertEqual(solve_quadratic(1, -5, 6), [2.0, 3.0])


if TestQuadraticSolver == "__main__":
    unittest.main(verbosity=2)
