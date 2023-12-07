from sqlalchemy.orm import Session

from .. import models, schemas


def create_feed(db: Session, feed: schemas.FeedCreate, user_id: int):
    db_feed = models.Feed(
        timestamp=feed.timestamp,
        video_url=feed.video_url,
        thumbnail_url=feed.thumbnail_url,
        user_id=user_id,
    )

    db.add(db_feed)
    db.commit()
    db.refresh(db_feed)

    return db_feed


def get_feeds(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Feed)
        .filter(models.Feed.user_id == user_id)
        .slice(skip, limit)
        .all()
    )


def get_feed(db: Session, feed_id: int):
    return db.query(models.Feed).filter(models.Feed.id == feed_id).first()


def delete_feed(db: Session, feed_id: int):
    row = db.query(models.Feed).filter(models.Feed.id == feed_id).first()
    db.delete(row)

    db.commit()
