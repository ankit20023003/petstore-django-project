from django.test import TestCase
from.models import Product

# Create your tests here.

def add(a,b):
    return a+b
class ProductTest(TestCase):

    def setUp(self):
        self.product=Product.manager.create(product_name="testProduct",
                               product_price=2500,
                               product_brand="superpet",
                               product_picture="anc.jpg",
                               product_description="diuhudihiuewh")


    def test_create_product(self):
        product=Product.manager.get(id=self.product.id)   
        self.assertEqual(self.product,product)      

    def test_all_products(self):
        products=Product.manager.all()
        self.assertTrue(len(products)>0)




    def test_add(self):
        self.assertEqual(add(5,5),10)