# views.py


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.utils import timezone



@api_view(['POST'])
def add_task(request):
    if request.method == "POST":
        # Extract data from the request
        title = request.data.get('title')
        description = request.data.get('description')
        user_id = request.data.get('user')  # Get user ID from request

        # Create a new Task instance
        task = Task(
            title=title,
            description=description,
            status='todo',
            user_id=user_id  # Directly use user_id
        )
        
        task.save()  # Save the task to the database

        return Response({"message": "Task added successfully!", "task": {"id": task.id, "title": task.title}}, status=status.HTTP_201_CREATED)

    return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt  # Use only during testing, secure this in production
def all_tasks(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        
        if user_id:
            # Fetch tasks based on the user_id
            tasks = Task.objects.filter(user_id=user_id).values()  # Assuming Task has a `user_id` field
            return JsonResponse(list(tasks), safe=False)
        else:
            return JsonResponse({"error": "User ID not provided"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
    

def get_user_tasks(request, user_id):
    if request.method == 'GET':
        tasks = Task.objects.filter(user_id=user_id)  # Adjust based on your model
        tasks_list = [{'id': task.id, 'title': task.title,'description':task.description,'start_date':task.start_date,'end_date':task.end_date,'status':task.status} for task in tasks]  # Customize fields
        return JsonResponse({'tasks': tasks_list})
    

@api_view(['PATCH'])
def start_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.status = 'in_progress'  # Set status to in_progress
        task.start_date = timezone.now()  # Set the start date to now
        task.save()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PATCH'])
def end_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.status = 'done'  # Set status to in_progress
        task.end_date = timezone.now()  # Set the start date to now
        task.save()
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PATCH'])
def edit_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    # Update the task fields directly from the request data
    task.title = request.data.get('title', task.title)  # Use current value if not provided
    task.description = request.data.get('description', task.description)  # Use current value if not provided

    task.save()  # Save the updated task instance

    return Response({'id': task.id, 'title': task.title, 'description': task.description}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        return Response({
            'id': task.id,
            'title': task.title,
            'description': task.description
        }, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    

class TaskDeleteView(APIView):
    def delete(self, request, taskId):
        try:
            task = Task.objects.get(id=taskId)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # Successfully deleted
        except Task.DoesNotExist:
            return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)  # Task not found