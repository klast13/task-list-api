from rest_framework.filters import SearchFilter

from rest_framework.response import Response
from rest_framework import status, viewsets


from task_manager.models import Task
from task_manager.serializers import TaskSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TaskViewSet(viewsets.ViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['completed']

    def list(self, request):
        completed = request.query_params.get('completed')
        queryset = Task.objects.all()

        if completed:
            if completed == 'true':
                queryset = queryset.filter(completed=True)
            if completed == 'false':
                queryset = queryset.filter(completed=False)

        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        task = Task.objects.filter(pk=pk).first()
        if task:
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        task = Task.objects.filter(pk=pk).first()
        if task:
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        task = Task.objects.filter(pk=pk).first()
        if task:
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)