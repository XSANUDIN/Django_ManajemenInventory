from django.db.models import Sum, Avg, F, Count
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Admin, Category, Supplier, Item
from .serializers import AdminSerializer, CategorySerializer, SupplierSerializer, ItemSerializer

# Create your views here.

# CRUD
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Views

# Ringkasan Stok
class StockSummary(APIView):
    def get(self, request):
        total_quantity = Item.objects.aggregate(total=Sum('quantity'))['total']
        total_value = Item.objects.aggregate(total=Sum(F('price') * F('quantity')))['total']
        avg_price = Item.objects.aggregate(avg=Avg('price'))['avg']
        return Response({
            "Stok Total" : total_quantity,
            "Total Nilai Stok" : total_value,
            "Harga Rata-Rata Barang" : avg_price,
        })
    
# Menampilkan Stok dibawah 10 unit
class LowStock(APIView):
    def get(self, request):
        low_stock = Item.objects.filter(quantity__lt=10)
        serializer = ItemSerializer(low_stock, many=True)
        return Response(serializer.data)
    
# Barang Berdasarkan Kategori
class ByCategory(APIView):
    def get(self, request, category_id):
        items = Item.objects.filter(category_id=category_id)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
# Ringkasan by Category
class CategorySummary(APIView):
    def get(self, request):
        summary = Category.objects.annotate(
            total_items=Count('items'),
            total_value=Sum(F('items__price') * F('items__quantity')),
            average_price=Avg('items__price')
        ).values('name', 'total_items', 'total_value', 'average_price')
        return Response(summary)
    
# Ringkasan supplier
class SupplierSummary(APIView):
    def get(self, request):
        summary = Supplier.objects.annotate(
            total_items=Count('items'),
            total_value=Sum(F('items__price') * F('items__quantity'))
        ).values('name', 'total_items', 'total_value')
        return Response(summary)
    
# Ringkasan Sistem
class SystemSummary(APIView):
    def get(self, request):
        total_items = Item.objects.count()
        total_value = Item.objects.aggregate(total=Sum(F('price') * F('quantity')))['total']
        total_categories = Category.objects.count()
        total_suppliers = Supplier.objects.count()
        return Response({
            "Jumlah Barang": total_items,
            "Nilai Stok": total_value,
            "Jumlah Kategori": total_categories,
            "Jumlah Pemasok": total_suppliers
        })