from django.urls import path
from .views import CharacterListCreateView, CharacterDetailView, ComicListCreateView, ComicDetailView, ApiStatusUpdateView

urlpatterns = [
    path('characters/', CharacterListCreateView.as_view(), name='character-list-create'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('comics/', ComicListCreateView.as_view(), name='comic-list-create'),
    path('comics/<int:pk>/', ComicDetailView.as_view(), name='comic-detail'),
    path('api-status/', ApiStatusUpdateView.as_view(), name='api-status-update'),
]
