from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime
from product.models import Product, Category
from mock import mock

from django.contrib.auth.models import User

def add_test_category():
    return Category.objects.create(name='test category name', description='test category description')

def add_product(name, description, price, days_offset):
    time = timezone.now() + datetime.timedelta(days=days_offset)
    category = add_test_category()

    # using mock for correct testing with option auto_now_add in field created_at
    with mock.patch('django.utils.timezone.now') as mock_now:
        mock_now.return_value = time
        product = Product.objects.create(name=name,
                                         description=description,
                                         price=price,
                                         created_at=time,
                                         category=category)
    return product

class Products24hViewTests(TestCase):

    def setUp(self):
        User.objects.create_user('test', 'test@gmail.com', 'pass')

    def test_view_without_login_user(self):
        """
        If user is not login, page should not be displayed, and it should be redirect to login page.
        """
        response = self.client.get(reverse('product:products24h'))
        self.assertEqual(response.status_code, 200)

    def test_view_with_login_user(self):
        """
        If user is login, page should be displayed.
        """
        self.client.login(username='test', password='pass')
        response = self.client.get(reverse('product:products24h'))
        self.assertEqual(response.status_code, 200)

    def test_view_without_products(self):
        """
        If user is login, page should be displayed.
        """
        self.client.login(username='test', password='pass')
        response = self.client.get(reverse('product:products24h'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['products24h_list'], [])

    def test_view_with_product_added_more_than_24_hours_ago(self):
        """
        If user is login, and there are product added more than 24 hours ago, it should not displayed it.
        """
        days_offset = -1
        self.client.login(username='test', password='pass')
        add_product(name='test product name', description='test product description',
                    price=100, days_offset=days_offset)
        response = self.client.get(reverse('product:products24h'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['products24h_list'], [])