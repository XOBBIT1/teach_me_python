import re

from .pasge import MagnitPage
from .patterms import PRODUCTS_PATTEREN

__all__ =(
    "MagnitDisasembler",
)

class MagnitDisasembler:
    _queue_prodicts = []


    def __init__(self,start_page:str, database):
        self.done_urls = set()
        self.start_page = MagnitPage.get_page_from_url(start_page)
        self.done_urls.add(self.start_page.url)
        self.database = database

    def run(self):
        for i in self.start_page.get_page_rel_links(PRODUCTS_PATTEREN):
            if i in self.done_urls:
                continue
            self.done_urls.add(i)
            products_page = MagnitPage.get_page_from_url(i)
            product_dict = products_page.to_dict()
            self.save_to_base(product_dict)

    def save_to_base(self, product_dict):
        self._queue_prodicts.append(product_dict)
        if len(self._queue_prodicts) > 10:
            self.database.save_promo_products(*self._queue_prodicts)
            self._queue_prodicts.clear()