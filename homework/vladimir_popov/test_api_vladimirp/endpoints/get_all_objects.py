import requests
import allure
from endpoints.endpoint import Endpoint


class GetObjects(Endpoint):

    @allure.step("Get all posts")
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
