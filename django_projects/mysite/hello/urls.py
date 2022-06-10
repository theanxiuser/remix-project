from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('template', TemplateView.as_view(template_name='hello/main.html')),
    path('', views.sessfun),
    path('cookie', views.cookie),
]