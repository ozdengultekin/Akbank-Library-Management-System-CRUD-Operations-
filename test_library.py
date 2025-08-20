import os
import pytest
from library import Library, Book

TEST_FILE = "test_library.json"

@pytest.fixture
def clean_library():
    # Testler için temiz bir kütüphane oluştur
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    lib = Library(filename=TEST_FILE)
    yield lib
    # Test sonrası dosyayı temizle
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_book_success(clean_library):
    clean_library.add_book("Ulysses", "James Joyce", "9780199535675")
    assert len(clean_library.books) == 1
    book = clean_library.books[0]
    assert book.title == "Ulysses"
    assert book.author == "James Joyce"
    assert book.isbn == "9780199535675"

def test_add_book_duplicate_isbn(clean_library):
    clean_library.add_book("Ulysses", "James Joyce", "9780199535675")
    clean_library.add_book("Another Book", "Another Author", "9780199535675")
    # İkinci ekleme yapılmamalı
    assert len(clean_library.books) == 1

def test_add_book_empty_fields(clean_library):
    with pytest.raises(ValueError):
        Book("", "Author", "9780199535675")
    with pytest.raises(ValueError):
        Book("Title", "", "9780199535675")
    with pytest.raises(ValueError):
        Book("Title", "Author", "")

def test_add_book_invalid_isbn(clean_library):
    with pytest.raises(ValueError):
        Book("Title", "Author", "123")  # Kısa ISBN
    with pytest.raises(ValueError):
        Book("Title", "Author", "978-0199535675")  # Hatalı karakter

def test_list_books(clean_library):
    clean_library.add_book("Book1", "Author1", "9781111111111")
    clean_library.add_book("Book2", "Author2", "9782222222222")
    books_list = clean_library.list_books()
    assert len(books_list) == 2
    assert "Book1" in books_list[0]
    assert "Book2" in books_list[1]

def test_find_book(clean_library):
    clean_library.add_book("Book1", "Author1", "9781111111111")
    book = clean_library.find_book("9781111111111")
    assert book is not None
    assert book.title == "Book1"

    book_none = clean_library.find_book("9780000000000")
    assert book_none is None

def test_remove_book(clean_library):
    clean_library.add_book("Book1", "Author1", "9781111111111")
    result = clean_library.remove_book("9781111111111")
    assert result is True
    assert len(clean_library.books) == 0

    result_none = clean_library.remove_book("9780000000000")
    assert result_none is False

def test_update_book(clean_library):
    clean_library.add_book("OldTitle", "OldAuthor", "9782222222222")
    result = clean_library.update_book("9782222222222", new_title="NewTitle", new_author="NewAuthor")
    assert result is True
    book = clean_library.find_book("9782222222222")
    assert book.title == "NewTitle"
    assert book.author == "NewAuthor"

    result_none = clean_library.update_book("9780000000000", new_title="X", new_author="Y")
    assert result_none is False


"""
=============================================================================================== test session starts ================================================================================================
platform darwin -- Python 3.12.2, pytest-7.4.4, pluggy-1.0.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/ozden/python_oop_kutuphane
plugins: dash-3.0.0, langsmith-0.3.18, anyio-4.2.0
collected 8 items                                                                                                                                                                                                  

test_library.py::test_add_book_success PASSED                                                                                                                                                                [ 12%]
test_library.py::test_add_book_duplicate_isbn PASSED                                                                                                                                                         [ 25%]
test_library.py::test_add_book_empty_fields PASSED                                                                                                                                                           [ 37%]
test_library.py::test_add_book_invalid_isbn PASSED                                                                                                                                                           [ 50%]
test_library.py::test_list_books PASSED                                                                                                                                                                      [ 62%]
test_library.py::test_find_book PASSED                                                                                                                                                                       [ 75%]
test_library.py::test_remove_book PASSED                                                                                                                                                                     [ 87%]
test_library.py::test_update_book PASSED                                                                                                                                                                     [100%]

================================================================================================ 8 passed in 0.01s =================================================================================================
(base) ozden@Ozden-MacBook-Air python_oop_kutuphane % 



"""