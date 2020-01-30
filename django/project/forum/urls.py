from django.urls import path
from .views import GroupListView, GroupCreateView, GroupDeleteView, GroupDetailView
from . import views

urlpatterns = [
    path('', views.home, name='forum-home'),
    path('groups/', GroupListView.as_view(), name='forum-groups'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('groups/new/', GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
]