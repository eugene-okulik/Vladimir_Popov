import requests
import allure
from endpoints.endpoint import Endpoint


class GetObjectsById(Endpoint):

    @allure.step("Get post by id")
    def get_one_object(self, new_object_id):
        self.response = requests.get(url=f"{self.url}/{new_object_id}")
        self.json = self.response.json()
