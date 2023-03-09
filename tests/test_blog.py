import json


def test_create_blog_bad_request(client):
    response = client.post(
        "/blog/",
        data=json.dumps({"author": "author", "title": None, "content": "content"}),
        content_type="application/json",
    )
    assert response.status__code == 400
    assert response.json is not None
