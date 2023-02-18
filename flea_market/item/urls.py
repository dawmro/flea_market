from django.urls import path

from . import views

# namespace for current app
app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('new_item/', views.new_item, name='new_item'),
]