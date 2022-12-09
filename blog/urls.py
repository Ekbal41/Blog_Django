from django.conf import settings
from django.conf.urls.static import static
from django.urls import  path
from . import views


urlpatterns = [
    
    path('', views.index, name='index' ),
    path('blog_detail/<str:slug>', views.blog_detail, name='blog_detail'),
    path('category/<str:slug>', views.category, name='category'),
    path('blog_archive/<int:year>/<int:month>', views.blog_archive, name='blog_archive'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
