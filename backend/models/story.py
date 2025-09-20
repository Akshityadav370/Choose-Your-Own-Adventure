from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship

from db.database import Base

# sqlalchemy - ORM 
# similar to how we mapped .env to our settings class, 
# fastapi has these sqlalchemy classes which helps us map data into python objects
# so that we don't need to write SQL code

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    # index = we'll be able to look the item through this field
    title = Column(String, index=True)
    session_id = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes = relationship(argument="Story_Node", back_populates="story")

class Story_Node(Base): 
    __tablename__ = "story_nodes"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id"), index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=list)

    story = relationship(argument="Story", back_populates="nodes")

# story.nodes → list of all related nodes (One-to-Many side)

# node.story → the parent story (Many-to-One side)