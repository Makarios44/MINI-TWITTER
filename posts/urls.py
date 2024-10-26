from django.urls import path
from . import views

urlpatterns = [
    # Listar e criar posts
    path('posts/', views.PostCreateListView.as_view(), name='post-list'),

    # Recuperar, atualizar e excluir post
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='update-delete-post'),

    # Criar post via formulário (se for uma view baseada em função)
    path('create/', views.create_post_view, name='create_post'),

    # Exibir perfil do usuário
    path('profile/<str:username>/', views.profile_view, name='profile_view'),

    # Curtir post
    path('like/<int:post_id>/', views.like_post, name='like_post'),

    # Seguir usuário
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),

   
]
