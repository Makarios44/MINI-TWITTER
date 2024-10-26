from rest_framework import generics
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from rest_framework.generics import ListAPIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# View para registro de novos usuários via API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# View para visualizar o perfil do usuário autenticado via API
class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# View para login de usuário
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')  # Redireciona ao perfil se o usuário já está logado
    # Implementação do login depende do front-end, ou pode usar login API endpoint
    return Response({"detail": "Página de login"}, status=status.HTTP_200_OK)

# View para logout de usuário
def logout_view(request):
    logout(request)
    return Response({"detail": "Logout realizado com sucesso."}, status=status.HTTP_200_OK)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format),
        # Adicione outros endpoints conforme necessário
    })