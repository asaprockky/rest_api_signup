from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer
from django.contrib.auth.hashers import check_password
@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

## create new user page
@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid() and not User.objects.filter(name=serializer.validated_data.get('name')).exists():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



## login user page
@api_view(['POST'])
def login_user(request):
    name = request.data.get('name')
    password = request.data.get('password')
    if not name or not password:
        return Response({"error": "Both name and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(name=name)  
        if password == user.password: 
            return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


## get question page
@api_view(["POST"])
def forget_pass(request):
    name = request.data.get("name")
    if User.objects.filter(name = name).exists():
        user = User.objects.get(name = name)
        return Response({"message" : user.security_question})



@api_view(["POST"])
def answer_sec_question(request):
    answer = request.data.get("answer")
    name = request.data.get("name")
    if not name or not answer:
        return Response({"error": "Both name and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(name=name)  
        if answer == user.security_answer: 
            return Response({"message": "Correct_Security_answer"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(["POST"])
def update_password(request):
    new_pass = request.data.get("answer")
    name = request.data.get("name")
    if not name or not new_pass:
        return Response({"error": "Both name and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(name=name)  
        user.password = new_pass
        user.save()
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
