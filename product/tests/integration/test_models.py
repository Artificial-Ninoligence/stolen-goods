from django.test import TestCase
from product.models import Product, ReviewRating
from category.models import Category
from django.contrib.auth import get_user_model


CustomUser = get_user_model()
class TestReviewRating(TestCase):

    def setUp(self):

        custom_user_1 = CustomUser.objects.create_user(
            email='customusertest1@unittest.com',
            username='usertest1',
            password='foo',
            first_name='User1',
            last_name='Test1'
        )

        custom_user_2 = CustomUser.objects.create_user(
            email='customusertest2@unittest.com',
            username='usertest2',
            password='foo',
            first_name='User2',
            last_name='Test1'
        )

        category = Category.objects.create(
            name='Jewellery',
            slug='jewellery',
            description='Oldest artefact used to show status',
            image='jewellery.png',
        )

        self.product = Product.objects.create(
            category_id=category.id,
            slug='blue-ocean-necklace',
            name='Blue Ocean Necklace',
            price=300000000,
            discounted_price=10000,
            stock=2
        )

        self.review_rating_1 = ReviewRating.objects.create(
            product_id=self.product.id,
            user_id=custom_user_1.id,
            subject='Test Review and Rating 1',
            review='Very elegant diamond',
            rating=4.5
        )

        self.review_rating_2 = ReviewRating.objects.create(
            product_id=self.product.id,
            user_id=custom_user_2.id,
            subject='Test Review and Rating 2',
            review='Very blue diamond',
            rating=4.5
        )

    def test_review_rating_creation(self):

        review_ratings = [self.review_rating_1, self.review_rating_2]

        for review_rating in review_ratings:
            self.assertTrue(isinstance(review_rating, ReviewRating))
            self.assertTrue(review_rating.status, True)
            self.assertEqual(review_rating.rating, 4.5)

        self.assertEqual(review_ratings[0].subject, 'Test Review and Rating 1')
        self.assertEqual(review_ratings[1].review, 'Very blue diamond')

    def test_product_average_review_and_review_count(self):

        test_product = self.product

        self.assertEqual(test_product.average_review(), 4.5)
        self.assertEqual(test_product.count_review(), 2)
