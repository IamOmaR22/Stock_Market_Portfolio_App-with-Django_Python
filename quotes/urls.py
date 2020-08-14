from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('add_stock.html', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),  # 'delete/<stock_id>' we will use this format when we create a path without create a html file.We call it from add_stock.html
    path('delete_stock.html', views.delete_stock, name='delete_stock'),
]
