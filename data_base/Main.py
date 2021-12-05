from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_base import Tables
from Generator import random_db
import Query

class DataBase:
    def __init__(self,db_url):
        engin = create_engine(db_url)
        Tables.Base.metadata.create_all(bind=engin)# нужно связать базовый класс и всю структуру бд с этим движком
        self.maker = sessionmaker(bind=engin)

def main():
    db_url = "sqlite:///some_db1.db"
    db = DataBase(db_url)
    session = db.maker()
    random_db(session)

    author_tags = Query.author_tag(session, 5)
    tags_author = Query.tag_author(session, "#Орига")
    return tags_author, author_tags


if __name__ == '__main__':
    main()