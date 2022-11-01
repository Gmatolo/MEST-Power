from abc import ABC, abstractmethod


class Product:
    id = ""
    name = ""
    description = ""
    price = ""
    image = ""
    expiry_date = ""
    date_created = ""


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


class ProductManager(ProductAbstract):
    def create_product(self, product: Product):
        print("product created")

    def edit_product(self, name):
        print("product edited")

    def get_product_id(self, id):
        print("product id")

    def get_all_products(self):
        print("names of all print")

    def upload_product_image(self, image):
        print("image uploaded")

    def delete_product(self, id):
        print("product deleted")


product1 = ProductManager()
