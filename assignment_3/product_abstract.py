from abc import ABC, abstractmethod

class Product:
    id=''
    name=''
    description=''
    price=''
    image=''
    expiry_date=''
    date_created=''

class ProductAbstract(ABC):
    @abstractmethod
    def create_product(self, product: Product):
        pass
    @abstractmethod
    def edit_product(self):
        pass
    @abstractmethod
    def get_product_by_id(self, id):
        pass
    @abstractmethod
    def get_all_products(self):
        pass

    @abstractmethod
    def delete_product(self, id):
        pass