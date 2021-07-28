from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from result import views as R

urlpatterns = [
    path('<str:id>/',R.detail, name="detail"),
    path('post/', R.make_post, name="make_post"),
    path('update/<str:id>/', R.update, name="update"),
    path('delete/<str:id>/', R.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
