from .. import schemas


def test_create_feed_success(authorized_client, test_feed: schemas.FeedCreate):
    response = authorized_client.post(
        "/feeds/",
        json={
            "user_id": test_feed.user_id,
            "video": test_feed.video,
            "concentration": test_feed.concentration,
            "thumnail": test_feed.thumnail,
        },
    )

    assert response.status_code == 200, response.text


def test_create_feed_failed(client, test_feed: schemas.FeedCreate):
    response = client.post(
        "/feeds/",
        json={
            "user_id": test_feed.user_id,
            "video": test_feed.video,
            "concentration": test_feed.concentration,
            "thumnail": test_feed.thumnail,
        },
    )

    assert response.status_code == 401, response.text


def test_get_feed_succcess(authorized_client, test_feeds):
    user_id = test_feeds[0].user_id

    response = authorized_client.get(
        "/feeds/", params={"user_id": user_id, "skip": 0, "limit": 100}
    )
    assert response.status_code == 200


def test_get_feed_failed(client, test_feeds):
    user_id = test_feeds[0].user_id

    response = client.get(
        "/feeds/", params={"user_id": user_id, "skip": 0, "limit": 100}
    )
    assert response.status_code == 401
