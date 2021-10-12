from .decorators import query_debugger
from .models import Book, Store


@query_debugger
def book_list():

    queryset = Book.objects.all()

    books = []
    for book in queryset:
        books.append({'id': book.id, 'name': book.name,
                     'publisher': book.publisher.name})


@query_debugger
def book_list_select_related():

    queryset = Book.objects.select_related('publisher').all()

    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name,
                     'publisher': book.publisher.name})

@query_debugger
def book_list_prefetch_related():

    queryset = Book.objects.prefetch_related('publisher').all()

    books = []

    for book in queryset:
        books.append({'id': book.id, 'name': book.name,
                     'publisher': book.publisher.name})


@query_debugger
def store_list_prefetch_related():

    queryset = Store.objects.prefetch_related('books')

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})


@query_debugger
def store_list():

    queryset = Store.objects.all()

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})
