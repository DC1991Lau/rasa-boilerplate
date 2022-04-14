from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(String)
    type_name = Column(String)
    timestamp = Column(String)
    intent_name = Column(String)
    action_name = Column(String)
    data = Column(String)

