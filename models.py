from sqlalchemy import Column, Integer, String, DateTime, UnicodeText, select
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils import load_specific_config

Base = declarative_base()

class ProductDB:
    def __init__(self) -> None:
        sqlite_db_path = load_specific_config('sqlite_db_path')
        self.connection_string = f'sqlite:///{sqlite_db_path}'
        self.engine = create_engine(self.connection_string, echo=False)
        self.Session = sessionmaker(bind=self.engine)

    def create_table(self):
        try:
            Base.metadata.create_all(bind=self.engine)
            print('Create table successfully!')
        except:
            print('Error while creating table!')

    def create_session(self):
        return self.Session()

    def insert_product(self, session, product):
        try:
            session.add(product)
            session.commit()
            return True 
        except Exception as e:
            print(e)
            session.rollback()
            return False


class Product(Base):
    __tablename__ = 'Product'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    url = Column('url', String(100), unique=True)
    shop_name = Column('shop_name', String(30))
    name = Column('name', String(80))
    price = Column('price', String(50))
    discount_rate = Column('discount_rate', Integer)
    describe = Column('describe', UnicodeText, unique=True)
    n_solded = Column('n_solded', Integer)
    rating_score = Column('rating_score', Integer)
    n_ratings = Column('n_ratings', Integer)
    n_items =  Column('n_items', Integer)
    type = Column('type', String(100))

db = ProductDB()
db.create_table()
