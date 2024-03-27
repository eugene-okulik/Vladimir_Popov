import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete object by id")
    def delete_object_by_id(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")
        self.json = self.response.json()

    @allure.step("Check object deleted")
    def check_object_deleted(self, object_id):
        self.response = requests.get(f"{self.url}/{object_id}")
        self.json = self.response.json()
