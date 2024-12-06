from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(
            title="Test Book",
            author="Author Name",
            publication_date="2024-12-06",
            isbn="1234567890123"
        )

    def test_book_creation(self):
        book = Book.objects.get(isbn="1234567890123")
        self.assertEqual(book.title, "Test Book")
