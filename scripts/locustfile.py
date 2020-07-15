import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        lat = "35.{}".format(random.randint(10, 100))
        lng = "139.{}".format(random.randint(10, 100))
        self.client.get("/v1/weather/forecasts/{0},{1}?lang=ja".format(lat, lng))

#    @task(3)
#    def view_item(self):
#        item_id = random.randint(1, 10000)
#        self.client.get(f"/item?id={item_id}", name="/item")
#
#    def on_start(self):
#        self.client.post("/login", {"username":"foo", "password":"bar"})
