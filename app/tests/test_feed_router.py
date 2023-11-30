from .. import schemas


def test_add_feed_success(authorized_client, test_feed: schemas.FeedCreate):
    date_time = test_feed["date"]
    date = str(date_time)

    response = authorized_client.post(
        "/feeds/",
        json={"date": date, **test_feed},
    )
    
    assert response.status_code == 200, response.text

    
def test_add_feed_failed(client, test_feed: schemas.FeedCreate):
    date_time = test_feed["date"]
    date = str(date_time)

    response = client.post(
        "/feeds/",
        json={"date": date, **test_feed},
    )
    
    assert response.status_code == 401, response.text

def test_get_feeds_success(authorized_client,test_feeds):
    
    response = authorized_client.get(
        "/feeds/",
        params = {"skip": 0, "limit": 9}
    )

    assert response.status_code == 200, response.text
    data = response.json()

    print(data)
    assert len(data) == 9

def test_get_feeds_failed(client):
    
    response = client.get(
        "/feeds/",
        params = {"skip": 0, "limit": 9}
    )

    assert response.status_code == 401, response.text
