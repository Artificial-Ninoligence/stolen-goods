from django.test import TestCase
from product.models import Product
from category.models import Category
from transactions.models import Payment, Order, OrderProduct
from django.contrib.auth import get_user_model


CustomUser = get_user_model()


class TestTransactions(TestCase):

    def setUp(self):

        custom_user = CustomUser.objects.create_user(
            email='customusertest1@unittest.com',
            username='usertest1',
            password='foo',
            first_name='User1',
            last_name='Test1'
        )

        category = Category.objects.create(
            name='Jewellery',
            slug='jewellery',
            description='Oldest artefact used to show status',
            image='jewellery.png',
        )

        product = Product.objects.create(
            category_id=category.id,
            slug='blue-ocean-necklace',
            name='Blue Ocean Necklace',
            price=300000000,
            discounted_price=10000,
            stock=2
        )

        self.payment = Payment.objects.create(
            user_id=custom_user.id,
            payment_id='123456789',
            payment_method='Paypal',
            amount_paid=str(product.discounted_price),
            status='Completed'
        )

        self.order = Order.objects.create(
            payment_id=self.payment.id,
            user_id=custom_user.id,
            first_name=custom_user.first_name,
            last_name=custom_user.last_name,
            email=custom_user.email,
            order_number='F123456789',
            order_total=10190,
            tax=19,
            address_line_1='Storkower Str. 108',
        )

        self.order_product = OrderProduct.objects.create(
            order_id=self.order.id,
            payment_id=self.payment.id,
            user_id=custom_user.id,
            product_id=product.id,
            quantity=1,
            price=product.discounted_price, 
        )

    def test_payment_creation(self):

        payment = self.payment

        self.assertTrue(isinstance(payment, Payment))
        self.assertTrue(payment.payment_id, '123456789')
        self.assertEqual(payment.payment_method, 'Paypal')
        self.assertEqual(payment.amount_paid, '10000')
        self.assertEqual(payment.__str__(), payment.payment_id)

    def test_order_creation(self):

        order = self.order

        self.assertTrue(isinstance(order, Order))
        self.assertEqual(order.__str__(), order.first_name)

    def test_order_product_creation(self):

        order_product = self.order_product

        self.assertTrue(isinstance(order_product, OrderProduct))
        self.assertEqual(order_product.__str__(), order_product.product.name)
