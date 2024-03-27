import allure
import requests
from endpoints.endpoint import Endpoint


class AddPost(Endpoint):

    @allure.step("Create new post")
    def add_new_post(self, body):
        self.response = requests.post(self.url, json=body)
        self.json = self.response.json()
