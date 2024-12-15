from django.contrib.auth.views import LoginView
from django.urls import path
from accounts_app import views
from django.conf import settings 
from django.conf.urls.static import static

app_name = 'accounts_app'

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name='profile_view'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)