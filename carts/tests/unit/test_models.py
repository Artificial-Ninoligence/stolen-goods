from django.test import TestCase, Client
from carts.models import Cart, CartItem
from carts.views import _cart_id, add_cart
from product.models import Product
from category.models import Category
from django.contrib.auth import get_user_model
import datetime


CustomUser = get_user_model()


class TestCarts(TestCase):

    def setUp(self):

        email = 'customusertest@unittest.com'
        username = 'usertest'
        password = 'foo'
        first_name = 'Tester'
        last_name = 'Unitester'

        custom_user = CustomUser.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        category = Category.objects.create(
            name='jewellery',
            slug='Jewellery',
            description='Oldest artefact used to show status',
            image='jewellery.png',
        )
        product = Product.objects.create(
            category_id=1,
            slug='blue-ocean-necklace',
            name='Blue Ocean Necklace',
            price=300000000,
            discounted_price=10000,
        )

        # Retrieving the session to create the cart id (id=_cart_id)
        client = Client()
        session = client.session
        session["Session Key"] = "0123456789"
        session.save()

        self.cart = Cart.objects.create(
            cart_id=session,
            date_added=datetime.datetime.now()
        )

        self.cart_item = CartItem.objects.create(
            user_id=custom_user.id,
            product_id=product.id,
            cart_id=self.cart.id,
            quantity=2
        )

    def test_cart_creation(self):

        cart = self.cart

        self.assertTrue(isinstance(cart, Cart))
        self.assertEqual(cart.__str__(), cart.cart_id)

    def test_cart_item_creation(self):

        cart_item = self.cart_item

        self.assertTrue(isinstance(cart_item, CartItem))
        self.assertTrue(cart_item.is_active, True)
        self.assertEqual(cart_item.__unicode__(), cart_item.product)
        self.assertEqual(cart_item.sub_total(), 20000)
