from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
    Text
)

# todo:  Заполнить базу минимум 100 авторами, у каждого автора от 50 до 100 статей, в которых от 3х тегов
# todo: Составить запрос и определить все теги использованые этим автором
# todo: Составить запрос и получить всех авторов которые использовали "Этот тег"

Base = declarative_base()

_publicatuin_tag = Table(
    "_author_tag",
    Base.metadata,
    Column("author.id", Integer, ForeignKey("author.id")),
    Column("tag.id", Integer, ForeignKey("tag.id"))
)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_tag = Column(Text(40), unique=False)

class Publication(Base):
    __tablename__ = 'publication'
    id = Column(Integer,  primary_key=True, autoincrement=True)
    name_Publications = Column(String(100), unique=False)
    tag_id = Column(Integer, ForeignKey("tag.id"), nullable=True)
    tags = relationship(Tag, backref="publications")


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_Author = Column(String(10), unique=False)
    publications_id = Column(Integer, ForeignKey("publication.id"), nullable=True)
    publications = relationship(Publication,  backref="author")
    tags = relationship(Tag, secondary="_author_tag",  backref="author")

class Blog(Base):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name_Blog = Column(String(30), unique=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=True)
    author = relationship(Author,  backref="blog")