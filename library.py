import json
import os
import uuid


import uuid

class Book:
    def __init__(self, title: str, author: str, isbn: str, id: str = None):
        if not title or not author or not isbn:
            raise ValueError("Kitap adı, yazar adı ve ISBN boş olamaz.")
        if not isbn.isdigit() or len(isbn) != 13:
            raise ValueError("ISBN 13 haneli ve sadece rakamlardan oluşmalıdır. Örn: 9780199535675")
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        formatted_isbn = f"{self.isbn[:3]}-{self.isbn[3:]}"
        return f"{self.title} by Kitap yazarı: {self.author} ISBN: {formatted_isbn}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }



class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """library.json dosyasından kitapları yükler. Geçersiz veri varsa atlar."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                    books_data = json.load(f)
                    books = []
                    for book_dict in books_data:
                        try:
                            book = Book(**book_dict)
                            books.append(book)
                        except ValueError:
                            print(f"⚠️ Geçersiz veri atlandı: {book_dict.get('isbn')}")
                    return books
                except json.JSONDecodeError:
                    return []
        return []  # Boş dosya veya yoksa boş liste döndür

    def save_books(self):
        """Tüm kitapları JSON dosyasına kaydeder."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, title, author, isbn):
        """Yeni kitap ekler. ISBN zaten varsa eklemez."""
        for book in self.books:
            if book.isbn == isbn:
                print("⚠️ Bu kitap zaten kayıtlıdır.")
                return
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        print(f"✅ Kitap eklendi: {title} by {author}")

    def list_books(self):
        """Tüm kitapları liste olarak döndürür."""
        if not self.books:  # Eğer liste boşsa
            return []
        return [str(book) for book in self.books]

    def find_book(self, isbn: str):
        """ISBN ile kitabı bulur."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book(self, isbn: str):
        """ISBN ile kitabı siler."""
        book_to_remove = self.find_book(isbn)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print(f"✅ ISBN {isbn} ile kitap silindi.")
            return True
        print("⚠️ Kitap bulunamadı.")
        return False

    def update_book(self, isbn: str, new_title: str = None, new_author: str = None):
        """ISBN ile kitabı günceller."""
        book_to_update = self.find_book(isbn)
        if book_to_update:
            if new_title and new_title.strip():
                book_to_update.title = new_title.strip()
            if new_author and new_author.strip():
                book_to_update.author = new_author.strip()
            self.save_books()
            print(f"✅ ISBN {isbn} ile kitap güncellendi.")
            return True
        print("⚠️ Kitap bulunamadı.")
        return False