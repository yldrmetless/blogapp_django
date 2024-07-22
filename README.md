# Blog Uygulaması

Bu proje, Django ve Django REST Framework kullanarak geliştirilmiş basit bir blog uygulamasıdır. Kullanıcılar blog yazıları oluşturabilir, bu yazıları kategorilere ayırabilir ve yorum yapabilirler. 

## İçindekiler

1. [Kurulum](#kurulum)
2. [Proje Yapılandırması](#proje-yapılandırması)
3. [API Endpoint'leri](#api-endpointleri)
4. [Örnek Kullanım](#ornek-kullanım)
5. [Yardım ve Destek](#yardim-ve-destek)

## Kurulum

### Gereksinimler

- Python 3.8 veya üstü
- Django 4.x
- Django REST Framework 3.x
- SQLite (varsayılan veritabanı)

### Adımlar

1. **Proje Klasörüne Gitme:**

   ```bash
   cd /path/to/your/project




# Sanal Ortamı Oluşturun ve Aktive Edin:
- Sanal ortam oluşturmak ve aktive etmek için:

- python -m venv env
- source env/bin/activate  # Linux/Mac
- env\Scripts\activate     # Windows


# Gerekli Paketleri Yükleyin:

- pip install -r requirements.txt


# Veritabanı Şemasını Uygulayın:

- Veritabanı şemasını oluşturmak için:

- python manage.py migrate


# Başlangıç Verilerini Yükleyin:

- Testlerinizde kullanılacak başlangıç verilerini yüklemek için:

- python manage.py loaddata initial_data.json



# Sunucuyu Başlatın:

- Geliştirme sunucusunu başlatmak için:

- python manage.py runserver

- Sunucu http://localhost:8000 adresinde çalışacaktır.



# API Endpoints

## Aşağıda mevcut API endpoint'leri ve kullanım detayları verilmiştir:

## Kategoriler


### Listeleme ve Oluşturma

### GET /api/categories/ - Tüm kategorileri listeleyin.

### POST /api/categories/ - Yeni bir kategori oluşturun.


### Görüntüleme, Güncelleme ve Silme

### GET /api/categories/<int:id>/ - Belirli bir kategoriyi görüntüleyin.

### PUT /api/categories/<int:id>/ - Belirli bir kategoriyi güncelleyin.

### DELETE /api/categories/<int:id>/ - Belirli bir kategoriyi silin.



## Yazılar

### Listeleme ve Oluşturma

### GET /api/posts/ - Tüm yazıları listeleyin.

### POST /api/posts/ - Yeni bir yazı oluşturun.


## Görüntüleme, Güncelleme ve Silme

### GET /api/posts/<int:id>/ - Belirli bir yazıyı görüntüleyin.

### PUT /api/posts/<int:id>/ - Belirli bir yazıyı güncelleyin.

### DELETE /api/posts/<int:id>/ - Belirli bir yazıyı silin.



## Yorumlar
## GET /api/posts/<int:post_id>/comments/ - Belirli bir yazıya ait yorumları listeleyin.

## POST /api/posts/<int:post_id>/comments/ - Belirli bir yazıya yeni bir yorum ekleyin.



## Yorumlar

## Get, Güncelleme ve Silme

## GET /api/comments/<int:id>/ - Belirli bir yorumu görüntüleyin.

## PUT /api/comments/<int:id>/ - Belirli bir yorumu güncelleyin.

## DELETE /api/comments/<int:id>/ - Belirli bir yorumu silin.


## Kullanıcı Yetkilendirmesi


## Yalnızca giriş yapmış kullanıcılar yazı ve yorum oluşturabilir, güncelleyebilir veya silebilir.
## Herkes (giriş yapmış veya yapmamış) yazıları ve yorumları görüntüleyebilir.


## Filtreleme ve Arama

## Yazılar kategorilere göre filtrelenebilir. Örneğin:

## GET /api/posts/?category=Web%20Geliştirme - Web Geliştirme kategorisine ait yazıları listeleyin.


## Yazılar ve yorumlar üzerinde arama yapılabilir. (Bu özellik, uygun API parametreleri ve sorguları eklenerek yapılabilir.)




## Sayfalama

## Yazılar ve yorumlar üzerinde sayfalama yapılabilir. (Bu özellik, uygun API parametreleri ve yapılandırmalar ile eklenebilir.)