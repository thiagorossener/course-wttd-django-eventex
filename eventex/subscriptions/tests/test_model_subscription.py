import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Thiago Rossener',
            cpf='12345678901',
            email='thiago@rossener.com',
            phone='12-981491771'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime.datetime)

    def test_str(self):
        self.assertEqual('Thiago Rossener', str(self.obj))
