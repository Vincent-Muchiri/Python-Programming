import requests


def request_blog_data():
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    blog_data = response.json()

    return blog_data


class Post:
    def __init__(self):
        self.blog_data = request_blog_data()

    def get_post(self, post_index: int):
        post_data = self.blog_data[post_index]
        return post_data
