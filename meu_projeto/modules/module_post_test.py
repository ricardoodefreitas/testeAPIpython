import requests
import random
import string
import pdb
from modules.api_config import API_URL

def get_posts():
    response = requests.get(f'{API_URL}/posts')
    assert response.status_code == 200, "Status code is not 200"
    posts = response.json()
    assert isinstance(posts, list), "Response is not a list"
    assert len(posts) > 0, "No posts found"
    print("GET Response:", posts)
    return posts

def create_post():
    url = f'{API_URL}/posts'
    random_title = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    random_body = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
    payload = {
        'title': random_title,
        'body': random_body,
        'userId': random.randint(1, 10)
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201, "Status code is not 201"
    post = response.json()
    assert 'id' in post, "ID not found in response"
    assert isinstance(post['id'], int), "ID is not an integer"
    print("POST Response:", post)
    return post
