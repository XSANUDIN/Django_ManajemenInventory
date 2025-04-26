
# Project UTS Pemrograman Sisi Server
Membuat **BACKEND SISTEM MANAJEMEN INVENTORY**.

## Deskripsi
Membuat aplikasi backend untuk mengelola persediaan pada toko. Aplikasi ini harus mendukung pengelolaan barang dan kategori, serta pencatatan data pemasok.

Aplikasi ini dibangun menggunakan Web Framework Django dan menggunakan PostgreSQL untuk database serta Menggunakan Docker untuk containerisasi seluruh sistem.


## Alur Pengerjaan
- **Instalasi [Docker](https://docs.docker.com/) dan [Python](https://www.python.org/doc/)**
- **Instal [Django](https://docs.djangoproject.com/en/5.2/)**

  ```bash
   pip install django
  ```

- **Membuat Project baru**
  ```bash
  django-admin startproject "uts_pss" 
  ```

- **Membuat App**
  ```bash
  django-admin manage.py startapp "manajemen_inventory"
  ```

- **Konfigurasi App**
  ```bash
  membuat requirements
  ```
  Edit settings.py
  ```bash
  import os
  ....
  INSTALLED_APPS = [
    ....
    'manajemen_inventory',
    'rest_framework',
  ]
  
  ...

  DATABASES = {
  'default': {
      'ENGINE': os.environ.get('DB_DRIVER', 'django.db.backends.postgresql'),
      'NAME': os.environ.get('PG_DB', 'postgres'),
      'USER': os.environ.get('PG_USER', 'postgres'),
      'PASSWORD': os.environ.get('PG_PASSWORD', 'postgres'),
      'HOST': os.environ.get('PG_HOST', 'localhost'),
      'PORT': os.environ.get('PG_PORT', '5432')
  }
  ```
  
- **Membuat Models** sesuai dengan tabel database yang telah diberikan.
- **Membuat Serializers** untuk merubah data menjadi format JSON.
- **Membuat urls** untuk menghubungkan alamat web (endpoint) ke fungsi view.
  ``` bash
  from django.urls import path
  from .views import (
      ItemList, CategoryList, SupplierList, StockSummary,
      LowStock, ByCategory, CategorySummary, SupplierSummary,
      SystemSummary
  )

  urlpatterns = [
      # Create Read
      path('items/', ItemList.as_view(), name='item'),
      path('category/', CategoryList.as_view(), name='category'),
      path('suppliers/', SupplierList.as_view(), name='supplier'),

      # Laporan
      path('summary/stock/', StockSummary.as_view(), name='stock-summary'),
      path('items/low-stock/', LowStock.as_view(), name='low-stock'),
      path('items/category/<int:category_id>/', ByCategory.as_view(), name='items-by-category'),
      path('summary/category/', CategorySummary.as_view(), name='category-summary'),
      path('summary/supplier/', SupplierSummary.as_view(), name='supplier-summary'),
      path('summary/system/', SystemSummary.as_view(), name='system-summary'),
  ]
  ```

  ``` bash
  Menambahkan urls dari manajemen_inventory ke uts_pss
  
  urlpatterns = [
    ...
    path('api/', include('manajemen_inventory.urls')),
  ]
  ```
- **Membuat views** untuk mengatur logika aplikasi untuk memproses permintaan (request) dan menghasilkan respons.
- **Membuat script django.sh** untuk mempermudah hal seperti migrasi dan seeding
  ``` bash
  #!/bin/bash
  echo "Create_Migrations"
  python manage.py makemigrations manajemen_inventory
  echo "==========================================="

  echo "Migrate..."
  python manage.py migrate
  echo "==========================================="

  echo "Seeding admin data..."
  python manage.py loaddata seeder/admin_seed.json
  echo "==========================================="

  echo "Seeding category data..."
  python manage.py loaddata seeder/category_seed.json
  echo "==========================================="

  echo "Seeding supplier data..."
  python manage.py loaddata seeder/supplier_seed.json
  echo "==========================================="

  echo "Seeding item data..."
  python manage.py loaddata seeder/item_seed.json
  echo "==========================================="

  echo "Start Server"
  python manage.py runserver 0.0.0.0:8080
  ```
- **Membuat Dockerfile dan docker-compose.yml**
- **Run Project**
  ```bash
    docker-compose up --build
  ```
- **Test Aplikasi menggunakan Postman atau Django REST Framework**
  ![DRF](https://drive.google.com/file/d/1tddUB0-TmX6Tp7U0GLilhZ7flM6DwJHT/view?usp=sharing)
  ![Postman](https://drive.google.com/file/d/10tW-SetYxYzFeJER4s-peXXzMOCD6hGh/view?usp=sharing)




## URL
url endpoint untuk aplikasi ini
``` bash
localhost:8080/api/items
localhost:8080/api/category
localhost:8080/api/supplier

localhost:8080/api/summary/stock
localhost:8080/api/items/low-stock
localhost:8080/api/items/category/{id}
localhost:8080/api/summary/category
localhost:8080/api/summary/supplier
localhost:8080/api/summary/system
```