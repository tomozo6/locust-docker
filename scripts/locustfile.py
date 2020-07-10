import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        url_base_path = "/v1/weather/forecasts"
        lat = "35.{}".format(random.randint(10, 100))
        lng = "139.{}".format(random.randint(10, 100))
        url = f"{end_point}/{lat},{lng}?lang=ja"
        self.client.get(url)
#        self.client.get("/world")

#    @task(3)
#    def view_item(self):
#        item_id = random.randint(1, 10000)
#        self.client.get(f"/item?id={item_id}", name="/item")
#
#    def on_start(self):
#        self.client.post("/login", {"username":"foo", "password":"bar"})
