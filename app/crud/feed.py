from sqlalchemy.orm import Session

from .. import models, schemas, crud


def create_feed(db: Session, feed: schemas.FeedCreate, user_id: int):
    db_feed = models.Feed(
        date=feed.date,
        video=feed.video,
        thumbnail=feed.thumbnail,
        concentration=feed.concentration,
        user_id=user_id,
    )

    crud.upload_file(feed.video)

    db.add(db_feed)
    db.commit()
    db.refresh(db_feed)

    return db_feed


def get_feeds(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    res = (
        db.query(models.Feed)
        .filter(
            models.Feed.user_id == user_id,
        )
        .slice(skip, limit)
        .all()
    )
    for f in range(len(res)):
        crud.download_file(res[f].video)
        crud.download_file(res[f].thumnail)


def get_feed(db: Session, feed_id: int):
    return db.query(models.Feed).filter(models.Feed.id == feed_id).first()


def delete_feed(db: Session, feed_id: int):
    row = db.query(models.Feed).filter(models.Feed.id == feed_id).first()
    db.delete(row)

    db.commit()
