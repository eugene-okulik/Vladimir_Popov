import pytest
import requests
from endpoints.get_all_objects import GetObjects
from endpoints.add_post import AddPost
from endpoints.get_one_object import GetObjectsById
from endpoints.update_object_put import UpdateObjectPut
from endpoints.update_object_patch import UpdateObjectPatch
from endpoints.delete_object import DeleteObject


url = "https://api.restful-api.dev/objects"


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


@pytest.fixture()
def object_id():
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
    object_id = response.json()['id']
    yield object_id
    response = requests.delete(f'{url}/{object_id}')


@pytest.fixture
def get_all_objects_endpoint():
    return GetObjects()


@pytest.fixture
def add_post_endpoint():
    return AddPost()


@pytest.fixture
def get_object_endpoint():
    return GetObjectsById()


@pytest.fixture
def update_object_put_endpoint():
    return UpdateObjectPut()


@pytest.fixture
def update_object_patch_endpoint():
    return UpdateObjectPatch()


@pytest.fixture
def delete_object_endpoint():
    return DeleteObject()
