from django.urls import path
from . import views

app_name = 'my_shop'
urlpatterns = [
    path('orders/<int:year>/<int:pk>/', views.YearProducts.as_view(), name='yearly_orders'),
    path('orders/<int:year>/<int:month>/<int:pk>/', views.MonthProducts.as_view(), name='monthly_orders'),
    path('orders/<int:year>/<int:week>/<int:pk>/', views.WeekProducts.as_view(), name='weekly_orders'),
]
