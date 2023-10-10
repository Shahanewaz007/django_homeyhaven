from django.urls import path
from . import views
urlpatterns = [
    path('hotels/', views.see_hotels, name='hotels'),
    path('<slug:hotel_slug>/<int:hotel_id>/', views.hotel_detail, name='hotel_details'),
    path('', views.hotel_search, name='search')
]