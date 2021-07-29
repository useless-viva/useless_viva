"""useless_viva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from question import views as Q
from result import views as R

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Q.home, name='home'),
    # path('choices/', Q.choices, name='choices'),
    path('choices/<int:pk>/', Q.choices, name='choices'),
    path('results/<int:pk>/', Q.results, name='results'),    
    path('popup/', Q.popup, name='popup'),
    path('gomin/', Q.gomin, name='gomin'),
    path('han/', Q.han, name='han'),
    path('sok/', Q.sok, name='sok'),
    path('question/', include('question.urls')),
    path('result/', include('result.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
