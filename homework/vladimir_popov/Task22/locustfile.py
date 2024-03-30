from locust import task, HttpUser


class NewUser(HttpUser):

    url = "https://api.restful-api.dev"
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    def on_start(self):
        response = self.client.post("/objects", json=self.body)
        self.object_id = response.json()['id']

    @task(1)
    def get_all_posts(self):
        self.client.get("/objects")

    @task(3)
    def get_one_object(self):
        self.client.get(f"/objects/{self.object_id}")

    @task(2)
    def add_new_post(self):
        self.client.post("/objects", json=self.body)
