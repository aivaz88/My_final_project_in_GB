from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('recovery_password/', views.recovery_password, name='recovery_password'),
    path('categories/<str:category>/', views.get_by_categories, name='categories'),
    path('create_retreat/', views.create_retreat, name='create_retreat'),
    path('retreat/<int:retreat_id>/', views.get_retreat_card, name='retreat'),
    path('booking/<int:retreat_id>', views.create_booking, name='booking'),
    path('organizer/<int:user_id>', views.get_organizer_card, name='organizer'),
    path('account/', views.get_user_card, name='account'),
    path('edit_profile/', views.edit_user_card, name='edit_profile'),
    path('my_bookings/', views.get_my_bookings, name='my_bookings'),
    path('payments/', views.get_payments, name='payments'),
    path('feedback/<int:retreat_id>', views.create_feedback, name='feedback'),
    path('favorites/', views.get_favorites, name='favorites'),
]
