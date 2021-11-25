import random
from data_base import Tables
import lists

def random_tag(session):
    for i in range(9):
        tag_itm = Tables.Tag(name_tag=random.choice(lists.Tags))
        session.add(tag_itm)
    session.commit()


def random_blog(session):
    for i in range(4):
        blog_itm = Tables.Blog(name_Blog=random.choice(lists.Blogs))
        session.add(blog_itm)
    session.commit()


def random_publication(session):
    for i in range(21):
        publication_itm = Tables.Publication(name_Publications=random.choice(lists.Publication))
        session.add(publication_itm)
    session.commit()

def random_author(session):
    for i in range(100):
        author_itm = Tables.Author(name_Author=lists.NSS[i])
        session.add(author_itm)
    session.commit()

def teg_author_tag(session):
    author_id = Tables.Author.count_articles(session)
    for author in range(author_id):
        tags_id = random.randint(3, 10)
        tags = set()
        for i in range(tags_id):
            if i not in tags:
                teg_id = Tables._publicatuin_tag(tag_id=i, author_id=author)
                tags.add(i)
            else:
                continue
            session.add(teg_id)
    session.commit()


def random_db(session):
    random_author(session)
    random_tag(session)
    random_blog(session)
    random_publication(session)

