import allure
import requests

from helpers import generate_random_string, delete_courier, get_courier_id
from urls import BASE_URL, CREATE_COURIER


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        courier_id = get_courier_id(login, password)
        delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": "Test"}

        first_response = requests.post(BASE_URL + CREATE_COURIER, data=payload)
        second_response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert first_response.status_code == 201
        assert second_response.status_code == 409

        courier_id = get_courier_id(login, password)
        delete_courier(courier_id)

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self):
        payload = {"password": "pass", "firstName": "Test"}
        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self):
        payload = {"login": generate_random_string(10), "firstName": "Test"}
        response = requests.post(BASE_URL + CREATE_COURIER, data=payload)

        assert response.status_code == 400
        assert "message" in response.json()
