from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@vandoeland.nl', password='test1234'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test the tag string represneation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Komkommer'
        )

        self.assertEqual(str(ingredient), ingredient.name)
