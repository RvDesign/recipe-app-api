from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@vandoeland.nl'
        password = 'Test123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@vanDoeland.nl'
        user = get_user_model().objects.create_user(email, 'test234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_normalized_2(self):
        """Test the email for a new user is user still in uppercase"""
        email = 'TEST@vandoeland.nl'
        user = get_user_model().objects.create_user(email, 'test234')

        self.assertEqual(user.email, email)

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises errror"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(" ", 'test123')
            get_user_model().objects.create_user("", 'test123')
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@vandoeland.nl',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
