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