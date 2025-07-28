from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.user_auth, name="user"),
    path('user/pre-register/', views.user_pre_register, name="user_pre_register"),
    path('user/finalize/', views.user_finalize_register, name="user_finalize_register"),
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/informations/<int:user_id>', views.user_informations, name="user_informations"),
    path('user/forgot-password/', views.user_forgot_password, name='user_forgot_password'),
    path('user/reset-password/', views.user_reset_password, name='user_reset_password'),
    path('user/user_cars/<int:user_id>', views.user_cars, name="user_cars"),
    path('cars/', views.cars, name="cars"),
    path('cars/<int:id>', views.car_view, name="car_view"),
    path('update_car_data/<int:id>', views.update_car_data, name="update_car_data"),
    path('car_exclude/<int:id>', views.car_exclude, name="car_exclude"),
    path('show_car/<int:id>', views.show_car, name="show_car"),
    path('all_cars/', views.all_cars, name="all_cars"),
    path('car_main_edit/<int:id>', views.car_main_edit, name="car_main_edit"),
]