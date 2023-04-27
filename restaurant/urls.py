from django.urls import path

from restaurant import views

urlpatterns = [
    path('', views.index, name='home'),
    path('items/', views.MenuItemsView.as_view(), name='menu'),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view()),
]