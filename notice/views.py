from rest_framework import generics, filters
from .models import Notice
from .serializers import NoticeSerializer


# GET /api/notice/   -> list notices (search, filter, sort, pagination)
# POST /api/notice/  -> create a notice
class NoticeListCreateView(generics.ListCreateAPIView):
    serializer_class = NoticeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "priority", "title"]

    def get_queryset(self):
        queryset = Notice.objects.all()
        category = self.request.query_params.get("category")
        is_active = self.request.query_params.get("is_active")

        if category:
            queryset = queryset.filter(category__iexact=category)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == "true")
        return queryset


# GET /api/notice/<id>/        -> get one notice
# PUT/PATCH /api/notice/<id>/  -> update a notice
# DELETE /api/notice/<id>/     -> delete a notice
class NoticeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    lookup_field = "id"
