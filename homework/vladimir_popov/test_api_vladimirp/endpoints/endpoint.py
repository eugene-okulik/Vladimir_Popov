import allure


class Endpoint:
    url = "https://api.restful-api.dev/objects"
    response = None

    @allure.step("Check status code is 200")
    def check_status_is_200(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step("")
    def check_status_is_404(self):
        assert self.response.status_code == 404, 'Status code is incorrect'

    @allure.step("Check object new name")
    def check_object_new_name(self, object_name):
        assert self.response.json()['name'] == object_name, "name is incorrect"
