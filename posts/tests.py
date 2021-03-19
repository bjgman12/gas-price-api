from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Posts

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Posts.objects.create(
            author = testuser1,
            station = 'GasGo',
            price = 9.99
        )
        test_post.save()

    def test_post_content(self):
        post = Posts.objects.get(id=1)
        actual_author = str(post.author)
        actual_station = str(post.title)
        actual_price = str(post.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'GasGo')
        self.assertEqual(actua;_price, 9.99')