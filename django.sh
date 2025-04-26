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