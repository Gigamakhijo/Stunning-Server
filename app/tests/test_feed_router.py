def test_get_thumbnail_url_success(authorized_client):
    response = authorized_client.post("/feeds/thumbnail_url/thumbnail.jpeg")

    assert response.status_code == 201, response.text


def test_get_video_url_success(authorized_client):
    response = authorized_client.post("/feeds/video_url/video.mp4")

    assert response.status_code == 201, response.text


def test_get_feed_success(authorized_client, test_feed):
    feed_id = test_feed["id"]
    response = authorized_client.get(f"/feeds/{feed_id}")

    assert response.status_code == 200, response.text

    data = response.json()
    for key in test_feed.keys():
        assert data[key] == test_feed[key]


def test_unauthorized_get_feed(client, test_feed):
    feed_id = test_feed["id"]
    response = client.get(f"/feeds/{feed_id}")

    assert response.status_code == 401, response.text


def test_get_other_user_feed(authorized_client, other_test_feed):
    feed_id = other_test_feed["id"]
    response = authorized_client.get(f"/feeds/{feed_id}")

    assert response.status_code == 200, response.text


def test_get_all_feeds_success(authorized_client, test_feeds):
    response = authorized_client.get(
        "/feeds/", params={"skip": 0, "limit": len(test_feeds)}
    )
    assert response.status_code == 200, response.text
    data = response.json()

    for feed, test_feed in zip(data, test_feeds):
        for key in test_feed.keys():
            assert feed[key] == test_feed[key]


def test_unauthorized_get_feeds(client, test_feeds):
    response = client.get("/feeds/", params={"skip": 0, "limit": len(test_feeds)})
    assert response.status_code == 401, response.text


def test_get_other_users_feeds(authorized_client, other_test_feeds):
    response = authorized_client.get(
        "/feeds/", params={"skip": 0, "limit": len(other_test_feeds)}
    )
    assert response.status_code == 200, response.text


def test_post_feed_success(authorized_client, video_url, thumbnail_url, timestamp):
    response = authorized_client.post(
        "/feeds/",
        json={
            "video_url": video_url,
            "thumbnail_url": thumbnail_url,
            "timestamp": timestamp,
        },
    )

    def validate_response(response):
        data = response.json()
        assert data["video_url"] == video_url
        assert data["thumbnail_url"] == thumbnail_url
        assert data["timestamp"] == timestamp

    assert response.status_code == 201, response.text
    validate_response(response)
    feed_id = response.json()["id"]

    response = authorized_client.get(f"/feeds/{feed_id}")

    assert response.status_code == 200, response.text
    validate_response(response)


def test_unauthorized_post_feed(client, video_url, thumbnail_url, timestamp):
    response = client.post(
        "/feeds/",
        json={
            "video_url": video_url,
            "thumbnail_url": thumbnail_url,
            "timestamp": timestamp,
        },
    )
    assert response.status_code == 401, response.text


def test_delete_feed_success(authorized_client, test_feed):
    feed_id = test_feed["id"]
    response = authorized_client.delete(
        f"/feeds/{feed_id}",
    )
    assert response.status_code == 204, response.text


def test_unauthorized_delete_feed(client, video_url, thumbnail_url, timestamp):
    response = client.post(
        "/feeds/",
        json={
            "video_url": video_url,
            "thumbnail_url": thumbnail_url,
            "timestamp": timestamp,
        },
    )
    assert response.status_code == 401, response.text


def test_delete_other_user_feed(authorized_client, other_test_feed):
    feed_id = other_test_feed["id"]
    response = authorized_client.delete(
        f"/feeds/{feed_id}",
    )
    assert response.status_code == 403, response.text


def test_get_feed_fail(authorized_client):
    feed_id = 1_000_000
    response = authorized_client.get(f"/feeds/{feed_id}")

    assert response.status_code == 404, response.text


def test_get_all_feeds_fail(authorized_client, test_feeds):
    response = authorized_client.get(
        "/feeds/", params={"skip": len(test_feeds), "limit": len(test_feeds) + 100}
    )
    assert response.status_code == 200, response.text
    assert len(response.json()) == 0


def test_delete_feed_fail(authorized_client):
    feed_id = 1_000_000
    response = authorized_client.delete(f"/feeds/{feed_id}")

    assert response.status_code == 404, response.text
