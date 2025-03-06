from modules.module_post_test import get_posts, create_post

def test_get_posts():
    posts = get_posts()
    print("GET /posts passed")

def test_create_post():
    post = create_post()
    print("POST /posts passed")

if __name__ == "__main__":
    test_get_posts()
    test_create_post()
    
