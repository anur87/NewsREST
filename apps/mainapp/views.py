from django_filters.rest_framework import FilterSet, DjangoFilterBackend, DateFilter
from rest_framework import viewsets, filters, pagination

from .models import Category, News
from .serializers import CategorySerializer, NewsSerializer
 
    # ModelViewSet - обеспечивает все операции CRUD для модели Category.
    # queryset - модель для работы с данными.
    # serializer_class - класс для сериализации данных.
    

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с категориями новостей.

    list:
    Получение списка всех категорий.

    create:
    Создание новой категории.

    retrieve:
    Получение информации о конкретной категории.

    update:
    Обновление информации о конкретной категории.

    partial_update:
    Частичное обновление информации о конкретной категории.

    destroy:
    Удаление конкретной категории.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsPagination(pagination.PageNumberPagination):
    """
    PageNumberPagination - обеспечивает пагинацию для модели News.
    page_size - количество элементов на странице.
    page_size_query_param - параметр для указания количества элементов на странице.
    max_page_size - максимальное количество элементов на странице.
    """
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

class NewsFilter(FilterSet):
    """
    FilterSet - обеспечивает фильтрацию данных для модели News.
    category - фильтр по категории.
    is_published - фильтр по статусу публикации.
    start_date - фильтр по дате создания (больше или равно).
    end_date - фильтр по дате создания (меньше или равно).
    filters.DateFilter - обеспечивает фильтрацию по дате.
    """
    start_date = DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = News
        fields = ['category', 'start_date', 'end_date', 'is_published']


class NewsViewSet(viewsets.ModelViewSet):
    """
    filter_backends - обеспечивает фильтрацию данных для модели News.
    filterset_class - класс для фильтрации данных.
    search_fields - поля для поиска.
    pagination_class - класс для пагинации данных.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = NewsFilter
    search_fields = ['title', 'content', 'author', 'category__name']
    pagination_class = NewsPagination
