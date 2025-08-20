from library import Library

def main():
    library = Library()

    while True:
        print("\n=== Kütüphane Sistemi ===")
        print("1. Kitap ekle")
        print("2. Kitapları listele")
        print("3. Kitap ara (ISBN ile)")
        print("4. Kitap sil (ISBN ile)")
        print("5. Kitap güncelle (ISBN ile)")
        print("6. Çıkış")

        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            while True:
                isbn = input("ISBN (13 haneli, sadece rakam): ").strip()
                title = input("Kitap adı: ").strip()
                author = input("Yazar adı: ").strip()
                try:
                    library.add_book(title, author, isbn)
                    print("✅ Kitap başarıyla eklendi.")
                    break
                except ValueError as e:
                    print(f"⚠️ Hata: {e}")
                    print("Lütfen bilgileri tekrar girin.")

        elif secim == "2":
            books_list = library.list_books()
            if not books_list:
                print("📚 Kütüphanede kitap yok.")
            else:
                for book_str in books_list:
                    print(book_str)

        elif secim == "3":
            isbn = input("Aranacak ISBN: ").strip()
            book = library.find_book(isbn)
            if book:
                print("📖 Kitap Bulundu:")
                print(book)
            else:
                print("❌ Kitap bulunamadı.")

        elif secim == "4":
            isbn = input("Silinecek ISBN: ").strip()
            library.remove_book(isbn)

        elif secim == "5":
            # ISBN doğrulama döngüsü
            while True:
                isbn = input("Güncellenecek ISBN (13 haneli rakam): ").strip()
                if not isbn or not isbn.isdigit() or len(isbn) != 13:
                    print("⚠️ ISBN boş olamaz. 13 haneli rakamdan oluşan ISBN numarasını giriniz.")
                    continue

                existing_book = library.find_book(isbn)
                if not existing_book:
                    print("❌ Bu ISBN'ye ait kayıt bulunmamaktadır! Lütfen tekrar girin.")
                    continue

                # ISBN bulundu, kitap adı ve yazar adı sor
                while True:
                    new_title = input("Yeni kitap adı: ").strip()
                    new_author = input("Yeni yazar adı: ").strip()
                    if not new_title or not new_author:
                        print("⚠️ Kitap adı ve yazar adı boş olamaz. Lütfen tekrar girin.")
                        continue
                    library.update_book(isbn, new_title=new_title, new_author=new_author)
                    print("✅ Kitap başarıyla güncellendi.")
                    break
                break

        elif secim == "6":
            print("Çıkış yapılıyor...")
            break

        else:
            print("⚠️ Geçersiz seçim! Tekrar deneyin.")

if __name__ == "__main__":
    main()
