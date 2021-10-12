"""
Seeds the database
"""
import random
from django.core.management.base import BaseCommand
from book.models import Publisher, Store, Book


class Command(BaseCommand):
    """
    This command is for inserting Publisher, Book, Store into database.
    Insert 5 Publishers, 100 Books, 10 Stores.
    """
    publishers_count = 10
    books_count_per_store_per_publisher = 100000
    stores_count = 10

    def handle(self, *args, **options):
        """
        Overriding the handle method
        """
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        publishers = [Publisher(name=f"Publisher{index}")
                      for index in range(self.publishers_count)]
        Publisher.objects.bulk_create(publishers)

        counter = 0
        books = []
        for publisher in Publisher.objects.all():
            for i in range(self.books_count_per_store_per_publisher):
                counter = counter + 1
                books.append(Book(name=f"Book{counter}", price=random.randint(
                    50, 300), publisher=publisher))

        Book.objects.bulk_create(books)

        books = list(Book.objects.all())
        for i in range(self.stores_count):
            temp_books = [books.pop(0) for i in range(
                self.books_count_per_store_per_publisher)]
            store = Store.objects.create(name=f"Store{i+1}")
            store.books.set(temp_books)
            store.save()
