from .. import schemas


def test_add_feed_success(authorized_client, test_feed: schemas.FeedCreate):
    response = authorized_client.post(
        "/feeds/",
        json={
            "video": test_feed.video,
            "concentration": test_feed.concentration,
            "thumnail": test_feed.thumnail,
        },
    )

    assert response.status_code == 200, response.text


def test_add_feed_failed(client, test_feed: schemas.FeedCreate):
    response = client.post(
        "/feeds/",
        json={
            "video": test_feed.video,
            "concentration": test_feed.concentration,
            "thumnail": test_feed.thumnail,
        },
    )

    assert response.status_code == 401, response.text


def test_get_feeds_succcess(authorized_client):

    response = authorized_client.get(
        "/feeds/", params={"skip": 0, "limit": 100}
    )
    assert response.status_code == 200


def test_get_feeds_failed(client):

    response = client.get(
        "/feeds/", params={"skip": 0, "limit": 100}
    )
    assert response.status_code == 401
