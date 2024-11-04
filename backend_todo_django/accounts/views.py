from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    # Create the user
    user = User.objects.create_user(username=username, password=password)
    user.save()

    # Return success response
    return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            request.session['user_id'] = user.id  # Store user ID in session
            return Response({
                "message": "Login successful",
                "userId": user.id,  # Add user ID to the response
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
  

@api_view(['POST'])
def user_logout(request):
    logout(request)  # This logs out the user
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)