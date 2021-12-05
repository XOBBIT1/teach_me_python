from data_base import Tables

def author_tag(session, author_name):
    author_tags = session.query(Tables.Author).filter(Tables.Author.id == author_name).all()
    return author_tags

def tag_author(session, tag_id):
    tags_author = session.query(Tables.Tag).filter(Tables.Tag.id == tag_id).all()
    return tags_author