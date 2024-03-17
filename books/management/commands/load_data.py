import csv
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Load data from a CSV file into the Book model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                book = Book.objects.create(
                    title=row['book_title'],
                    author=row['author_name'],
                    media_type=row['book_media_type'],
                    gutenberg_id=row['book_gutenberg_id'],
                    download_count=row['book_download_count'],
                    bookshelf_name=row['bookshelf_name'],
                    mime_type=row['format_mime_type'],
                    url=row['format_url'],
                    language=row['language_code'],
                    subject=row['subject_name']
                )
                self.stdout.write(self.style.SUCCESS(f'Loaded book: {book.title}'))
