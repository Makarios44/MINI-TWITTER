from rest_framework.pagination import PageNumberPagination

class TwitterLikePagination(PageNumberPagination):
    page_size = 20  # Define 20 itens por página
    page_size_query_param = 'page_size'  # Permite ajustar a paginação pela URL (opcional)
    max_page_size = 100  # Define um limite máximo para controle (opcional)

