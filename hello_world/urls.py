from django.contrib import admin
from django.urls import path,include
from app_1 import views as app_1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_1_views.index,name='index'),
    path('task/', include('app_1.urls')),
    path('account/', include('user_app.urls')),
    path('contact', app_1_views.contact,name='contact'),
    path('about', app_1_views.about,name='about')
]
