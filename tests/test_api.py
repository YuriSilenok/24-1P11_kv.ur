"""Тест FastAPI"""

from fastapi.testclient import TestClient
from app import app
import unittest


class TestKvYrAPI(unittest.TestCase):
    """Атотесты для FastAPI"""

    def setUp(self):
        """Инициализация клиента"""
        self.client = (TestClient(app))

    def test_1(self):
        """Дискриминант меньше нуля, корней нет"""
        params = {"a": 1, "b": 2, "c": 1}
        x = -1
        response = self.client.get("/KvYr", params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data[0],
            "Дискриминант = 0, квадратное уравнение имеет 1 корень"
        )
        self.assertEqual(data[1], x)

    def test_two_real_roots(self):
        """Тестирование disk > 0"""
        params = {
            "a": 4,
            "b": 2,
            "c": -2
        }
        response = self.client.get("/solve/", params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data["message"],
            "Дискриминант > 0, квадратное уравнение имеет 2 корня"
        )
        self.assertAlmostEqual(float(data["disk"]), 36.0)
        self.assertAlmostEqual(float(data["x1"]), -1.0)
        self.assertAlmostEqual(float(data["x2"]), 0.5)
