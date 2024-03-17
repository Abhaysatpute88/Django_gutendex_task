from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Book
from .serializers import BookSerializer






class BookListView(APIView):
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20

    def get(self, request):
        queryset = Book.objects.all()

        filters = {}

        book_ids = request.query_params.getlist('book_id')
        if book_ids:
            filters['gutenberg_id__in'] = book_ids

        languages = request.query_params.getlist('language')
        if languages:
            filters['language__in'] = languages

        mime_types = request.query_params.getlist('mime_type')
        if mime_types:
            filters['mime_type__in'] = mime_types

        topics = request.query_params.getlist('topic')
        if topics:
            topic_query = Q()
            for topic in topics:
                topic_query |= Q(subject__icontains=topic) | Q(bookshelf_name__icontains=topic)
            queryset = queryset.filter(topic_query)

        authors = request.query_params.getlist('author')
        if authors:
            author_query = Q()
            for author in authors:
                author_query |= Q(author__icontains=author)
            queryset = queryset.filter(author_query)

        titles = request.query_params.getlist('title')
        if titles:
            title_query = Q()
            for title in titles:
                title_query |= Q(title__icontains=title)
            queryset = queryset.filter(title_query)

        if filters:
            queryset = queryset.filter(**filters)

        queryset = queryset.order_by('-download_count', 'id')

        # Pagination
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        
        serializer = BookSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
