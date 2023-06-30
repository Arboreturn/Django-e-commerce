from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('<category_slug>/items/<int:pk>/',views.detail,name='detail'),
    path('category/<slug:category_slug>/',views.category_show, name="category_show"),
    path('product/',views.product,name='product'),
    path('categories/',views.product,name='category'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)