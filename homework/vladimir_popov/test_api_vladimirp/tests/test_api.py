import pytest
import allure


@allure.story("Posts")
@allure.feature("Get all posts")
@allure.title("Test get all posts")
@pytest.mark.medium
def test_get_all_posts(start_end_testing, before_after_test, get_all_objects_endpoint):
    get_all_objects_endpoint.get_all_objects()
    get_all_objects_endpoint.check_status_is_200()


@allure.story("Posts")
@allure.feature("Add new post")
@allure.title("Test add new post")
@pytest.mark.critical
@pytest.mark.parametrize("objects", ["Apple MacBook Pro 17", "Apple MacBook Pro 18", "Apple MacBook Pro 19"])
def test_add_post(before_after_test, objects, add_post_endpoint):
    body = {
        "name": objects,
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    add_post_endpoint.add_new_post(body)
    add_post_endpoint.check_status_is_200()


@allure.story("Posts")
@allure.feature("Get one object")
@allure.title("Test get one object by id")
def test_get_one_object(object_id, before_after_test, get_object_endpoint):
    get_object_endpoint.get_one_object(object_id)
    get_object_endpoint.check_status_is_200()


@allure.story("Posts")
@allure.feature("Update object")
@allure.title("Test update object with PUT method")
def test_update_object_put(object_id, before_after_test, update_object_put_endpoint):
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
    update_object_put_endpoint.update_object_put(object_id, body)
    update_object_put_endpoint.check_status_is_200()
    update_object_put_endpoint.check_object_new_name(body['name'])


@allure.story("Posts")
@allure.feature("Update object")
@allure.title("Test update object with PATCH method")
def test_update_object_patch(object_id, before_after_test, update_object_patch_endpoint):
    body = {
        "name": "Apple MacBook Pro 17 (Updated Name)"
    }
    update_object_patch_endpoint.update_object_patch(object_id, body)
    update_object_patch_endpoint.check_status_is_200()
    update_object_patch_endpoint.check_object_new_name(body['name'])


@allure.story("Posts")
@allure.feature("Delete object")
@allure.title("Test delete object")
def test_delete_object(before_after_test, delete_object_endpoint, get_object_endpoint, object_id):
    delete_object_endpoint.delete_object_by_id(object_id)
    delete_object_endpoint.check_status_is_200()
    delete_object_endpoint.check_object_deleted(object_id)
    delete_object_endpoint.check_status_is_404()
