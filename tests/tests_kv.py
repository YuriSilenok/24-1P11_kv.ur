'''Тест квадратного уравнения'''

import unittest
from main import cvyr


class TestKv(unittest.TestCase):
    '''Кв уравн'''
    def test_1(self):
        """Тест диск больше нуля"""
        a, b, c = 4, 2, -2
        disk = 36
        x1 = 0.5
        x2 = -1
        res = cvyr(a, b, c)
        self.assertEqual(len(res), 4, "Неверное количество элементов")
        self.assertEqual(
            res[0],
            "Дискриминант > 0, квадратное уравнение имеет 2 корня"
        )
        self.assertEqual(res[1], disk, "Неверный дискриминант")
        self.assertEqual(res[2], x1, "Неверный корень 1")
        self.assertEqual(res[3], x2, "Неверный корень 2")

    def test_2(self):
        """Тест диск равен нуля"""
        a, b, c = 3, -18, 27
        disk = 0
        x = 3
        res = cvyr(a, b, c)
        self.assertEqual(len(res), 3, "Неверное количество элементов")
        self.assertEqual(
            res[0],
            "Дискриминант = 0, квадратное уравнение имеет 1 корень"
        )
        self.assertEqual(res[1], disk, "Неверный дискриминант")
        self.assertEqual(res[2], x, "Неверный корень 1")

    def test_3(self):
        """Тест диск меньше нуля"""
        a, b, c = 1, 2, 2
        disk = -4
        res = cvyr(a, b, c)
        self.assertEqual(len(res), 2, "Неверное количество элементов")
        self.assertEqual(
            res[0],
            "Дискриминант меньше нуля, квадратное уравнение не имеет корней"
        )
        self.assertEqual(res[1], disk, "Корней нет")

    def test_4(self):
        """Тест для линейного уравнения"""
        a, b, c = 0, 2, -4
        x = 2
        res = cvyr(a, b, c)
        self.assertEqual(len(res), 2, "Неверное количество элементов")
        self.assertEqual(
            res[0],
            "Линейное уравнение, прямая пересекает ось Оx"
        )
        self.assertEqual(res[1], x)

    def test_5(self):
        """Тест все переменные равны нулю"""
        a, b, c = 0, 0, 0
        res = cvyr(a, b, c)
        self.assertEqual(len(res), 4, "Неверное количество элементов")
        self.assertEqual(
            res[0],
            "Бесконечное множество решений (тождество 0 = 0)"
        )
        self.assertEqual(res[1], a)
        self.assertEqual(res[2], b)
        self.assertEqual(res[3], c)
