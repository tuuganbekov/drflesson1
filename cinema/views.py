from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.parsers import MultiPartParser, FormParser


from .models import Movie, Genre
from .serializers import MovieModelSerializer, GenreSerializer, MovieSerializer, UserSerializer


# @api_view(['POST'])
# def user_register(request):
#     serializer = UserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     return Response({"message": "Регистрация прошла успешно"})
#
#
# @api_view(['GET', 'POST'])
# def hello_api(request):
#     if request.method == 'GET':
#         data = {
#             "message": "Hello, this is my first function based API",
#             "status": "Success",
#             "is_active": True,
#             "numeric_value": 2025
#         }
#         return Response(data=data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         name = request.data.get("name", "Гость")
#         data = {
#             "message": f"Привет, {name}!"
#         }
#         return Response(data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['POST'])
# def reverse_view(request):
#     text = request.data.get("text", "")
#     # is_palindrome = True if text.lower() == text[::-1].lower() else False
#     data = {
#         "reversed": text[::-1],
#         "is_palindrome": True if text.lower() == text[::-1].lower() else False
#     }
#     return Response(data, status=status.HTTP_200_OK)
#
#
# @api_view(['POST'])
# def reverse_number(request):
#     num = request.data.get('number')
#     if num < 0:
#         return Response({
#             "reverse": int(str(abs(num))[::-1]) * (-1)
#         }, status=status.HTTP_200_OK)
#     return Response({"reverse": int(str(num)[::-1])})
#
#
# @api_view(['GET', 'POST'])
# @parser_classes([MultiPartParser, FormParser])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response({
#             "movies": serializer.data
#         }, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         print("REQUEST FILES: ", request.FILES)
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def genre_list(request):
#     if request.method == "GET":
#         genres = Genre.objects.all()
#         serializer = GenreSerializer(genres, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer = GenreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def genre_detail(request, pk):
#     try:
#         genre = Genre.objects.get(id=pk)
#         print(f"GENRE: {genre}, type: {type(genre)}")
#         serializer = GenreSerializer(genre)
#         print(f"SERIALIZER DATA: {serializer.data}")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Genre.DoesNotExist:
#         return Response({
#             "message": f"Жанр с ID {pk} не существует"
#         }, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['PUT'])
# def genre_update(request, pk):
#     try:
#         genre = Genre.objects.get(id=pk)
#         serializer = GenreSerializer(genre, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Genre.DoesNotExist:
#         return Response({
#             "message": f"Жанр с ID {pk} не существует"
#         }, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['DELETE'])
# def genre_delete(request, pk):
#     try:
#         genre = Genre.objects.get(id=pk)
#         genre.delete()
#         return Response(
#             {"message": "Успешно удалено"},
#             status=status.HTTP_204_NO_CONTENT
#         )
#     except Genre.DoesNotExist:
#         return Response(
#             {"message": f"Жанр с ID {pk} не существует"},
#             status=status.HTTP_404_NOT_FOUND
#         )
    

class GenreAPIView(views.APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreRetrieveUpdateDestroyAPIView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieAPIView(views.APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieModelSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieRetrieveUpdateDestroyAPIView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieModelSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieModelSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieModelSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











