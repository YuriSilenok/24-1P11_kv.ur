"""Тест фаст апи"""

import unittest
from fastapi.testclient import TestClient
from app import app


class TestQuadraticAPI(unittest.TestCase):
    """Класс тестирования"""
    client = TestClient(app)

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
