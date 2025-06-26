from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cars/', views.cars, name="cars"),
    path('cars/<int:id>', views.car_view, name="car_view"),
    path('update_car_data/<int:id>', views.update_car_data, name="update_car_data"),
    path('car_exclude/<int:id>', views.car_exclude, name="car_exclude"),
    path('show_car/<int:id>', views.show_car, name="show_car"),
    path('all_cars/', views.all_cars, name="all_cars"),
]