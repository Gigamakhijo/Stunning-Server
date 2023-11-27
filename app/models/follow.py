from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..database import Base


class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    pending = Column(Boolean, nullable=False, default=True)

    follower_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    followed_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    user = relationship("User")
