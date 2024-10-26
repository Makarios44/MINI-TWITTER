from posts.models import Post, Follow
from rest_framework import generics
from posts.serializers import PostSerializer, FollowSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from posts.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


class PostCreateListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Visualizar, atualizar e deletar posts
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Visualizar seguidores e seguidos de um usuário
class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user_to_follow = User.objects.get(id=self.request.data.get('user_id'))
        serializer.save(follower=self.request.user, following=user_to_follow)

@login_required
@api_view(['POST'])
def create_post_view(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@login_required   
@api_view(['GET'])
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@login_required
def like_post(request, post_id):
    """Função para curtir/descurtir um post."""
    post = get_object_or_404(Post, id=post_id)
    
    # Verifica se o usuário já curtiu o post
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Descurtir
        liked = False
    else:
        post.likes.add(request.user)  # Curtir
        liked = True
    
    # Retorna uma resposta JSON com o status da curtida
    return JsonResponse({'liked': liked, 'total_likes': post.likes.count()})

@login_required
def follow_user(request, user_id):
    """Função para seguir/parar de seguir um usuário."""
    target_user = get_object_or_404(User, id=user_id)
    
    # Verifica se o usuário já está seguindo o usuário alvo
    if Follow.objects.filter(follower=request.user, following=target_user).exists():
        # Se já segue, remove o relacionamento
        Follow.objects.filter(follower=request.user, following=target_user).delete()
        following = False
    else:
        # Caso contrário, cria o relacionamento de seguir
        Follow.objects.create(follower=request.user, following=target_user)
        following = True
    
    # Retorna uma resposta JSON com o status do relacionamento
    return JsonResponse({'following': following})
