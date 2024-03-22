import pytest
import requests

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