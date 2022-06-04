from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [ 
    path('',views.home,name='home'),
    path('blog',views.blog,name='blog'),
    path('detail/<slug>',views.detail,name='detail'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('success',views.success,name='success'),
    path('detail/<slug>',views.detail,name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)