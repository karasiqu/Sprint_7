import allure
import pytest
import requests

from data import ORDER_COLORS, ORDER_PAYLOAD
from urls import BASE_URL, CREATE_ORDER


class TestCreateOrder:

    @allure.title("Создание заказа с цветами: {colors}")
    @pytest.mark.parametrize("colors", ORDER_COLORS)
    def test_create_order_with_colors(self, colors):
        payload = ORDER_PAYLOAD.copy()
        payload["color"] = colors

        response = requests.post(BASE_URL + CREATE_ORDER, json=payload)

        assert response.status_code == 201
        assert "track" in response.json()
