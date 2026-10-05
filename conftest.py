import pytest

from helpers import register_new_courier_and_return_login_password, delete_courier, get_courier_id


@pytest.fixture
def new_courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    yield login, password, first_name

    courier_id = get_courier_id(login, password)
    if courier_id:
        delete_courier(courier_id)
