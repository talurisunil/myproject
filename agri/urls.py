from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),
    path('', include('about_us.urls')),
    path('', include('how_it_works.urls')),
    #path('', include('agri_properties.urls')),
    path('', include('technology.urls')),
    #path('', include('product.urls')),
    #path('', include('Resource_center.urls')),
    #path('', include('accounts.urls')),

]
