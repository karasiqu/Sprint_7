import allure
import requests

from urls import BASE_URL, LIST_ORDERS


class TestListOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = requests.get(BASE_URL + LIST_ORDERS)

        assert response.status_code == 200
        body = response.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)
