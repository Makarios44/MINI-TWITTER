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

# View for registering new users via API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

#View to view the profile of the user authenticated via API
class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')  
    # this will need a front-end interface
    return Response({"detail": "Página de login"}, status=status.HTTP_200_OK)

# User logout view 
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
        #  endpoints
    })