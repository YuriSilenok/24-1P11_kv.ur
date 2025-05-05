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
        params = {"a": 1, "b": 2, "c": 5}
        response = self.client.get("/KvYr", params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(
            data[0],
            "Дискриминант меньше нуля, квадратное уравнение не имеет корней"
        )
        self.assertEqual(data[1], 0)
