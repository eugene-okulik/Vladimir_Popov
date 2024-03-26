import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObjectPut(Endpoint):

    @allure.step("Update post with PUT method by id")
    def update_object_put(self, new_object_id, body):
        self.response = requests.put(url=f"{self.url}/{new_object_id}", json=body)
        self.json = self.response.json()
