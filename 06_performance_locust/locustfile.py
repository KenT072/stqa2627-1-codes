from locust import HttpUser, task, between

class HitCounterUser(HttpUser):
    """
    Simulates a user interacting with the Hit Counter app.
    """
    host = "http://127.0.0.1:5000"

    @task(1)
    def load_homepage(self):
        self.client.get("/")

    @task(3)
    def post_hit(self):
        self.client.post("/hit")