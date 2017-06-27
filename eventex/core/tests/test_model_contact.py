from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Thiago Rossener',
            slug='thiago-rossener',
            photo='http://hbn.link/tr-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='thiago@rossener.com')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE,
                                         value='12-98149-1771')
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='thiago@rossener.com')
        self.assertEqual('thiago@rossener.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Thiago Rossener',
            slug='henrique-bastos',
            photo='http://hbn.link/tr-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='thiago@rossener.com')
        s.contact_set.create(kind=Contact.PHONE, value='12-981491771')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['thiago@rossener.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['12-981491771']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
