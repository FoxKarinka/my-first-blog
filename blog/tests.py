from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from .models import Post


class PostListTests(TestCase):
    def setUp(self):
        self.author = get_user_model().objects.create_user(username='author')

    def test_only_published_posts_are_displayed(self):
        Post.objects.create(
            author=self.author,
            title='Published story',
            text='A story about a cat.',
            published_date=timezone.now(),
        )
        Post.objects.create(
            author=self.author,
            title='Draft story',
            text='Not ready to publish.',
        )

        response = self.client.get(reverse('post_list'), HTTP_HOST='localhost')

        self.assertContains(response, 'Published story')
        self.assertNotContains(response, 'Draft story')
