import allure
import requests

from urls import BASE_URL, LOGIN_COURIER, TIMEOUT


class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_login_success(self, new_courier):
        login, password, _ = new_courier
        response = requests.post(
            BASE_URL + LOGIN_COURIER,
            data={"login": login, "password": password},
            timeout=TIMEOUT,
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин без логина возвращает ошибку")
    def test_login_without_login(self, new_courier):
        _, password, _ = new_courier
        response = requests.post(
            BASE_URL + LOGIN_COURIER,
            data={"password": password},
            timeout=TIMEOUT,
        )

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Логин без пароля возвращает ошибку")
    def test_login_without_password(self, new_courier):
        login, _, _ = new_courier
        response = requests.post(
            BASE_URL + LOGIN_COURIER,
            data={"login": login},
            timeout=TIMEOUT,
        )

        assert response.status_code == 400

    @allure.title("Логин с неверным паролем возвращает ошибку")
    def test_login_wrong_password(self, new_courier):
        login, _, _ = new_courier
        response = requests.post(
            BASE_URL + LOGIN_COURIER,
            data={"login": login, "password": "wrong_password"},
            timeout=TIMEOUT,
        )

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Логин несуществующего курьера возвращает ошибку")
    def test_login_nonexistent_courier(self):
        response = requests.post(
            BASE_URL + LOGIN_COURIER,
            data={"login": "nonexistent_xyz_123", "password": "wrong"},
            timeout=TIMEOUT,
        )

        assert response.status_code == 404
        assert "message" in response.json()
