from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "favigen"

app_name = "favigen"

urlpatterns = [
    path("", views.home_page, name='home'),
<<<<<<< HEAD
    path("signup/", views.signup, name='register'),
    path("login/", views.login, name='login'),
    path('upload/', views.upload,name='upload'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path("signup/", views.signup_page, name='signup'),
    path("login/", views.login_page, name='login')
]
>>>>>>> 0fb436d51a861efdb8fa5c00db68af6f5e1be7f2
