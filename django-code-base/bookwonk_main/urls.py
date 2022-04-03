"""bookwonk_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import logout
from django.urls import path
from members import views as memberView
from books import views as bookView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=memberView.indexView, name='index'),
    path('login/', view=memberView.loginView, name='login'),
    path('logout/', view=memberView.logoutView, name='logout'),
    path('signup/', view=memberView.signupView, name='signup'),
    path('collection/', view=bookView.collectionView, name='collection'),
    path('book/<bookName>', view=bookView.readerView, name='reader')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
