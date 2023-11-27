from sqlalchemy.orm import Session

from .. import models, schemas


def create_feed(db: Session, feed: schemas.FeedCreate):
    db_feed = models.Feed(
        user_id=feed.user_id,
        video=feed.video,
        concentration=feed.concentration,
        thumnail=feed.thumnail,
    )

    db.add(db_feed)
    db.commit()
    db.refresh(db_feed)

    return db_feed


def get_feeds_by_userid(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Feed)
        .filter(
            models.Feed.user_id == user_id,
        )
        .slice(skip, limit)
        .all()
    )
