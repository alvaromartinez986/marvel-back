from rest_framework import generics
from .models import Character, Comic
from .serializers import CharacterSerializer, ComicSerializer, ApiStatusSerializer
from .models import ApiStatus
from rest_framework.response import Response
from django.http import Http404




class CharacterListCreateView(generics.ListCreateAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Character.objects.all()

        # Check if a 'name' parameter is present in the request
        name = self.request.query_params.get('name', None)
        if name is not None:
            # Filter the queryset by name
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Http404:
            # Handle the case where no characters match the filter
            return Response({"detail": "No characters found with the specified filter."}, status=status.HTTP_404_NOT_FOUND)

class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class ComicListCreateView(generics.ListCreateAPIView):
    serializer_class = ComicSerializer

    def get_queryset(self):
        # Filter comics based on the character's ID provided in the query parameters
        character_id = self.request.query_params.get('character_id')
        if character_id:
            try:
                character = Character.objects.get(id=character_id)
                return Comic.objects.filter(character=character)
            except Character.DoesNotExist:
                raise Http404("Character does not exist")
        else:
            # If no character_id is provided, return all comics
            return Comic.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Http404:
            # Handle the case where no comics match the filter
            return Response({"detail": "No comics found with the specified filter."}, status=status.HTTP_404_NOT_FOUND)

class ComicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer

class ApiStatusUpdateView(generics.UpdateAPIView):
    queryset = ApiStatus.objects.all()
    serializer_class = ApiStatusSerializer  # Create a serializer if needed

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.data_loaded = request.data.get('data_loaded', instance.data_loaded)
        instance.save()
        return Response({"message": "ApiStatus updated successfully"}, status=status.HTTP_200_OK)
