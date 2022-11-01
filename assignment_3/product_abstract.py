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
        print(f"new product: {product} created now")

    def edit_product(self, name):
        print(f"{name} product edited")

    def get_product_by_id(self, id):
        print(f"product id is: {id}")

    def get_all_products(self):
        print("names of all print")

    def upload_product_image(self, image):
        print(f"image uploaded to{image}")

    def delete_product(self, id):
        print(f"Product id: {id} has been deleted successfully")


product1 = ProductManager()


product1.edit_product("Chocolate")
product1.get_product_by_id(123456)
product1.get_all_products()
product1.upload_product_image("path/xyz")
product1.delete_product(123)
