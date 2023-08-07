from django.urls import path, include
# from .views import CustomRegistrationView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/users/', CustomRegistrationView.as_view(), name='registration'),
]