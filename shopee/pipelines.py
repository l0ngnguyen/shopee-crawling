# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from models import Product, ProductDB
from scrapy.exceptions import DropItem


class PreprocessPipeline:
    def _process_attr(self, item, attr_name, convert_method=None, val_if_none=None):
        value = item[attr_name]
        if not value:
            item[attr_name] = val_if_none
        else:
            try:
                if convert_method:
                    item[attr_name] = convert_method(value)
            except:
                item[attr_name] = val_if_none

    def process_item(self, item, spider):
        self._process_attr(item, 'n_items', int)
        self._process_attr(item, 'rating_score', float, 0)
        self._process_attr(item, 'n_ratings', int, 0)

        s = item['n_solded']
        if s:
            if s[-1] == 'k':
                s = s.replace(',', '')
                s = s.replace('k', '')
                item['n_solded'] = int(s) * 100
            else:
                self._process_attr(item, 'n_solded', int)

        dr = item['discount_rate'] if item['discount_rate'] else '0% giảm'
        item['discount_rate'] = int(dr.split('%')[0])

        return item


class InsertDBPipeline:
    def __init__(self) -> None:
        self.db = ProductDB()
        self.db.create_table()

    def process_item(self, item, spider):
        session = self.db.create_session()
        new_product = Product(
            url=item['url'],
            shop_name=item['shop_name'],
            name=item['name'],
            price=item['price'],
            discount_rate=item['discount_rate'],
            describe=item['describe'],
            n_solded=item['n_solded'],
            rating_score=item['rating_score'],
            n_ratings=item['n_ratings'],
            n_items=item['n_items'],
            type=item['type']
        )
        success = self.db.insert_product(session, new_product)
        session.close()

        if success:
            return item
        else:
            raise DropItem()
