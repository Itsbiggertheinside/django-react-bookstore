from rest_framework import viewsets, mixins, serializers, permissions, filters, generics, status
from rest_framework.response import Response

from .models import Book, Order, OrderItem
from .serializers import BookSerializer, BookDetailSerializer, OrderItemSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly
from .pagination import BookHomePagination, BookCategoryPagination


# Create your views here.
class BookListHomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.select_related('author').prefetch_related('details__comments__owner__user').all()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter, )
    search_fields = ('category',)
    pagination_class = BookHomePagination


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.select_related('customer__user').all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, is_completed=False)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderItemViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = OrderItem.objects.select_related('order__customer__user', 'item__author').all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        customer = self.request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, is_completed=False)
        serializer.save(order=order)
