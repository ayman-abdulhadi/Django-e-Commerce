from django.urls import path
from . import views
# from django.utils.translation import gettext_lazy as _


app_name = 'payment'


urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('done/', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]
