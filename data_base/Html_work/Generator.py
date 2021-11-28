import table
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DataInfo:

    def __init__(self, db_url):
        engine = create_engine(db_url)
        table.Base.metadata.create_all(bind=engine)
        self.maker = sessionmaker(bind=engine)


    def save_promo_products(self, *args):
        products = [table.Info(**i) for i in args]
        session = self.maker()
        session.add_all(products)
        try:
            session.commit()
        except Exception as exc:
            session.rollback()
        finally:
            session.close()
