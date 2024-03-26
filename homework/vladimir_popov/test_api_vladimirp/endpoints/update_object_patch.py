import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateObjectPatch(Endpoint):

    @allure.step("Update object with PATCH method by id")
    def update_object_patch(self, object_id, body):
        self.response = requests.patch(url=f"{self.url}/{object_id}", json=body)
        self.json = self.response.json()
