from django.contrib import admin
from django.urls import path, include  
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from app import views
import django.contrib.auth
from app.views import CustomLogoutView
from django.conf import settings
from django.conf.urls.static import static   
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#urlpatterns = [
  #  path('admin/', admin.site.urls),  
  # path('accounts/login/', django.contrib.auth.views.LoginView.as_view(template_name='registration/login.html'),name='login'),
  #  path('accounts/logout/',django.contrib.auth.views.LogoutView.as_view(next_page='inicio'), name='logout'),
  #  path('accounts/register/', views.register, name='register'),
  #  path('app/', include('app.urls')),  
  #  path('', views.inicio, name='inicio') ,
  #  path('', RedirectView.as_view(url='app/', permanent=True)),
  #  path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#]
urlpatterns = [
    path('admin/', admin.site.urls),

    # Login, logout y registro
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/register/', views.RegistroView.as_view(), name='register'),
    # URLs de la app principal
    path('app/', include('app.urls')),

    # Página de inicio
    path('', views.inicio, name='inicio'),

    ]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
