
# AŞAMA 1: Python OOP Kütüphane Sistemi
Bu proje, Python kullanarak Nesne Yönelimli Programlama (OOP) prensiplerine uygun bir **terminal tabanlı kütüphane sistemi** sağlar. Kitap ekleme, silme, güncelleme, arama ve listeleme işlemleri yapılabilir. Veriler `library.json` dosyasında kalıcı olarak saklanır.

## Özellikler

* Kitap ekleme (ISBN, kitap adı ve yazar adı zorunlu)
* ISBN 13 haneli ve sadece rakam olmalı
* ISBN duplicate kontrolü
* Kitap silme (ISBN ile)
* Kitap güncelleme (ISBN ile)
* Kitap arama (ISBN ile)
* Kitap listeleme (ISBN `978-XXXXXXXXXXX` formatında)
* Tüm veriler JSON dosyasında saklanır
* Pytest ile test edilmiş fonksiyonlar

## Kurulum

Pycharm platformunda oluşturulmuştur. 
1. Python 3.7+ kurulu olmalı.
2. Proje klasörünü indirin veya klonlayın:

   ```bash
   git clone <repo_link>
   cd python_oop_kutuphane
   ```
3. Gereken paketleri yükleyin (opsiyonel, proje için standart Python yeterli):

   ```bash
   pip install pytest
   ```

## Kullanım

1. Uygulamayı başlatın:

   ```bash
   python main.py
   ```

2. Menü üzerinden seçim yapın:

   ```
   1. Kitap ekle
   2. Kitapları listele
   3. Kitap ara (ISBN ile)
   4. Kitap sil (ISBN ile)
   5. Kitap güncelle (ISBN ile)
   6. Çıkış
   ```

3. Bilgileri girerken:

   * ISBN 13 haneli ve sadece rakamlardan oluşmalı.
   * Kitap adı ve yazar adı boş bırakılamaz.
   * ISBN duplicate ise uyarı verilir.

## Testler

Projede testler `pytest` ile yazılmıştır. Çalıştırmak için terminalde:

```bash
pytest test_library.py
```
## Test Sonuçları

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
