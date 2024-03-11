import requests


url = "https://api.restful-api.dev/objects"


def add_object():
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
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "Apple MacBook Pro 16", "name is incorrect"
    return new_object_id


def clear(object_id):
    response = requests.delete(f'{url}/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'


def update_object_put():
    object_id = add_object()
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
    response = requests.put(url=f"{url}/{object_id}", json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "Apple MacBook Pro 17", "name is incorrect"
    clear(object_id)


def update_object_patch():
    object_id = add_object()
    body = {
        "name": "Apple MacBook Pro 17 (Updated Name)"
    }
    response = requests.patch(url=f"{url}/{object_id}", json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == "Apple MacBook Pro 17 (Updated Name)", "name is incorrect"
    clear(object_id)


update_object_put()
update_object_patch()
