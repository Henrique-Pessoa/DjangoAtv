from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'equipamentos', EquipamentosViewSet, basename='equipamentos')
router.register(r'comentarios', ComentariosViewSet, basename='comentarios')
urlpatterns += router.urls

