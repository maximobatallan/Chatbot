from django.urls import path
from mysite import views


urlpatterns = [
    path('', views.index, name='index'),
    path('formulario1.html', views.save_formulario, name='save_formulario'),
    path('webhook-whatsapp/', views.webhook_whatsapp, name='webhook_whatsapp'),
]









