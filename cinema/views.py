from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def hello_api(request):
    if request.method == 'GET':
        data = {
            "message": "Hello, this is my first function based API",
            "status": "Success",
            "is_active": True,
            "numeric_value": 2025
        }
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get("name", "Гость")
        data = {
            "message": f"Привет, {name}!"
        }
        return Response(data, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
def reverse_view(request):
    text = request.data.get("text", "")
    # is_palindrome = True if text.lower() == text[::-1].lower() else False 
    data = {
        "reversed": text[::-1],
        "is_palindrome": True if text.lower() == text[::-1].lower() else False
    }
    return Response(data, status=status.HTTP_200_OK)