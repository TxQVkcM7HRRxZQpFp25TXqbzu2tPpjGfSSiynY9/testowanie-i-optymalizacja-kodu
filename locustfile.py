from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_comments(self):
        self.client.get("/comments")

    @task
    def get_albums(self):
        self.client.get("/albums")

    @task
    def get_photos(self):
        self.client.get("/photos")

    @task
    def search_posts(self):
        self.client.get("/posts?search=lorem")
