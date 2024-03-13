import requests
import pytest


url = "https://api.restful-api.dev/objects"


@pytest.fixture()
def new_object_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url, json=body)
    new_object_id = response.json()['id']
    yield new_object_id
    response = requests.delete(f'{url}/{new_object_id}')


@pytest.fixture(scope="session")
def start_end_testing():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(scope="function")
def before_after_test():
    print("before test")
    yield
    print("after test")


@pytest.mark.medium
def test_get_all_posts(start_end_testing, before_after_test):
    response = requests.get(url=url)
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.critical
@pytest.mark.parametrize("objects", ["Apple MacBook Pro 17", "Apple MacBook Pro 18", "Apple MacBook Pro 19"])
def test_add_post(before_after_test, objects):
    body = {
        "name": objects,
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url, json=body)
    assert response.status_code == 200, 'Status code is incorrect'


def test_get_one_object(new_object_id, before_after_test):
    response = requests.get(url=f"{url}/{new_object_id}")
    assert response.status_code == 200, 'Status code is incorrect'


def test_update_object_put(new_object_id, before_after_test):
    body = {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(url=f"{url}/{new_object_id}", json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "Apple MacBook Pro 17", "name is incorrect"


def test_update_object_patch(new_object_id, before_after_test):
    body = {
        "name": "Apple MacBook Pro 17 (Updated Name)"
    }
    response = requests.patch(url=f"{url}/{new_object_id}", json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "Apple MacBook Pro 17 (Updated Name)", "name is incorrect"


def test_delete_object(new_object_id, before_after_test):
    response = requests.delete(f'{url}/{new_object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
