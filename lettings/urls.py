from django.urls import path

from . import views


urlpatterns = [
    path('<int:letting_id>/', views.letting, name='letting')
]
