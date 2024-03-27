import requests
import pytest
import allure


url = "https://api.restful-api.dev/objects"


@allure.story("Posts")
@allure.feature("Get all posts")
@allure.title("Test get all posts")
@pytest.mark.medium
def test_get_all_posts(start_end_testing, before_after_test):

    with allure.step("Get all posts"):
        response = requests.get(url=url)
    with allure.step("Check status code is 200"):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.story("Posts")
@allure.feature("Add new post")
@allure.title("Test add new post")
@pytest.mark.critical
@pytest.mark.parametrize("objects", ["Apple MacBook Pro 17", "Apple MacBook Pro 18", "Apple MacBook Pro 19"])
def test_add_post(before_after_test, objects):
    with allure.step("Prepare test data"):
        body = {
            "name": objects,
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
    with allure.step("Create new post"):
        response = requests.post(url, json=body)
    with allure.step("Check status code is 200"):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.story("Posts")
@allure.feature("Get one object")
@allure.title("Test get one object by id")
def test_get_one_object(new_object_id, before_after_test):
    with allure.step(f"Get post by id: {new_object_id}"):
        response = requests.get(url=f"{url}/{new_object_id}")
    with allure.step("Check status code is 200"):
        assert response.status_code == 200, 'Status code is incorrect'


@allure.story("Posts")
@allure.feature("Update object")
@allure.title("Test update object with PUT method")
def test_update_object_put(new_object_id, before_after_test):
    with allure.step("Prepare test data"):
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
    with allure.step(f"Update post with PUT method by id: {new_object_id}"):
        response = requests.put(url=f"{url}/{new_object_id}", json=body)
    with allure.step("Check status code is 200"):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step("Check object new name"):
        assert response.json()['name'] == "Apple MacBook Pro 17", "name is incorrect"


@allure.story("Posts")
@allure.feature("Update object")
@allure.title("Test update object with PATCH method")
def test_update_object_patch(new_object_id, before_after_test):
    with allure.step("Prepare test data"):
        body = {
            "name": "Apple MacBook Pro 17 (Updated Name)"
        }
    with allure.step(f"Update post with PATCH method by id: {new_object_id}"):
        response = requests.patch(url=f"{url}/{new_object_id}", json=body)
    with allure.step("Check status code is 200"):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step("Check object new name"):
        assert response.json()['name'] == "Apple MacBook Pro 17 (Updated Name)", "name is incorrect"


@allure.story("Posts")
@allure.feature("Delete object")
@allure.title("Test delete object")
def test_delete_object(new_object_id, before_after_test):
    with allure.step(f"Delete object by id: {new_object_id}"):
        response = requests.delete(f'{url}/{new_object_id}')
    with allure.step(f"Check object exists by id: {new_object_id}"):
        deleted_object_response = requests.get(url=f"{url}/{new_object_id}")
    with allure.step("Check status code is 200"):
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step("Check status code is 404"):
        assert deleted_object_response.status_code == 404, 'Status code is incorrect'
