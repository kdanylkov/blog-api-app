from django.test import TestCase

from .models import Post
from django.contrib.auth import get_user_model


class BlogTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
                username='test_user',
                email='test@email.com',
                password='secret'
                )
        cls.post = Post.objects.create(
                author=cls.user,
                title='A good title',
                body='Nice body content'
                )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'test_user')
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(str(self.post), 'A good title')
