from .serializers import *
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def get_users(self, request):
        try:
            users = CustomUser.objects.all()
            serializer = CustomUserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(status=404, data=str(e))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        refresh = RefreshToken.for_user(serializer.instance)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        response_data = {
            'user': {
                'id': serializer.instance.id,
                'funcao': serializer.instance.funcao,
            },
            'tokens': tokens
        }
        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=201, headers=headers)
    
class EquipamentosViewSet(viewsets.ModelViewSet):
    queryset = Equipamentos.objects.all()
    serializer_class = EquipamentosSerializer
    permission_classes = (IsAuthenticated,)

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = (IsAuthenticated,)