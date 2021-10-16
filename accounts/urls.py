from django.urls import path
from .views import RegisterPageView, LoginPageView,SingOutview
app_name = 'registerpage'
urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', SingOutview.as_view(), name='logout_user'),
    path('login/', LoginPageView.as_view(), name='login'),
]
