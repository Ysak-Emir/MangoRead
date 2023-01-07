from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from mango.models import Card, Review
from mango.serializers import CardSerializer, ReviewSerializer, ReviewCreateSerializer, CardDetailSerializer


class ReviewPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class CardPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination


class ReviewCreateAPIView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response({"post": serializer.data})


class CardAPIView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'year']
    # search_fields = ('title',)



    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        return Card.objects.all()

    def get(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        paginator = CardPagination()
        paginator.page_size = 12
        result_page = paginator.paginate_queryset(filtered_queryset, request)
        serializer = CardSerializer(result_page, many=True)
        return paginator.get_paginated_response({
            "card": serializer.data
        })


class CardDetailAPIView(APIView):

    def get(self, request, id):
        try:
            queryset = Card.objects.get(id=id)
        except:
            return Response(data={'errors': 'Card not found'}, status=404)
        serializer = CardDetailSerializer(queryset)
        return Response({
            "card": serializer.data
        })
