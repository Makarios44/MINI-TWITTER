# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import api_root, UserListView 
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api/users/', include('users.urls')),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', api_root, name='api-root'),  # Rota para api_root
    path('api/users/', UserListView.as_view(), name='user-list'),

]
