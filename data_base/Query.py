from data_base import Tables

def author_tag(session, tag_id):
    author_tags = session.query(Tables.Author).filter(Tables.Tag.id == tag_id).all()
    return author_tags

def tag_author(session, author_name):
    tags_author = session.query(Tables.Tag).filter(Tables.Author.id == author_name).all()
    return tags_author