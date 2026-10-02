from django.urls import path
from .views import NoticeListCreateView, NoticeDetailView

urlpatterns = [
    path("api/notice/", NoticeListCreateView.as_view()),
    path("api/notice/<int:id>/", NoticeDetailView.as_view()),
]
