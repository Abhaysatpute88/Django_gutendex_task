from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITest(APITestCase):

    def test_get_books_with_filters(self):
        url = reverse('book-list') + '?language=en&topic=child&author=Dickens&title=oliver'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_books = Book.objects.filter(language='en', author__icontains='Dickens', title__icontains='oliver')
        expected_books_count = expected_books.count()
        self.assertEqual(len(response.data['results']), expected_books_count)
        response_titles = {book['title'] for book in response.data['results']}
        expected_titles = {book.title for book in expected_books}
        self.assertEqual(response_titles, expected_titles)


    def test_pagination(self):
        for i in range(21):
            Book.objects.create(title=f"Book {i+3}", author=f"Author {i+3}", language="English", download_count=50)
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 20)
        self.assertIsNotNone(response.data['next'])
