from django.urls import path

from . import views

# namespace for current app
app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('new_item/', views.new_item, name='new_item'),
    path('<int:pk>/delete_item/', views.delete_item, name='delete_item'),
    path('<int:pk>/edit_item/', views.edit_item, name='edit_item'),
]